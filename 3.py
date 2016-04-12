def factors(n):
	return sorted(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))), reverse=True)
n = 600851475143 
for a in factors(n):
	print a, len(factors(a))
	if len(factors(a))<=2:
		print a
		break
else:
	print "No prime factors"