a, b, n = 1, 1, 2
while len(str(b)) < 1000: a, b, n = b, a+b, n+1
print n