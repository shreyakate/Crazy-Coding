def plusOne(digits):
	carry = 1
	i = len(digits)-1
	while i >=0 and carry:
		digits[i], carry = (digits[i]+carry)%10  , (digits[i]+carry)/10
		i -= 1
	if carry:
		digits.insert(0,carry)
	return digits

print plusOne([9,9,9])
print plusOne([1,0,0])