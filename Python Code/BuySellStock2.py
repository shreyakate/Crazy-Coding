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
	
	buy = prices[0]
        tmp1, tmp2 = 0,0
        n = len(prices)
        for i in range(1,n):
            if prices[i] < buy:
                buy = prices[i]
            else:
                sell = prices[i]
                prof = max(sell - buy,0)
                if prof == tmp1:
                    tmp1 = tmp2 = prof
                elif prof > tmp1:
                    tmp2 = tmp1
                    tmp1 = prof
                elif prof > tmp2:
                    tmp2 = prof
                prof = 0
                buy = prices[i]
        
        return tmp1+tmp2


print BuySellStock2([7,1,3,5,9,1,3],2)
print BuySellStock2([1, 3, 2, 8, 4, 9],2)