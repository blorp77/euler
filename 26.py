def size_of_recurring_cycle(denum):
	num = 1
	left = []
	while True:
		number_zeros_added = 0
		if num == 0:
			return 0
		while num < denum:
			number_zeros_added +=1
			num *= 10
		if num == denum:
			return 0
		
		num = num%denum
		if num in left: #you have repetition
			#print left
			return len(left[left.index(num):]) + (number_zeros_added-1)
		left.append(num)

value = 0
max = 0

for i in range(2, 1000):
	n = size_of_recurring_cycle(i)
	#print i, n
	if n > max:
		max = n
		value = i

print value ,max