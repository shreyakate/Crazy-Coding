def DivisibleBy9(n):
	while n>10:
		num = str(n)
		n = sum([int(ch) for ch in num])
	return n == 9

def DivisibleBy11(n):
	num = str(n)[::-1]
	sign , val = 1, 0
	multiples = [0,11,22,33,44,55,66,77,88,99]
	for ch in num:
		val += int(ch) * sign
		sign *= -1
	return val in multiples

print DivisibleBy9(273456783)
print DivisibleBy11(1080706)
