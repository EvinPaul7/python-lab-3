a=open("testfile.txt","r")
b=a.readlines()
for x in b:
    c=x.splitlines()
    print(c)
