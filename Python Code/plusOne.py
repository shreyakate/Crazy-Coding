def plusOne(digits):
	carry = 1
	i = len(digits)-1
	while i >=0:
		digits[i], carry = (digits[i]+carry)%10  , (digits[i]+carry)/10
		i -= 1
	if carry>0:
		digits.insert(0,carry)
	return digits


print plusOne([9,9,9])