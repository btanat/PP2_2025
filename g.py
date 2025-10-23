

s = input("s: ")
d = input("d")

with open(s, "r") as src:
    content = src.read()

with open(d, "w") as dest:
    dest.write(content)

print("File copied successfully!")
