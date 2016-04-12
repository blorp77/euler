n = 1000
for a in range(1, n+1):
	for b in range(a+1, n-(a+1)):
		c = n - (a+b)
		if c > b and b > a:
			if (a+b+c) == n and (a**2+b**2)==c**2:
				print a, b, c
				print a*b*c
