n=1
for i in range(3,1002,2):
	n += i**2
	n += i**2 - (i-1)
	n += i**2 - 2*(i-1)
	n += i**2 - 3*(i-1)
print n