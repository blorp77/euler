import itertools
list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
a=[]
for word in itertools.permutations( list ):
   a.append(int("".join(word)))
a= sorted(a)
print a[999999]