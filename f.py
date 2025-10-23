import os
import string

folder = "C:/Users/Батыр/Desktop/PP2_2025/lab6/folder_for_f.py"

os.makedirs(folder, exist_ok=True)

for letter in string.ascii_uppercase:
    filename = folder + "/" + letter + ".txt"
    
    with open(filename, 'w') as f:
        f.write(f"{letter}")

print("Success!")