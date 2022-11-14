a = open("testfile.txt", "r")
b = a.readlines()
c = open("numbers.txt", "w")
for x in b:
    c.write(x)
