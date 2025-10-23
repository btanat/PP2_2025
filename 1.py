a = list(map(int, input().split()))
result = a[0]
for i in range(1, len(a)):
    result *= a[i]

print(result)

from functools import reduce

numbers = [2, 3, 4, 5]

result = reduce(lambda x, y: x * y, numbers)
print("Result:", result)
