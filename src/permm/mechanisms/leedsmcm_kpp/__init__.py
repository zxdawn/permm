__all__ = ['mech']

from permm.getmech import get_pure_mech
from os import path
def mech():
    get_pure_mech(path.basename(path.dirname(__file__)))