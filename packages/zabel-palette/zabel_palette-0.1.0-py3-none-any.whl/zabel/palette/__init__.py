# Copyright (c) 2019 Martin Lafaix (martin.lafaix@external.engie.com)
#
# This program and the accompanying materials are made
# available under the terms of the Eclipse Public License 2.0
# which is available at https://www.eclipse.org/legal/epl-2.0/
#
# SPDX-License-Identifier: EPL-2.0

"""The root of the **mlf** library.

The **mlf** library offers the following modules:

- async
- date
- db
- html
- http
- misc
- text
- timeline

The modules can be used independently.  They share the same logger, and
have a common epoch, though.
"""

__author__ = 'Martin Lafaix'
__copyright__ = 'Copyright 2016, 2017, 2018'
__license__ = 'GPL'
__version__ = '0.0.18'
__maintainer__ = 'Martin Lafaix'
__email__ = 'mlafaix@qualixo.com'
__status__ = 'Alpha'


import datetime
import logging as _logging


_logging.getLogger(__name__).addHandler(_logging.NullHandler())
_EPOCH = datetime.datetime.now()
