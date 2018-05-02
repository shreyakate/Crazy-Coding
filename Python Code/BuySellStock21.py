def BuySellStock21(prices):
	profit = 0
	n =len(prices)
	for i in range(1,n):
		if prices[i] > prices[i-1]:

			profit += prices[i] - prices[i-1]
			print  prices[i], prices[i-1], profit
	return profit 

print BuySellStock21([7,1,5,3,6,4])
print BuySellStock21([1,2,3,4,5])
print BuySellStock21([7,6,4,3,1])