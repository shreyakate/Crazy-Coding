def Stocks1(prices):
	if not prices: return 0
	buy = prices[0]
	profit = 0
	for i in xrange(1,len(prices)):
		buy = min(buy, prices[i])
		tmp = prices[i] - buy
		profit = max(tmp,profit)
	return profit


def Stocks1a(prices):
	if not prices : return 0
	maxCurr = maxSoFar = 0
	for i in range(1,len(prices)):
		maxCurr += (prices[i] - prices[i-1])
		maxCurr = max(0,maxCurr)
		maxSoFar = max(maxSoFar,maxCurr)
	return maxSoFar

print Stocks1([7, 1, 5, 3, 6, 4])
print Stocks1([7, 6, 4, 3, 1])
print Stocks1a([7, 1, 5, 3, 6, 4])
print Stocks1a([7, 6, 4, 3, 1])


