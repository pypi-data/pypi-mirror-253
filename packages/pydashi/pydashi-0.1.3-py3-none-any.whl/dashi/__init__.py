"""
dashi documentations goes here
"""

__version__ = "0.1.3"

from . import histfactory as factory
from .fitting import model,gaussian,poly,leastsq #,poissonllh 
from .visual import visual
from .storage import histsave,histload
from .objbundle import bundle, emptybundle, bundleize

from . import junkbox

import logging
logging.basicConfig(level=logging.INFO)

from . import tests
