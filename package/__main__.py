#!/home/user/miniconda3/envs/bi-pyt/bin/python
import sys

print("Package ran as a script.")

if len(sys.argv) >= 2:
    print(f"First argument is: {sys.argv[1]}")