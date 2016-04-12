def factors(n):
	s = sorted(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))
	if len(s) > 1:
		return s[:-1]
	return s

def is_abundant(n):
	return (sum(factors(n)) > n)

abundant_list = []
for i in range(2, 28123):
	if is_abundant(i):
		abundant_list.append(i)
list_sums = []
for i in abundant_list:
	for j in abundant_list:
		list_sums.append(i+j)
list_sums = list(set(list_sums))
list_numbers = range(28123)

for i in list_sums:
	if i >= 28123:
		break
	list_numbers.remove(i)

print sum(list_numbers)
