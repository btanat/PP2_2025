import math
import time

num = int(input("num:"))
ttime = int(input("time:"))

time.sleep(ttime / 1000)
result = math.sqrt(num)
print(f"{result} after {ttime} miliseconds")


import time
import math

num = int(input())
milliseconds = int(input())

time.sleep(milliseconds / 1000)
result = math.sqrt(num)

print(f"Square root of {num} after {milliseconds} miliseconds is {result}")
