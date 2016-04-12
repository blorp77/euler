def make_chain(n): #n is the starting number
	chain = [n]
	while n != 1:
		if n%2 == 0:
			n = n/2
		else:
			n = 3*n+1
		chain.append(n)
	return chain
	
number = 0
max_n = 0
for i in range(2, 1000000):
	n = len(make_chain(i))
	if n > max_n:
		number = i
		max_n = n
print number, max_n