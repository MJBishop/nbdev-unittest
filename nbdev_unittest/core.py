"""Fill in a module description here"""

# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/01_core.ipynb.

# %% auto 0
__all__ = ['NotebookParser']

# %% ../nbs/01_core.ipynb 2
import nbformat
from nbformat.v4 import new_notebook, new_markdown_cell, new_code_cell

from configparser import ConfigParser 

# %% ../nbs/01_core.ipynb 3
class NotebookParser(object):
    """
    NotebookParser

    
    """
    def __init__(self, module_name):
        self._module_name = module_name
        self._repo_string = None

    @property
    def repo_string(self):
        """str: Return the repository name."""
        if self._repo_string == None:
            configure = ConfigParser() 
            configure.read('settings.ini') 
            lib_path = configure.get('DEFAULT','lib_path')
            self._repo_string = lib_path
        return self._repo_string
    
    def module_filename(self, index_str):
        """str: Return the module filename."""
        return f"{index_str}_{self._module_name}.ipynb"
    
    @property
    def default_exp_module_string(self):
        """str: Return the 'default_exp' module string."""
        return f'#| default_exp {self._module_name}'
    
    @property
    def unittest_class_string(self):
        """str: Return the unittest class string."""
        return f'Test{self._module_name[0].upper() + self._module_name[1:]}'
    
    @property
    def unittest_module_string(self):
        """str: Return the unittest module string."""
        return f'tests/test_{self._module_name}'
    
    @property
    def export_string(self):
        return "#| hide \nimport nbdev; nbdev.nbdev_export()"
    
  

