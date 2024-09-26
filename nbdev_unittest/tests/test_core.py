# AUTOGENERATED! DO NOT EDIT! File to edit: ../../nbs/00_test_core.ipynb.

# %% auto 0
__all__ = ['TestNotebookParser']

# %% ../../nbs/00_test_core.ipynb 1
from ..core import *

# %% ../../nbs/01_core.ipynb 5
import unittest

# %% ../../nbs/01_core.ipynb 6
class TestNotebookParser(unittest.TestCase):

    def setUp(self):
        self.test_module_name = 'moduleA'
        self.test_index_str = '02'
    
    def test_repo_string(self):
        notebook_parser = NotebookParser(self.test_module_name)
        self.assertEqual(notebook_parser.repo_string, 'nbdev_unittest')
    
    def test_module_filename(self):
        notebook_parser = NotebookParser(self.test_module_name)
        self.assertEqual(notebook_parser.module_filename(self.test_index_str), '02_moduleA.ipynb')
    
    def test_default_exp_module_string(self):
        notebook_parser = NotebookParser(self.test_module_name)
        self.assertEqual(notebook_parser.default_exp_module_string, '#| default_exp moduleA')
    
    def test_unittest_class_string(self):
        notebook_parser = NotebookParser(self.test_module_name)
        self.assertEqual(notebook_parser.unittest_class_string, 'TestModuleA')

    def test_unittest_module_string(self):
        notebook_parser = NotebookParser(self.test_module_name)
        self.assertEqual(notebook_parser.unittest_module_string, 'tests/test_moduleA')

    def test_export_string(self):
        notebook_parser = NotebookParser(self.test_module_name)
        self.assertEqual(notebook_parser.export_string, '#| hide \nimport nbdev; nbdev.nbdev_export()')
