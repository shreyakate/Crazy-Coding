def isPowerOfTwo(n):
	# print bin(n)
	return bin(n).count('1') == 1

print isPowerOfTwo(-16)

def isPowerOfThree(n):
	return n>0  and 1162261467%n == 0

print isPowerOfThree(9)

def isPowerOfFour(n):

	return n>0 and bin(n).count('1') == 1 and 1431655765&n == n


print isPowerOfFour(64)

