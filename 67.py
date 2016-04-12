import time

f = open('p067_triangle.txt', 'r')
a=[]
for line in f:
	a.append([int(num_string) for num_string in line.split(" ")])

for i in range(len(a)-2, -1, -1):
	for j in range(len(a[i])):
		left = a[i][j] + a[i+1][j]
		right = a[i][j] + a[i+1][j+1]
		if left > right:
			a[i][j] = left
		else:
			a[i][j] = right

print a[0][0]
