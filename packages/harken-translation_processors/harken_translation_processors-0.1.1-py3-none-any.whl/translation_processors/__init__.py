import sys

from funcy import lcat

from .post.fix_cr_lf import *

modules = ("post.fix_cr_lf",)
__all__ = lcat(sys.modules["translation_processors." + m].__all__ for m in modules)
