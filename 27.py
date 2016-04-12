def is_prime(n):
	if n < 2:
		return False
	return len(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))) <= 2

def find_number_of_primes(a, b):
	n=0
	while is_prime((n)**2 + n*a + b):
		n+=1
	return n

max = 0
max_mult = 0
for a in range(-999, 1000):
	for b in range(-999, 1000):
		n = find_number_of_primes(a, b)
		if n > max:
			max = n
			max_mult = a * b
print max_mult
