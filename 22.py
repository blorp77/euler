def num_value(s):
	alphabet = list("abcdefghijklmnopqrstuvwxyz")
	total = 0
	for i in list(s.lower()):
		total += alphabet.index(i)+1
	return total

f = open('p022_names.txt', 'r')
a = sorted(f.read().replace("\"", "").split(","))

pos = 1
total = 0
for name in a:
	total += num_value(name) * pos
	pos+=1
print total