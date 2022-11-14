a=open("testfile.txt","r")
print(a.read())
b=""
for x in a:
    b=b+x
print(b)
