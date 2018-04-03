def BuySellStock1(prices):
	buy = prices[0]
	profit = 0
	sell = b = s =0
	for i in range(1,len(prices)):
		if buy > prices[i]:
			buy = prices[i]
			sell = 0
			b = i
		else:
			sell = max(sell, prices[i])
			if profit < sell-buy:
				s = i
				profit = sell-buy
		
		#profit = max(profit,sell-buy)
	
	return [b,s,profit]

print BuySellStock1([7,1,3,5,9,1,3])