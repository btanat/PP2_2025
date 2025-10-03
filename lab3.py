import math
import random
from itertools import permutations

class StringClass:
    def __init__(self):
        self.s = ""
    def getString(self):
        self.s = input("Enter a string: ")
    def printString(self):
        print(self.s.upper())

class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length
    def area(self):
        return self.length * self.length

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
    def area(self):
        return self.length * self.width

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def show(self):
        print(f"({self.x}, {self.y})")
    def move(self, x, y):
        self.x = x
        self.y = y
    def dist(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit of {amount} accepted. New balance = {self.balance}")
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrawal of {amount} accepted. New balance = {self.balance}")
        else:
            print("Funds Unavailable!")

def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

def grams_to_ounces(grams):
    return 28.3495231 * grams

def fahrenheit_to_celsius(F):
    return (5/9) * (F - 32)

def solve(numheads, numlegs):
    for chickens in range(numheads+1):
        rabbits = numheads - chickens
        if 2*chickens + 4*rabbits == numlegs:
            return chickens, rabbits
    return None

def filter_prime(numbers):
    return [n for n in numbers if is_prime(n)]

def string_permutations(s):
    return [''.join(p) for p in permutations(s)]

def reverse_sentence(s):
    return ' '.join(s.split()[::-1])

def has_33(nums):
    for i in range(len(nums)-1):
        if nums[i] == 3 and nums[i+1] == 3:
            return True
    return False

def spy_game(nums):
    code = [0,0,7]
    for n in nums:
        if n == code[0]:
            code.pop(0)
        if not code:
            return True
    return False

def volume_sphere(r):
    return (4/3) * 3.14159 * (r**3)

def unique_list(lst):
    result = []
    for x in lst:
        if x not in result:
            result.append(x)
    return result

def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

def histogram(lst):
    for n in lst:
        print('*' * n)

def guess_game():
    print("Hello! What is your name?")
    name = input()
    number = random.randint(1, 20)
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    guesses = 0
    while True:
        guess = int(input("Take a guess: "))
        guesses += 1
        if guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses} guesses!")
            break

movies = [
{"name": "Usual Suspects","imdb": 7.0,"category": "Thriller"},
{"name": "Hitman","imdb": 6.3,"category": "Action"},
{"name": "Dark Knight","imdb": 9.0,"category": "Adventure"},
{"name": "The Help","imdb": 8.0,"category": "Drama"},
{"name": "The Choice","imdb": 6.2,"category": "Romance"},
{"name": "Colonia","imdb": 7.4,"category": "Romance"},
{"name": "Love","imdb": 6.0,"category": "Romance"},
{"name": "Bride Wars","imdb": 5.4,"category": "Romance"},
{"name": "AlphaJet","imdb": 3.2,"category": "War"},
{"name": "Ringing Crime","imdb": 4.0,"category": "Crime"},
{"name": "Joking muck","imdb": 7.2,"category": "Comedy"},
{"name": "What is the name","imdb": 9.2,"category": "Suspense"},
{"name": "Detective","imdb": 7.0,"category": "Suspense"},
{"name": "Exam","imdb": 4.2,"category": "Thriller"},
{"name": "We Two","imdb": 7.2,"category": "Romance"}
]

def is_above_55(movie):
    return movie["imdb"] > 5.5

def good_movies(movies):
    return [m for m in movies if m["imdb"] > 5.5]

def movies_by_category(movies, category):
    return [m for m in movies if m["category"] == category]

def average_imdb(movies):
    return sum(m["imdb"] for m in movies) / len(movies)

def avg_category(movies, category):
    category_movies = [m["imdb"] for m in movies if m["category"] == category]
    return sum(category_movies) / len(category_movies)
