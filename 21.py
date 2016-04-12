def factors(n):
	s = sorted(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))
	if len(s) > 1:
		return s[:-1]
	return s

def is_amiable(n):
	s = sum(factors(n))
	return n == sum(factors(s)) and n != s

amiable_list = []
for i in range(2, 10000):
	if is_amiable(i):
		amiable_list.append(i)
print sum(amiable_list)
