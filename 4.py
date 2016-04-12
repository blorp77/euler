def is_palindrome(n):
	s=str(n)
	l=int(len(s)/2)
	resp = True
	for i in range(l):
		resp = resp and (s[i] == s[-(i+1)])
	return resp
l = []
for i in range(1000, 900, -1):
	for j in range(1000, 900, -1):
		if is_palindrome(i*j):
			l.append(i*j)
print max(l)