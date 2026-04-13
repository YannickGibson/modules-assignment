1. Create a **regular** package named `package` and verify.
   
2. When importing `package` print `"I am a package."`.
  
3. Create a module within `package` called `first` and print `"I am first module"` on its import.  **Also** add a variable`CONSTANT` set to `1234`.
4. When running `python package/first.py` print `"FIRST MODULE WAS RAN DIRECTLY"`. However, when imported as `from package import first` do not print this text.
   
5. Create another module within `package` called `second` and print `"I am second module"` on import. **Also** add `hello` function printing `"Hello world!"` 
  
6. Make **only** the following accessible `import package` -> `package.first` and `package.CONSTANT`.
   
7. Allow **only** the `second` module and `CONSTANT` from `first` to be accessible by `from package import *`
  
8. On `python -m package` make the last print say `"Package ran as a script."`. Make sure not to have errors in output.
   
9.  On `python -m package.second <my_arg>` print `"The argument is: <my_arg>"` (among other prints).
   
10. Optional: Enable running `package` without specifying `python -m package` (multiple 
ways to achieve this)
