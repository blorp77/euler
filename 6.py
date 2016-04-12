def sum_of_square(n):
	total = 0
	for i in range(n+1):
		total += (i**2)
	return total
	
def square_of_sum(n):
	return (n*(n+1)/2)**2
	
print square_of_sum(100) - sum_of_square(100)