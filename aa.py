import os

path = input("way:::")
dirs = []
for i in os.listdir(path):
    if os.path.isdir(path + "/" + i):
        dirs.append(i)

print(dirs)

files = []
for i in os.listdir(path):
    if os.path.isfile(os.path.join(path, i)):
        files.append(i)

print(files)

allitems = os.listdir(path)
print(allitems)