def reverseBits(n):
	y = '0'*(32-len(bin(n)[2:])) + bin(n)[2:]
	return int(y[::-1],2)


print reverseBits(43261596)
print reverseBits(4326)