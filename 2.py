def a(s):
    upper = 0
    lower = 0
    for i in s:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
    print("upper:", upper)
    print("lower:", lower)

    
text = "Hello World"
a(text)


text = input("Enter a string: ")

upper = sum(1 for c in text if c.isupper())
lower = sum(1 for c in text if c.islower())

print("Uppercase letters:", upper)
print("Lowercase letters:", lower)
