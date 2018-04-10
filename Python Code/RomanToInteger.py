def RomanToInteger(s):
	conv = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000} 
	i = len(s)-1
	num = 0
	prev = 'I'
	while i>=0:
		if conv[prev]>conv[s[i]]:
			num -= conv[s[i]]
		else:
			num += conv[s[i]]
		prev = s[i]
		i -= 1
	print num

RomanToInteger('XXXIX')

 d = {'I':1, 'V':5, 'X':10,'L':50,'C':100,'D':500,'M':1000 }
        i =res = prev =0 
        while i<len(s):
            if s[i] in d:
                curr = d[s[i]]
                if prev < curr:
                    res += (curr - 2*prev) 
                else:
                    res += curr
                prev = curr
            i +=1
        return res
		


