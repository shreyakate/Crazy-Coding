def SqrtBinarySearch(low,high,x):
	if low>high: 
		return
	else:
		mid = low + (high-low)//2
		a = mid * mid 
		if a==x:
			return mid
		if a > x:
			if (mid-1) * (mid-1) < x:
				return mid-1
			else:
				return SqrtBinarySearch(low,mid-1,x)
		else:
			return SqrtBinarySearch(mid+1,high,x)

print SqrtBinarySearch(0,16,16)


