import os

path = input("111:")

print("exist:", os.access(path, os.F_OK))
print("read:", os.access(path, os.R_OK))
print("write:", os.access(path, os.W_OK))
print("execute:", os.access(path, os.X_OK))
