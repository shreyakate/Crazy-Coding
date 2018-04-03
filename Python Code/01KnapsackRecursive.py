
def KnapsackRecursive01(values, weights, W, n):
	if n ==0 or W==0:
		return 0
	elif weights[n-1] > W :
		return KnapsackRecursive01(values, weights, W, n-1)
	else: 
		return max(values[n-1]+KnapsackRecursive01(values, weights, W-weights[n-1], n-1) , 
			KnapsackRecursive01(values, weights, W, n-1))

def KnapsackDP01(values, weights, W, n):
	K = [[0 for x in range(W+1)] for x in range(n+1)]
	for i in range(n+1):
		for w in range(W+1):
			if i == 0 or w ==0 :
				K[i][w] = 0
			elif weights[i-1]<=w:
				K[i][w] = max(values[i-1] + K[i-1][w-weights[i-1]], K[i-1][w])
			else:
				K[i][w] = K[i-1][w]
	return K[n][W]

print KnapsackRecursive01([60,100,120],[1,2,3],5,3)
print KnapsackDP01([60,100,120],[1,2,3],5,3)