import os

path = input("Enter path: ")

print("Directories:")
print([d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))])

print("Files:")
print([f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])

print("All:")
print(os.listdir(path))


path = input("Введите путь к папке: ")

print("Список папок:")
dirs = []
for name in os.listdir(path):
    if os.path.isdir(os.path.join(path, name)):
        dirs.append(name)
print(dirs)

print("Список файлов:")
files = []
for name in os.listdir(path):
    if os.path.isfile(os.path.join(path, name)):
        files.append(name)
print(files)

print("Все файлы и папки:")
all_items = os.listdir(path)
print(all_items)

