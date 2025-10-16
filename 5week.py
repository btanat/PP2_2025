import re

with open("a.txt", "r", encoding="utf-8") as f:
    text = f.read()

print(re.findall(r'ab*', text))
print(re.findall(r'ab{2,3}', text))
print(re.findall(r'[a-z]+_[a-z]+', text))
print(re.findall(r'[A-Z][a-z]+', text))
print(re.findall(r'a.*b', text))
print(re.sub(r'[ ,.]', ':', text))

def snake_to_camel(s):
    parts = s.split('_')
    return parts[0] + ''.join(p.capitalize() for p in parts[1:])
print(snake_to_camel(text))

print(re.split(r'(?=[A-Z])', text))
print(re.sub(r'(?=[A-Z])', ' ', text).strip())

def camel_to_snake(s):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', s).lower()
print(camel_to_snake(text))
