# my_package/__init__.py

"""
My Package

This is a sample Python package demonstrating key __init__.py attributes.
It provides some utility functions and classes.

A Python package, particularly in its top-level __init__.py file, often defines several special attributes (often referred to as "dunder" attributes due to the double underscores) for various purposes, including providing metadata and controlling the package's behavior when imported.

While Python doesn't strictly require all of these, defining them is considered good practice and helps users understand and work with your package.

Here are some of the key attributes a Python package should or commonly does define:

__version__:

Purpose: Specifies the version number of the package. This is crucial for tracking releases and dependencies.
Example: __version__ = "1.2.0"
__author__:

Purpose: Indicates the author or authors of the package.
Example: __author__ = "Jane Doe"
__email__:

Purpose: Provides contact information for the author(s).
Example: __email__ = "jane.doe@example.com"
__license__:

Purpose: Specifies the software license under which the package is distributed.
Example: __license__ = "Apache-2.0" (Note: often the full license text or a reference to a LICENSE file is included in the package distribution, but this attribute provides a quick indication).
__all__:

Purpose: This is a list of strings defining the names that should be imported when a user uses the wildcard import statement (from package import *). If __all__ is not defined, import * will import all public names defined directly in the __init__.py file (names not starting with _). Defining __all__ is explicit and recommended if you want to control what import * does.

Other Attributes (Often Set Automatically or Defined Elsewhere):

__name__: Automatically set by Python to the package's name when imported (e.g., "my_package").
__package__: Automatically set by Python to the name of the package (e.g., "my_package").
__file__: Automatically set by Python to the path of the __init__.py file.
__path__: Automatically set by Python for packages; it's a list containing the path(s) to the directory(ies) containing the package.
__doc__: The package's docstring (the string literal right at the top of the __init__.py file) becomes the package's documentation string.
Formal Package Metadata:

It's important to note that while __version__, __author__, etc., are often defined in __init__.py for programmatic access within the package, the comprehensive metadata used by packaging tools (like pip and build systems) for distribution on PyPI is primarily defined in your project's pyproject.toml file (or the older setup.py/setup.cfg files). This metadata includes the package name, description, URLs (homepage, repository), dependencies, etc. There might be some overlap (e.g., defining the version in both places, often linking the pyproject.toml version to __version__ in __init__.py via tools).
"""

# --- Package Metadata Attributes ---

# The version of the package
__version__ = "1.0.0"

# The author(s) of the package
__author__ = "Your Name"

# The primary contact email for the author(s)
__email__ = "your.email@example.com"

# The license under which the package is distributed
__license__ = "MIT"


# relative imports (.) to bring specific names (function_x, ClassY, MY_CONSTANT) 
# from the sub-modules (module_a.py, module_b.py) into the my_package namespace.
# --- Import selected components from sub-modules ---
# These imports make the specified names available directly under the package namespace
from .module_a import function_x, ClassY
from .module_b import MY_CONSTANT


# --- Define __all__ for wildcard imports ---
# This list specifies the names that are imported when a user does 'from my_package import *'
__all__ = [
    "__version__", # It's common to include version/author info in __all__
    "__author__",
    "__email__",
    "__license__",
    "function_x",
    "ClassY",
    "MY_CONSTANT",
    # Note: 'another_function' from module_b is NOT included in __all__,
    # so it won't be imported with 'from my_package import *'
    # but can still be imported directly like 'from my_package.module_b import another_function'
]


# --- Optional: Initialization code that runs when the package is imported ---
# print("My Awesome Package is being initialized!")

# You could also set up logging here, etc.


