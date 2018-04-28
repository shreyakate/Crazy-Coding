def singleNumber(nums):
	x = 0
	for i in nums:
		x ^= i
	return x

print singleNumber([2,2,1])
print singleNumber([4,1,2,1,2])

def singleNumber2(nums):
	return (3*sum(set(nums)) - sum(nums))//2

print singleNumber2([2,2,3,2])
print singleNumber2([0,1,0,1,0,1,99])


def singleNumber3(nums):
	mask = 0
	for x in nums:
		mask ^= x  # repeated numebers neutralize each other
		# print mask , x	

	# We need only one of this bits, for example the last:
	pivot_bit = mask & -mask
	# print pivot_bit
					
	# Having a and b a different value of pivot_bit we can
	# repeat the game on 2 virtual partitions:
	a, b = 0, 0
	for x in nums:
		if x & pivot_bit:
			a ^= x  # repeated numebers neutralize each other
		else:
			b ^= x  # repeated numebers neutralize each other
					
	return [a, b]

print singleNumber3([1, 7, 1, 2, 7, 5])