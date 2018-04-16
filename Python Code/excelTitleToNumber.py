def excelTitleToNumber(s):
	if not s: return 0
	i = num = 0
	n = len(s) -1
	while i<=n:
		x = (ord(s[i]) - 64) 
		num += (26**(n-i)) * x
		i += 1
	return num

print excelTitleToNumber('AABB')
print excelTitleToNumber('AUL')


def excelNumberToTitle(num):
	if not num : return ''
	res = ''
	while num:
		ch = chr((num%26) + 64)
		res = ch + res
		num = num//26

	return res
print excelNumberToTitle(18306)
print excelNumberToTitle(12345)