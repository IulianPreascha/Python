with open("test.txt", 'w') as txt:
    txt.write("Name|Phone \n" +
    "John; 1234 \n" +
    "Bob; 5678 \n" +
    "Alice; 9432")

file = open('test.txt')

data = file.read()
print(data)


#! Using the WITH statement a file is closed automatically

with open(r"C:\Users\Iulian\Documents\GitHub\Python\Start\fileSistem\test2.txt", "w") as fp:
    fp.write("Name|Phone \n" +
    "John; 1234 \n" +
    "Bob; 5678 \n" +
    "Alice; 9432")

fp = open(r"C:\Users\Iulian\Documents\GitHub\Python\Start\fileSistem\test2.txt", "r")
data2 = fp.read()
print(data2)
print(fp.read())

fp.seek(0)
print(fp.read())

fp.seek(0)
lines = fp.readlines()
print(type(lines))
print(lines)
print(len(lines))

with open(r"C:\Users\Iulian\Documents\GitHub\Python\Start\fileSistem\sample.txt", "w") as fp:
    fp.write("test")
sample_file = open(r"C:\Users\Iulian\Documents\GitHub\Python\Start\fileSistem\sample.txt")
sample_file.close()
print(sample_file.closed)

with open(r"C:\Users\Iulian\Documents\GitHub\Python\Start\fileSistem\sample.txt") as sample_file:
    sample_data = sample_file.read()
print(sample_data)

with open(r"C:\Users\Iulian\Documents\GitHub\Python\Start\fileSistem\sample.txt", mode='r+') as sample_file:
    sample_file.seek(0, 2)
    sample_file.write('\nToub;5627')
    sample_file.seek(0)
    print(sample_file.read())

with open('abracadabra.txt', mode='w+') as spell_file:
    spell_file.write('abra-abra-abra-cadabra')
    spell_file.seek(0)
    print(spell_file.read())