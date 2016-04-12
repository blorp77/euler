def factors(n):
	return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

nf = 0
for i in range(2, 100000000):
	if len(factors(i)) <= 2 :
		nf += 1
		if nf == 10001:
			print i
			break