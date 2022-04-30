# This file, when placed in a directory, indicates that the directory is a package.
# It must always have the same name "__init__.py".
# It may remain empty, or may contain initialising statements for the package whenever it is called by a program.
from .informalGreetings import *
from .formalGreetings import formalGreet1
# NOTES PART 1
# Relative imports cannot be used with "import .a" form. Use "from . import a" instead.
# Relative import specifices the resource relative to the current location.
# In this case, the resource is a module relative to the program importing the package.

# NOTES PART 2
# In the "__init__.py" file, you must precede every module name with a '.'.
# The import functions in this file ensure that the module elements are more easily accessible to the program importing the whole package.
# In this case, I have imported them such that they will be accessible through the package name as though the package were a module with these elements.