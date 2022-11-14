
a=open("testfile.txt","r")
b=dict()
for x in a:
    words=x.split()
    print (words)
    for y in words:
        if y in b:
            b[y]=b[y]+1
        else:
            b[y]=1         
print(b) 