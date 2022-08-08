from platform import python_branch


x = "hello, my name is Elias"

print(len(x)) # 24
print(x[len(x)-1]) # n

print(x.count('l')) # 3

print(x.capitalize()) # Hello, my name is elias

upper_cased = x.upper()
print(upper_cased) # HELLO, MY NAME IS ELIAS

lower_cased = x.lower()
print(lower_cased) # hello, my name is elias

print(lower_cased.islower()) # True
print(upper_cased.isupper()) # True
print(x.isupper()) # False
print(x.islower()) # False

#! Find

print(x.find('l')) # 2
print(x.find('l', 5)) # 20
print(x.find('l',5, 10)) # -1 (nu exista)
print(x.find('m',7, 10)) # 7
print(x.find('m',8, 15)) # 12

print(x.find('my')) # 7

#! isalnum (cifre si litere)
print('123abc'.isalnum()) # True
print('123abc!'.isalnum()) # False

#! isalpha

print('123abc'.isalpha()) # False
print('abc'.isalpha()) # True

#! isspace

print("    ".isspace()) # True
print("".isspace()) # False

#? Special case

empty_string = ""
print(empty_string == "") # True

empty_string = "  "
print(empty_string.strip() == "") # True

empty_string = ""
if not empty_string:
    print("not empty")
else:
    print("empty")
# not empty


h = "hello"
print(h.startswith("he")) # True
print(h.endswith("lo")) # True

split = h.split('l')
print(type(split)) # <class 'list'>
print(split) # ['he', '', 'o']
split = h.split('e')
print(split) # ['h', 'llo']

data = "12;10;8;10"
separated_data = data.split(';')
print(separated_data) # ['12', '10', '8', '10']

python = "Python is fun"

print(python.partition('is '))
print(python.partition('not '))

python = "Python is fun, isn't it"
print(python.partition('is'))