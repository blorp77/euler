def factors(n):
	return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def triangle(n):
	return (n*(n+1))/2
	
for i in range(1, 1000000):
	n = triangle(i)
	if len(factors(n)) > 500:
		print n
		break