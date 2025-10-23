import os

path = input("")

if os.path.exists(path):
    if os.access(path, os.R_OK) and os.access(path, os.W_OK):
        os.remove(path)
        print("deleted")
    else:
        print("No")
else:
    print("not exist")
