

file = input('name:')

count = 0
with open(file, 'r') as f:
    for i in f:
        count += 1

print(count)