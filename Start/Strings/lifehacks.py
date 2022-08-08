print("I'm Iulian and I'm a \"strong\" programmer")
print(r'C:\Users\EngineerSpocok')

greeting = str("Hello, my name is Iulian")
print(greeting[-1]) # n
print(greeting[1]) # e


#! Срезу строк 

print(greeting[2:]) # llo, my name is Iulian
print(greeting[0:3]) # Hel
print(greeting[::2]) # Hlo ynm sIla
print(greeting[3:25:2]) # l,m aei uin

#! Конкатенация 

print("My name is" + " " + "Iulian")
hello = "hello"
world = "world"
print(hello + " " + world) # hello world
print("%s %s" % (hello,world)) # hello world
print("{} {}".format(hello,world)) # hello world

print('a'*5) # aaaaa
