# -*- coding: cp936 -*-
from distutils.core import setup
import py2exe


includes = []
excludes =[]
packages = []
dll_excludes = [] 
'''
['libgdk-win32-2.0-0.dll', 'libgobject-2.0-0.dll', 'tcl84.dll',
                'tk84.dll',"MSVCP90.dll"]
'''
setup(
    options = {"py2exe": {"compressed": 2, 
                          "optimize": 2,
                          "includes": includes,
                          "excludes": excludes,
                          "packages": packages,
                          "dll_excludes": dll_excludes,
                          "bundle_files": 3,
                          "dist_dir": "dist",
                          "xref": False,
                          "skip_archive": False,
                          "ascii": False,
                          "custom_boot_script": '',
                         }
              },

    console=['encrypt.py']
)

