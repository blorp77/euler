list = []
for a in range(2, 101):
	for b in range(2, 101):
		c = a**b
		if c not in list:
			list.append(c)
print len(list)