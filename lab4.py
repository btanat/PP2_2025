def generate_squares(n):
    for i in range(1, n + 1):
        yield i ** 2

a = int(input("num: "))
for num in generate_squares(a):
    print(num, end=" ")


def generate_even_numbers(n):
    for i in range(1, n + 1):
        if i % 2 == 0:
            yield i

b = int(input("num: "))
print(", ".join(str(i) for i in generate_even_numbers(b)))


def divisible_by_3_and_4(n):
    for i in range(0, n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

c = int(input("Enter n: "))
for num in divisible_by_3_and_4(c):
    print(num, end=" ")


def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2

a1 = int(input("Enter start: "))
b1 = int(input("Enter end: "))
for sq in squares(a1, b1):
    print(sq)

def countdown(n):
    while n >= 0:
        yield n
        n -= 1

d = int(input("Enter n: "))
for num in countdown(d):
    print(num, end=" ")


from datetime import datetime, timedelta, date

current_date = datetime.now()
new_date = current_date - timedelta(days=5)

print("Current date:", current_date)
print("Date 5 days ago:", new_date)


today = date.today()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Yesterday:", yesterday)
print("Today:", today)
print("Tomorrow:", tomorrow)

now = datetime.now()
no_microseconds = now.replace(microsecond=0)

print("With microseconds:", now)
print("Without microseconds:", no_microseconds)

date1 = datetime(2025, 10, 9, 12, 0, 0)
date2 = datetime(2025, 10, 8, 11, 30, 0)

difference = (date1 - date2).total_seconds()

print("Difference in seconds:", difference)

#radian

import math

degree = float(input("Input degree: "))
radian = degree * (math.pi / 180)
print("Output radian:", round(radian, 6))

#trapezoid

height = float(input("Height: "))
base1 = float(input("Base, first value: "))
base2 = float(input("Base, second value: "))

area = ((base1 + base2) / 2) * height
print("Expected Output:", area)

#polygon

n = int(input("Input number of sides: "))
s = float(input("Input the length of a side: "))

area = (n * s ** 2) / (4 * math.tan(math.pi / n))
print("The area of the polygon is:", round(area, 2))

#parallelogram

base = float(input("Length of base: "))
height = float(input("Height of parallelogram: "))

area = base * height
print("Expected Output:", area)

import json


with open('pp2.json') as f:
    data = json.load(f)


print("Interface Status")
print("=" * 80)
print(f"{'DN':<50} {'Description':<20} {'Speed':<8} {'MTU':<6}")
print("-" * 80)


for item in data["imdata"]:
    dn = item["l1PhysIf"]["attributes"]["dn"]
    descr = item["l1PhysIf"]["attributes"]["descr"]
    speed = item["l1PhysIf"]["attributes"]["speed"]
    mtu = item["l1PhysIf"]["attributes"]["mtu"]
    
    print(f"{dn:<50} {descr:<20} {speed:<8} {mtu:<6}")
