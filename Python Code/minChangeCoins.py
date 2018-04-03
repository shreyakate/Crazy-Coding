def minChangeCoins(n):
	change = [1,0.50,0.25,0.1,0.05,0.01]
	i = 0
	coins = [0]*len(change)
	while n and i<len(change):
		if n> change[i]:
			n -= change[i]
			coins[i] += 1
		else:
			i += 1
	return coins 

print minChangeCoins(1.33)



