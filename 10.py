def factors(n):
	return sorted(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))

sum = 0
for i in range(2,2000001):
	if len(factors(i)) <= 2:
		sum += i
print sum