def BuySellStock2(prices, fee):
	b, s = 0,1
	buy, sell = prices[b], prices[s]
	while b < len(prices):
		
		while s < len(prices):
			sell = prices[s]
			if sell - buy - fee > 0:
				profit += sell - buy - fee
				b = s+1
				s = b+1



print BuySellStock1([7,1,3,5,9,1,3])