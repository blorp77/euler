n = 1
for i in range(2, 101):
	n *= i
sum=0
print n
while n:
	sum += n%10
	n /= 10
print sum