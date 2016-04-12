def lattice(n):
	a = []
	for i in range(n+1):
		b = []
		for j in range(n+1):
			if i == 0 or j == 0 :
				b.append(1)
			else:
				b.append(a[i-1][j] + b[-1])
		a.append(b)
	return a
	
print lattice(20)[-1][-1]

				