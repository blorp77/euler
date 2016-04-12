def factors(n):
	return sorted(set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0))))
print factors(12)

max = 20
answer = 1
prime = []
comp = []
for i in range(1, max+1):
	if len(factors(i)) > 2:
		comp.append(i)
	else:
		prime.append(i)

for j in prime:
	answer *= j
	
for k in comp:
	if answer%k != 0 :
		for l in factors(k):
			if (answer*l)%k == 0:
				answer *= l
				break
		
		
print answer