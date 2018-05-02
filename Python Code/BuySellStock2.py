def BuySellStock2(prices, fee):
	profit = 0
	buy = prices[0]
	for p in prices:
		if buy > p:
			buy = p
		else:
			tmp = p - buy - fee
			if tmp > 0:
				profit += tmp 
				buy = p - fee
	return profit 
	


print BuySellStock2([7,1,3,5,9,1,3],2)
print BuySellStock2([1, 3, 2, 8, 4, 9],2)