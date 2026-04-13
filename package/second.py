import sys

print("I am second module")

def hello():
    print("Hello world!")

if __name__ == "__main__":
    if len(sys.argv) >= 2:
        print(f"The argument is: {sys.argv[1]}")