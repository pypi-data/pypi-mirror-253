# Copyright (c) 2019 Martin Lafaix (martin.lafaix@external.engie.com)
#
# This program and the accompanying materials are made
# available under the terms of the Eclipse Public License 2.0
# which is available at https://www.eclipse.org/legal/epl-2.0/
#
# SPDX-License-Identifier: EPL-2.0

## Misc. text functions

from html import escape


def F(s, n, **extra):
    """Return s with {n} and {s} replaced according to n.

    Also replace existings {xs} in s with the plural form of x, for
    all 'x' in extra (i.e., one-character items in extra) that are
    either integers or floats.

    'F' is a reference to the formatted string literals in Python 3.6+.
    """
    extra.update(
        {
            k + 's': plural(extra[k])
            for k in extra
            if len(k) == 1 and isinstance(extra[k], (int, float))
        }
    )
    return s.format(n=n, s=plural(n), **extra)


def plural(count, mark='s'):
    """Return the plural mark ('s' by default) if count is not 1."""
    return mark if count >= 2 else ''


def pretty(n):
    """Return a locale-pretty form of number n or 'n/a' if not a number."""
    return 'n/a' if n is None else '{s:,}'.format(s=n).replace(',', '&nbsp;')


def small(t):
    """Return t in a span block with class small."""
    return '<span class="small">{text}</span>'.format(text=t)


def _clean_entities(s):
    """Convert diacritics in s to entities."""
    return s.translate(
        dict(
            zip(
                map(ord, 'Ééêèîûùàâô'),
                [
                    '&Eacute;',
                    '&eacute;',
                    '&ecirc;',
                    '&egrave;',
                    '&icirc;',
                    '&ucirc;',
                    '&ugrave;',
                    '&agrave;',
                    '&acirc;',
                    '&ocirc;',
                ],
            )
        )
    )


def pprint(ls, file=None):
    """Write ls on file, removing unnecessary spaces for lines in ls.

    Diacritics in ls are converted to entities using _clean_entities.
    """
    print(
        '\n'.join(
            _clean_entities(' '.join(l.split())) for l in ls.split('\n')
        ),
        file=file,
        flush=True,
    )


def safe(s, spaces=None):
    """Return an HTML-safe version of s, optionnaly replacing spaces."""
    return escape(s) if spaces is None else escape(s).replace(' ', spaces)
