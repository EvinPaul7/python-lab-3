n=int(input("Enter the number of last lines needed to be print: "))
a=open("testfile.txt","r")
for x in (a.readlines()[-n:]):   
    print(x)