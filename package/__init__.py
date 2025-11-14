# 1. Adds: import package >>> package.first, import package.CONSTANT
from . import first
from .first import CONSTANT

print("I am a package")

# 2. Specifies: from package import * -> only CONSTANT and second module. By default imports all in this file (first, CONSTANT).
__all__ = ["CONSTANT", "second"]

# 3. `from package import second` and `import package.second` can not be restricted