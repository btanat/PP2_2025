text = ["1", "2", "3", "hdgyudfguygdsufsgu"]

filename = "C:\\Users\\Батыр\\Desktop\\PP2_2025\\lab6\\1.txt"


with open(filename, 'w') as f:
    for i in text:
        f.write(i + "\n")

print("Success!")