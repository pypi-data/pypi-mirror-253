# Copyright (c) 2019 Martin Lafaix (martin.lafaix@external.engie.com)
#
# This program and the accompanying materials are made
# available under the terms of the Eclipse Public License 2.0
# which is available at https://www.eclipse.org/legal/epl-2.0/
#
# SPDX-License-Identifier: EPL-2.0

## Date helpers

import datetime

from zabel.palette import _EPOCH, _logging


########################################################################
# Constants

EPOCH = _EPOCH

datetime_as_text_tmpl = '{day} à {dt.hour}h{dt.minute:02d}'
date_as_text_tmpl = '{date.day:d}{st} {month} {date.year:04d}'
date_as_text_firstday = 'er'
datetime_as_relative_text_today = 'aujourd\'hui'
datetime_as_relative_text_yesterday = 'hier'
datetime_as_relative_text_tmpl = (
    '{d} à {dt.hour}:{dt.minute:02d}:{dt.second:02d}'
)

months = [
    '',
    'janvier',
    'février',
    'mars',
    'avril',
    'mai',
    'juin',
    'juillet',
    'août',
    'septembre',
    'octobre',
    'novembre',
    'décembre',
]
days = [
    'lundi',
    'mardi',
    'mercredi',
    'jeudi',
    'vendredi',
    'samedi',
    'dimanche',
]


########################################################################
# Functions


def text_as_date(text):
    """Return date object corresponding to text (of form yyyy-mm-dd).

    Returned date object corresponds to end of day (23:59:59).

    Returns 1900-01-01 if text is not a valid date.
    """
    try:
        yyyy, mm, dd = text.split('-')
        tad = datetime.datetime(int(yyyy), int(mm), int(dd), 23, 59, 59)
    except ValueError:
        _logging.warning('text_as_date', 'unexpected date (yyyy-mm-dd)', text)
        tad = datetime.datetime(1900, 1, 1, 23, 59, 59)

    return tad


def date_as_text(d):
    """Return textual representation of date d (of form yyyy-mm-dd).

    Textual representation is of form 'n mmmm yyyy', e.g.,
    '4 décembre 2015'.

    Returns textual representation of 1900-01-01 if d is invalid.
    """
    date = text_as_date(d)
    return date_as_text_tmpl.format(
        date=date,
        month=months[date.month],
        st=date_as_text_firstday if date.day == 1 else '',
    )


def date_as_dd_mm(d):
    """Return dd/mm representation of date d (of form yyyy-mm-dd).

    Returns 01/01 (dd/mm for 1900-01-01) if d is invalid.
    """
    return '{date.day:02d}/{date.month:02d}'.format(date=text_as_date(d))


def date_as_mm_dd(d):
    """Return mm/dd representation of date d (of form yyyy-mm-dd).

    Returns 01/01 (mm/dd for 1900-01-01) if d is invalid.
    """
    return '{date.month:02d}/{date.day:02d}'.format(date=text_as_date(d))


def datetime_as_text(dt):
    """Return textual representation for datetime dt.

    Textual representation is of form 'date_as_text() à hh:mm', e.g.,
    '4 décembre 2015 à 5h04'.
    """
    return datetime_as_text_tmpl.format(
        day=date_as_text(dt.strftime('%Y-%m-%d')), dt=dt
    )


def datetime_as_absolute_text(dt):
    """Return absolute textual representation for datetime dt.

    Absolute textual representation is of form 'yyyy-mm-dd&nbsp;hh:mm:ss'.
    """
    return str(dt)[:19].replace(' ', '&nbsp;')


def datetime_as_humanized_text(dt):
    """Return a human-readable relative form for datetime dt.

    For dates older than 5 days, an absolute date and time is returned.
    """
    then = {'dt': dt, 'd': days[dt.weekday()]}

    m0 = datetime.date.today()
    m1 = m0 - datetime.timedelta(days=1)
    m2 = m0 - datetime.timedelta(days=2)
    m3 = m0 - datetime.timedelta(days=3)
    m4 = m0 - datetime.timedelta(days=4)
    if dt.date() == m0:
        then['d'] = datetime_as_relative_text_today
    elif dt.date() == m1:
        then['d'] = datetime_as_relative_text_yesterday
    if dt.date() in (m0, m1, m2, m3, m4):
        return datetime_as_relative_text_tmpl.format(**then)

    return datetime_as_absolute_text(dt)


def stamp_as_text(stamp):
    """Return textual representation of stamp (of form yymmddhhmmss).

    Textual representation is as datetime_as_text(), e.g.,
    '4 décembre 2015 à 5h04'.
    """
    return datetime_as_text(
        datetime.datetime.strptime('20' + stamp, '%Y%m%d%H%M%S')
    )
