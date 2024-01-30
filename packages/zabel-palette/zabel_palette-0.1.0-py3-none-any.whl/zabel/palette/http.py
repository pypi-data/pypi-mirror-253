# Copyright (c) 2019 Martin Lafaix (martin.lafaix@external.engie.com)
#
# This program and the accompanying materials are made
# available under the terms of the Eclipse Public License 2.0
# which is available at https://www.eclipse.org/legal/epl-2.0/
#
# SPDX-License-Identifier: EPL-2.0

# HTTP Helpers

import cgi
import datetime
import http.cookies
import os
import sys

from html import escape

from zabel.palette import _EPOCH, _logging
from .date import datetime_as_text, text_as_date
from .timeline import get_timeline
from .text import safe, pprint


HOST_NAME = escape(os.environ['HTTP_HOST'])
SCRIPT_NAME = escape(os.environ['SCRIPT_NAME'])
pyname = os.path.split(SCRIPT_NAME)[1]

_admin = False
_application_title = None


########################################################################

## HTML Templates
htmlTemplateLogin = '''<!DOCTYPE html>
<html lang="fr">
<head>
    <title>{application_title} - Login</title>
    <meta content="text/html; charset=windows-1252" http-equiv="content-type">
    <script language='JavaScript'>
        function loginaction()
        {{
            document.getElementById("loginform").submit();
        }}
    </script>
    <link rel="stylesheet" href="/resources/css/cpm.css" type="text/css"/>
</head>
<body>
    <h1>{application_title} - Login</h1>

    <!-- MSG -->

    <div class="block">
    <h2>Login</h2>
    <table width="100%">
        <tr>
            <td>
                <form id="loginform"
                      name="loginform"
                      action="?wa=access"
                      method="post">
                    insert password here:&nbsp; <input type="password"
                                                       name="pwd"
                                                       id="pwd"/>
                </form>
            </td>
        </tr>
        <tr>
            <td>
                <input type="button"
                       onclick="javascript:loginaction();"
                       value="login"/>
            </td>
        </tr>
    </table>
    </div>
</body>
</html>'''

htmlHeader_tmpl = '''<!DOCTYPE html>
<html lang="fr">
<head>
    <title>{title}</title>
    <meta content="text/html; charset=windows-1252" http-equiv="content-type">
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <script>function logout()
        {{
            window.location.href = '?wa=logout';
        }}
        function show_newapp(d)
        {{
            document.getElementById(d).style.display='block';
        }}
        function hide_newapp(d)
        {{
            document.getElementById(d).style.display='none';
        }}
        function do_form(form)
        {{
            document.getElementById(form).submit();
        }}
        function do_instance(action, instance)
        {{
            window.location.href = '?a=' + action +'/' + instance;
        }}
        function do_transfer(triplette, src, dst)
        {{
            window.location.href = '?a=copy/' + src + '/' + triplette
                                 + '/' + dst + '/' + triplette;
        }}
    </script>
    <link rel="stylesheet" href="/resources/css/cpm.css" type="text/css"/>
    <script src="/resources/js/Chart.min.js"></script>
    <script src="/resources/js/list.min.js"></script>
</head>
<body class="second">
    <h1>{action}{title}</h1>
    <div class="watermark">{watermark}</div>
    <h3 class="extraction">Photo effectuée le {epoch}</h3>
'''

htmlFooter_tmpl = '''<p class="footnote">Généré en {elapsed} - {details}</p>
</body>
</html>'''

messages = {
    'pwdexpired': 'The specified account has expired, please '
    'contact the CAST administrators to re-enable '
    'it if needed.',
    'nopwd': 'You must specify a password.',
    'pwdnotequal': 'Unknown account.',
}

logout_tmpl = '<a href="javascript:logout();" title="Déconnexion"><img class="icon" src="/resources/img/logout.png" alt="Déconnexion"/></a>'
back_tmpl = '<a href="?" title="Retour à la page d\'accueil"><img class="icon" src="/resources/img/back_arrow.png" alt="Retour"/></a>'

access_denied_tmpl = '<p>Accès non autorisé</p>'

header_admin_tmpl = ' (Administration)'


########################################################################
## LIBRARY

## Routes helpers


def _find_matching_pattern(request, rs):
    """Return the most precise matching key in rs, if any, or None.

    request is the user request.
    rs is a dict of pattern: handler entries.

    If there is an exact match, it wins.
    If not, if there is an exact partial match, it wins.
    If not, if there is a relative match, it wins.
    If not, if there is a double relative match, it wins.
    If not, if there is a default route, it wins.
    If not, return None.
    """
    if request in rs:
        return request
    if '/' in request and ('%s/{}' % request.split('/')[0]) in rs:
        return '%s/{}' % request.split('/')[0]
    if '/' not in request and '{}' in rs:
        return '{}'
    if '/' in request and '{}/{}' in rs:
        return '{}/{}'
    if ... in rs:
        return ...

    return None


def _do_route(request, route):
    """Execute the route request, and the ensuing redirection if any.

    request is the user request (possibly None).
    route is the handler, a function of one or two arguments.
    """
    if request is not None and '/' in request:
        path = request.split('/')
        _do_forward(route(path[0], '/'.join(path[1:])))
    else:
        _do_forward(route(request))


def _do_forward(destination, msg=None):
    """Execute the redirection request, adding msg to log if given.

    destination is the target URL.
    msg is an optional message to log.
    """
    if msg is not None:
        _logging.info(msg)
    _do_page(
        '''<!DOCTYPE html><html><body><script language="JavaScript">
                    window.location.href = '{destination}';
                </script></body></html>'''.format(
            destination=destination
        )
    )


def handle_request(application, queries):
    """Handle the request defined by queries.

    Authentication is performed beforehand.

    application is a dict containing (at least) two entries, routes and
        default.
    queries is a dict (possibly None, possibly empty) of args: values,
        all items being strings. (It is typically build from the
        request URI as in 'dict(parse_qsl(urlparse(URI)[4]))'.)

    routes defines routing (see below).
    default is a pair present in routes.

    If queries contains more than one request, only the one with the
    highest priority is processed (as defined by routes, first matching
    entry wins).

    If no matching route is found, the default route in routes[default]
    will be used (an error is raised if there is no default route
    defined).

    A request either completes or returns a new request. If a new
    request is returned, it will be handled (possibly recursively).

    routes is a non-empty list of [(string, bool), patterns, ...]

    (string, bool) is a pair, whose first element is a string (arg in
        query) and second element is True if admin rights are required
        for the routes or False otherwise).
    patterns is a dict listing the routes patterns: {pattern: fn, ...}.

    pattern is a string like 'foo[/bar]', or Ellipsis (...). If foo
        is a place-holder ('{}'), bar must be one too if specified.
    fn is a function of one or two arguments (two if pattern includes a
        '/', one otherwise). The first argument will be the leading
        element (what is before the first '/'), the second the remaining
        elements (what is after, if applicable). This function either
        exits (in wich case the script ends) or returns a string that
        is used as a redirection.

    Pattern examples:

        'abc'     -- matches 'abc' only
        'abc/d'   -- matches 'abc/d' only
        'abc/{}'  -- matches 'abc/xxx' and 'abc/', but not 'abc'
        '{}'      -- matches 'abc', 'def', but neither '' nor 'abc/def'
        '{}/abc'  -- matches nothing (invalid construction)
        '{}/{}'   -- matches 'abc/xxx', 'abc/', and 'def/ghi', but not
                  -- 'abc'
        ...       -- matches everything

    Routes example:

        [('a', True), {'foo': bar, '{}/{}': xyzzy},
         ('b', False), {...: baz}]

    It will handle queries like:

        a=foo     -- assuming admin rights, call bar('foo')
        a=x/y/z   -- assuming admin rights, call xyzzy('x', 'y/z')
        b=        -- regardless of admin status, call baz('')
        b=x       -- regardless of admin status, call baz('x')
        b=x/y/z   -- regardless of admin status, call baz('x', 'y/z')
        a=ABC     -- not handled (except if default is ('b', False), in
                  -- which case baz(None) is called.
    """
    _handle_access_actions_and_controls(application, queries)

    routes = application['routes']
    for i in range(0, len(routes) // 2):
        k, restricted = routes[i * 2]
        patterns = routes[i * 2 + 1]

        if not restricted or (restricted and is_admin()):
            if k in queries:
                request = queries[k]
                route = _find_matching_pattern(request, patterns)
                if route is not None:
                    _do_route(request, patterns[route])

    # default route
    try:
        _do_route(None, routes[routes.index(application['default']) + 1][...])
    except Exception as e:
        _do_error('handle_request', 'Default route' + str(e))


## Access helpers


def _handle_access_actions_and_controls(application, qsList):
    """Handle access actions.

    application is a dict with (at least) three entries, title, accounts
        and cookie.
    qsList is a dict (possibly None, possibly empty) of args: values,
        all items being strings. (It is typically build from the
        request URI as in 'dict(parse_qsl(urlparse(URI)[4]))'.)

    title is the application title.
    accounts is a dict of password: account entries, account being a
        list/tupple of at least 3 elements describing the account.
    cookie is the used cookie name to store credentials (the password).

    account first element is the account name. If it starts with the
    'admin' string, it has administrator rights.
    account third element is the account expiration date, in
    'yyyy-mm-dd' format.  Access attempts at a later date will be
    rejected with a 'password expired' message.
    The other elements in account are not used by this function.

    Never returns except if account is authorized.

    If a "web action" ('wa' key in qsList) is specified and is one of
    'logout', 'login', or ' access', it is handled first. (Other web
    actions are ignored, i.e, they perform no specific action).
    """
    global _admin, _application_title

    action = qsList['wa'] if 'wa' in qsList else None  # web action

    _application_title = application['title']
    accounts = application['accounts']
    cookie = application['cookie']

    if action == 'logout':
        # log out
        _setCookieKey(cookie, '')
        _do_forward(pyname, 'logout ok')

    if action == 'login':
        # login page request
        _logging.info('login screen')
        tmpl = htmlTemplateLogin.format(application_title=_application_title)
        if 'msg' in qsList and qsList['msg'] in messages:
            # update informations with specified message
            repl = safe(messages[qsList['msg']])
            tmpl = tmpl.replace(
                '<!-- MSG -->', '<p><strong>{m}</strong></p>'.format(m=repl)
            )
        _do_page(tmpl)

    if action == 'access':
        # check for password
        fs = cgi.FieldStorage()
        if 'pwd' not in fs:
            _do_forward('?wa=login&msg=nopwd', 'access failed (no pwd)')

        sendkey = fs['pwd'].value

        if sendkey not in accounts:
            _do_forward(
                '?wa=login&msg=pwdnotequal', 'access failed (unknown pwd)'
            )

        if text_as_date(accounts[sendkey][2]) <= _EPOCH:
            _do_forward(
                '?wa=login&msg=pwdexpired', 'access failed (expired pwd)'
            )

        _setCookieKey(cookie, sendkey)
        _do_forward(
            pyname,
            'access ok (account %s, pwd %s)' % (accounts[sendkey][0], sendkey),
        )

    if _getCookieKey(cookie) not in accounts:
        # not authorized
        _do_forward(
            '?wa=login',
            'access nok (no account for %s)' % _getCookieKey(cookie),
        )

    _admin = accounts[_getCookieKey(cookie)][0].startswith('admin')


# Low-level document emitters


def _do_page(body):
    """Put page in output using text html format."""
    print('Content-type: text/html')
    print()
    print(body)
    sys.exit()


def _do_error(section, msg):
    """Put error in output using text plain format."""
    _logging.error(section, msg)
    print('Content-type: text/plain')
    print()
    print('SECTION:', section)
    print('MESSAGE:', msg)
    sys.exit()


def _emit_header(title, toplevel=False):
    """Write HTML document header."""
    action = logout_tmpl if toplevel else back_tmpl
    watermark = title.split('/')[1] if '/' in title else title

    title_safe = safe(_application_title + ' - ' + title)
    if is_admin():
        title_safe += header_admin_tmpl

    pprint(
        htmlHeader_tmpl.format(
            action=action,
            title=title_safe,
            watermark=safe(watermark),
            epoch=datetime_as_text(_EPOCH),
        )
    )


def _emit_footer():
    """Write HTML document footer."""
    pprint(
        htmlFooter_tmpl.format(
            elapsed=str(datetime.datetime.now() - _EPOCH),
            details=get_timeline(),
        )
    )


## Document types (Decorators)


def attachement(contenttype='text/csv', filename='export.csv'):
    """Decorate a function so that it renders an attachments.

    Whatever the function produces is presented as a file 'filename'
    to the client, of type contenttype.
    """

    def wrap(a):
        def wrapped(*args):
            print('Content-type:', contenttype)  # application/vnd.ms-excel
            print('Content-Disposition: attachment;filename=' + filename)
            print()
            a(*args)
            sys.exit()

        return wrapped

    return wrap


def page(title, restricted, toplevel=False):
    """Decorate a function so that it renders a web page.

    title is the produced page title.  It can contains positional
        substitution parameters, which will be replaced by the
        corresponding parameters passed to the decorated function.
    restricted is either True or False. If True, only admin users
        are allowed, others will see an 'access denied' page.
    toplevel is an optional boolean parameter, defaulting to False.
        If set to True, the page will contain a 'logout' option.
        Otherwise, it will contain a 'go back' option instead.

    Produces a page of type text/html.
    """

    def wrap(p):
        def wrapped(*args, **kargs):
            print('Content-type: text/html; charset=windows-1252')
            print()
            _emit_header(title.format(*args), toplevel)
            if not restricted or is_admin():
                p(*args, **kargs)
            else:
                pprint(access_denied_tmpl)
            _emit_footer()
            sys.exit()

        return wrapped

    return wrap


## Cookies helpers


def _getCookieKey(cn):
    """Get cn key stored in cookie."""
    try:
        if 'HTTP_COOKIE' in os.environ:
            cookie = http.cookies.SimpleCookie(os.environ['HTTP_COOKIE'])
        else:
            cookie = http.cookies.SimpleCookie()

        if cn in cookie:
            return cookie[cn].value
        else:
            return ''

    except http.cookies.CookieError:
        _do_error('_getCookieKey', 'error detected')


def _setCookieKey(cn, cv):
    """Set cn key stored in cookie to cv."""
    try:
        expires = _EPOCH + datetime.timedelta(days=2)
        cookie = http.cookies.SimpleCookie()
        cookie[cn] = cv
        cookie[cn]['domain'] = HOST_NAME
        cookie[cn]['path'] = '/'
        cookie[cn]['expires'] = expires.strftime('%a, %d-%b-%Y %H:%M:%S PST')
        print(cookie)
    except Exception as e:
        _do_error('_setCookieKey', e)


## Misc. helpers


def is_admin():
    """Recognize an administrator account."""
    return _admin


def get_form_data(*fields):
    """Returns a list of fields values in current form, in order.

    If field not in form, value is None if field name starts with '!' or
    '*' and 'no'+name otherwise.

    Leading and trailing '!' and '*' are ignored for field search (i.e.,
    specifying '!foo' will search for field 'foo').

    If field name starts with '*', a list (possibly with only one
    string) is returned for the field value.
    """
    fs = cgi.FieldStorage()
    return [
        (fs.getlist(f.strip('!*')) if f[0] == '*' else fs[f.strip('!*')].value)
        if f.strip('!*') in fs
        else (None if f[0] in '!*' else 'no' + f)
        for f in fields
    ]
