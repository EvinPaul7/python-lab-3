import random

a=open("testfile.txt","r")
b=a.readlines()
c=random.randint(0,len(b)-1)
print(b[c])



