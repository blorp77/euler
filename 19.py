n=0
days = 1 #divisible by 7 = sunday
for year in range(1900, 2001):
	for month in range (1, 13):
		if month in [4, 6, 9, 11]: #30 days
			days += 30
		elif month == 2:
			if year%4==0 and (year%100!=0 or year%400==0): #leap year
				days += 29
			else: #regular year
				days += 28
		else: #31 days
			days += 31
		if year >= 1901 and days%7==0:
			n+=1
print n