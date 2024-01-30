## Misc. helpers

import os
import re


def compose(*fs):
    """Return a new function that compose functions in fs.

    Functions in fs are unary functions.
    """

    def inner(arg):
        for f in reversed(fs):
            arg = f(arg)
        return arg

    return inner


def compose2(*fs):
    """Return a new function that compose functions in fs.

    Functions in fs are unary functions, except for the last,
    that may take any number of arguments.
    """

    def inner(*args, **kwargs):
        arg = fs[-1](*args, **kwargs)
        for f in reversed(fs[:-1]):
            arg = f(arg)
        return arg

    return inner


def get_tag_data(tag, text, default=None):
    """Return the tag content as found in text.

    tag is an xml tag name (e.g., 'id', 'version', etc.).
    test is a string possibly containing the tag.
    default is the optional tag value, returned if tag not in text.

    Only return the content of the first matching tag in text.

    Tag arguments are ignored.
    """
    return (
        re.search(r'<%s(\s+[^>]*)?>([^<]+)</%s>' % (tag, tag), text).group(2)
        if '<' + tag in text
        else default
    )


def simple_mime_type(f):
    """Return 'archive' or 'file' depending on file f type.

    If needed, can be made to use the magic library.
    """
    a = os.path.splitext(f)[1].lower() in ('.zip', '.rar', '.7z', '.gz')
    t = 'application/x-compressed' if a else ''

    return 'archive' if t == 'application/x-compressed' else 'file'
