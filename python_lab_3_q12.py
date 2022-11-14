numbers=[1,2,3,4,5,6,7,8,9,10]
print(numbers)
a=open("numbers.txt","w")
for x in numbers:
    a.write("%s\n" %x)
print(a)


