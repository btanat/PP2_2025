text = ["1", "2", "3"]
with open("1.txt", "w") as f:
    f.writelines(item + "\n" for item in text)
