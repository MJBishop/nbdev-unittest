# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/00_test_core.ipynb.

# %% auto 0
__all__ = ['TestCore']

# %% ../../nbs/00_test_core.ipynb 1
from ..core import *

# %% ../../nbs/01_core.ipynb 4
import unittest

class TestCore(unittest.TestCase):
    
    def test_foo(self):
        self.assertEqual(foo(), 'foobar')