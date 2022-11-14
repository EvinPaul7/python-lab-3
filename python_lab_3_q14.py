a = open("testfile.txt", "r")
b = a.readlines()
c = open("numbers.txt", "r")
d=c.readlines()
for x in b:
    d.append(x)
print(d)