def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]


input_str = input("Enter a string: ")
if is_palindrome(input_str):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

def pal(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

text = input("blablabla:")
if pal(text):
    print("si")
else: 
    print("no")