l = []
for n in range(10, 1000000):
	total=0
	for s in list(str(n)):
		total += int(s)**5
	if n == total:
		l.append(n)

print l
print sum(l)