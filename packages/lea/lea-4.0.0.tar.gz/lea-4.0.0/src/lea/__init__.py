"""
--------------------------------------------------------------------------------

    __init__.py

--------------------------------------------------------------------------------
Copyright 2013-2024 Pierre Denis

This file is part of Lea.

Lea is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Lea is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with Lea.  If not, see <http://www.gnu.org/licenses/>.
--------------------------------------------------------------------------------
"""

from .lea import *
from .alea import *
from .olea import *
from .plea import *
from .evidence_ctx import *
from .exceptions import *
from .license import VER as __version__

# remove modules from imported names
del lea, alea, blea, clea, dlea, flea, flea1, flea2, flea2a, glea, ilea, olea, plea, \
    rlea, slea, tlea, toolbox, number, exceptions, license

# init Lea package with default 'x' type code: if a probability is expressed as
# a string, then the target type is determined from its content
# - see Alea.prob_any method
set_prob_type('x')
