# freezing the program
import sys
from cx_Freeze import setup, Executable

import os.path
PYTHON_INSTALL_DIR = os.path.dirname(os.path.dirname(os.__file__))
os.environ['TCL_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tcl8.6')
os.environ['TK_LIBRARY'] = os.path.join(PYTHON_INSTALL_DIR, 'tcl', 'tk8.6')


base = None
if sys.platform == 'win32' : base = 'Win32GUI'

opts = {'include_files': ['logo.gif'], 'includes': ['re']}

setup( name = 'Lotto', 
	   version = '1.0',
	   description = 'Lottery number picker',
	   author = 'Mike McGrath',
	   options = {'build_exe': opts},
	   executables = [Executable('Chapter10_lotto.py', base = base)])
	   