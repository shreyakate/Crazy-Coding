def addBinaryStrings(num1,num2):
	if not num1 and not num2: return 0
	if not num1 and num2: return num2
	if not num2 and num1: return num1

	x,y = len(num1)-1, len(num2)-1
	res, carry ='', 0

	while x>=0 or y>=0:
		if x>=0 and y>=0:
			res = str((int(num1[x]) + int(num2[y]) + carry)%2) + res
			carry = (int(num1[x]) + int(num2[y]) + carry)//2
			x -= 1
			y -= 1
		elif x>=0:
			res = str((int(num1[x]) + carry)%2) + res
			carry = (int(num1[x]) + carry)//2
			x -= 1
		elif y>=0:
			res = str((int(num2[y]) + carry)%2) + res
			carry = (int(num2[y]) + carry)//2
			y -= 1

	if carry:
		res = str(carry)+res
	return res

print addBinaryStrings('100','111')
