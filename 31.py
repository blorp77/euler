coins = [200, 100, 50, 20, 10, 5, 2, 1]

no_iter = 0

def iterate(n):
	global no_iter
	if n == 200:
		no_iter += 1
		return
	for i in coins:
		if i <= (200-n):
			iterate(n + i)

iterate(0)
print no_iter