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


def excelNumberToTitle(n):
	if not n : return ''
        res = ''
        while n:
            if n%26:
                res = chr((n%26) + 64) + res
                n = n//26
            else:
                res = chr(90) + res
                n = (n//26) -1
            
        return res

print excelNumberToTitle(18306)
print excelNumberToTitle(12345)
print excelNumberToTitle(26)
