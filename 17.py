def number_to_text(n):
	if len(str(n)) == 1:
		if n == 1:
			return "one"
		elif n == 2:
			return "two"
		elif n == 3:
			return "three"
		elif n == 4:
			return "four"
		elif n == 5:
			return "five"
		elif n == 6:
			return "six"
		elif n == 7:
			return "seven"
		elif n == 8:
			return "eight"
		elif n == 9:
			return "nine"
		else:
			return ""	
	elif len(str(n)) == 2:
		if n == 10:
			return "ten"
		elif n == 11:
			return "eleven"
		elif n == 12:
			return "twelve"
		elif n == 13:
			return "thirteen"
		elif n == 14:
			return "fourteen"
		elif n == 15:
			return "fifteen"
		elif n == 16:
			return "sixteen"
		elif n == 17:
			return "seventeen"
		elif n == 18:
			return "eighteen"
		elif n == 19:
			return "nineteen"
		else:
			n1 = number_to_text(int(str(n)[-1]))
			if int(str(n)[0]) == 2:
				n10 = "twenty"
			elif int(str(n)[0]) == 3:
				n10 = "thirty"
			elif int(str(n)[0]) == 4:
				n10 = "forty"
			elif int(str(n)[0]) == 5:
				n10 = "fifty"
			elif int(str(n)[0]) == 6:
				n10 = "sixty"
			elif int(str(n)[0]) == 7:
				n10 = "seventy"
			elif int(str(n)[0]) == 8:
				n10 = "eighty"
			elif int(str(n)[0]) == 9:
				n10 = "ninety"
			if n1 != "":
				return n10 + "-" + n1
			return n10
	elif len(str(n)) == 3:
		n100 = number_to_text(int(str(n)[0]))
		n10 = number_to_text(int(str(n)[1:]))
		if n10 != "":
			return n100 + " hundred and " + n10
		return n100 + " hundred"
	elif n == 1000:
		return "one thousand"
	else:
		return ""

a = []

for i in range (1, 1001):
	a.append(number_to_text(i))
print len("".join(a).replace(" ", "").replace("-", ""))
"""
for i in range (1, 1001):
	n = number_to_text(i)
print len(n.replace(" ", "").replace("-", "")) ,n
"""