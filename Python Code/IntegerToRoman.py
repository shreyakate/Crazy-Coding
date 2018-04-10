def IntegerToRoman(num):
	r = ['M','MC','D','DC','C','XC','L','XL','X','IX','V','IV','I']
	n = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
	i = 0
	res =''
	while num>0:
		if num>=n[i]:
			num -= n[i]
			res += r[i]
		else:
			i += 1

	return res

print IntegerToRoman(75)


