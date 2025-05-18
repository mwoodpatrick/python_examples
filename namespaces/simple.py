#! /usr/bin/env python
# This is main_script.py

import sys
import os

# Import the entire module
import my_module

x=5 # a local variable

# Every Python module has a special built-in global variable called __name__. 
# Its value depends on how the module is being used:
# If the script is being run directly (as the main program), the value of __name__ is set to the string "__main__".
# If the module is being imported into another script or module, the value of __name__ is set to the module's name (which is usually the filename without the .py extension, relative to the import path).
print(f'Hello From script {sys.argv[0]} module name {__name__} x={x}')

# This is the standard way to check if a script is being run as the main program (hence the common if __name__ == "__main__": block).

if __name__ == "__main__":
    print(f'The script {__name__} is being run directly.')
else:
    print(f'The script {__name__} is being imported as a module.')

# Access the variable from the module
print(my_module.greeting)

# Call the function from the module
message = my_module.greet("Alice")
print(message)

# You can also import specific things from a module
from my_module import greeting as module_greeting, greet as module_greet

print(module_greeting)
print(module_greet("Bob"))

# Note: The print statement inside my_module.py runs when the module is imported.

# Trying to access the internal helper function (possible but convention suggests not to)
# my_module._internal_helper()

