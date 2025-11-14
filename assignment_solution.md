1. Create a **regular** package named `package` and verify.
    1. Create a folder `package`
    2. Create an empty file `__init__.py` within
    - **Verify:** from `package` parent folder run `python`, then `import package`. -> no errors
2. When importing `package` print `"I am a package."`.
    1. Add `print("I am a package")` into `__init__.py`
    - **Verify:** import `package` -> `"I am a package."`
3. Create a module within `package` called `first` and print `"I am first module"` on its import.  **Also** add a variable`CONSTANT` set to `1234`.
    1. Create a file at `package/first.py`
    2. Put `print("I am first module")` into it.
    3. Put `CONSTANT = 1234`
    - **Verify:** `from package import first` -> `"I am first module"`
   - **Verify:** `first.CONSTANT` -> `1234`
4. When running `python package/first.py` print `"FIRST MODULE WAS RAN DIRECTLY"`. However, when imported as `from package import first`, do not print this text.
    1. In `package/first.py` add:
      ```python
      if __name__ == "__main__":
          print("FIRST MODULE WAS RAN DIRECTLY")
      ```
    - **Verify:** `python package/first.py` -> `"FIRST MODULE WAS RAN DIRECTLY"`
    - **Verify:** `from package import first` -> does not print this uppercase text.
5. Create another module within `package` called `second` and print `"I am second module"` on import. **Also** add `hello` function printing `"Hello world!"` 
    1. Create a file at `package/second.py`
    2. Put `print("I am second module")` into it.
    3. Put `def hello():` with body `print("Hello world!")` into it.
    - **Verify:** `from package import second` -> `"I am second module"`
   - **Verify:** `second.hello()` -> `"I am second module"`
6. Make **only** the following accessible `import package` -> `package.first` and `package.CONSTANT`.
    1. Put `from . import first` into `package/__init__.py`.
    2. Put `from .first import CONSTANT` into `package/__init__.py`.
   - **Verify:** `import package` -> `package.first` is accessible.
   - **Verify:** `package.CONSTANT` -> 1234
7. **Only** allow the `second` module and `CONSTANT` from `first` to be accessible by `from package import *`
    1. Add `__all__ = ["CONSTANT", "second"]` into `package/__init__.py`
   - **Verify:** `from package import *`, then `second` and `CONSTANT` are available, but not `first`.
8. On `python -m package` print `"Package ran as a script."` (among other prints). Make sure not to have errors in output.
    1. Create an empty file `package/__main__.py`
    2. Add `print("Package ran as a script.")`
    - **Verify:** `python -m package` -> `"Package ran as a script."`
9.  On `python -m package.first <my_arg>` print `"First argument is: <my_arg>"` (among other prints).
    1. In `__main__.py` import `sys` module.
    2. Check `len(sys.argv) >= 2` then print `f"First argument is: {sys.argv[1]}"`.
    - **Verify:** `python -m package.first test` -> `"First argument is: test"`
10. Optional: Enable running `package` without specifying `python -m package` 
    1.  Add shebang `#<path to python>` at the top of `package/__main__.py` (`which python`)
    2.  Make `__main__.py` executable: `chmod +x package/__main__.py`
    3.  Create a link to it using `ln -s __main__.py package/package`
    4.  Add full path of `package` folder to `PATH` -> `export PATH="<full/path/to/package>:$PATH"`
    - **Verify:** `package` -> `"Package ran as a script."`