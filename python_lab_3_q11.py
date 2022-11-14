import os
a=os.stat("testfile.txt")
print(a.st_size,"bytes")