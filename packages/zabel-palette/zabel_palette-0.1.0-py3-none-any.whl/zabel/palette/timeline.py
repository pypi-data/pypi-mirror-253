# Copyright (c) 2019 Martin Lafaix (martin.lafaix@external.engie.com)
#
# This program and the accompanying materials are made
# available under the terms of the Eclipse Public License 2.0
# which is available at https://www.eclipse.org/legal/epl-2.0/
#
# SPDX-License-Identifier: EPL-2.0

## Timeline helpers

import datetime

from zabel.palette import _EPOCH
from .text import safe


_time_log = [(_EPOCH, None)]


def add_to_timeline(event):
    """Add a new event to the global timeline."""
    global _time_log

    _time_log += [(datetime.datetime.now(), event)]


def get_timeline():
    """Return the global timeline events."""
    timeline = []
    prev = _time_log[0][0]
    for t in _time_log[1:]:
        timeline += [str(t[0] - prev) + ' (%s)' % safe(t[1])]
        prev = t[0]

    return ' - '.join(timeline)
