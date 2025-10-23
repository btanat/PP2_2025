import os

path = input("Where:")

print("Existance:", os.access(path, os.F_OK))
print(os.path.dirname(path))
print(os.path.basename(path))