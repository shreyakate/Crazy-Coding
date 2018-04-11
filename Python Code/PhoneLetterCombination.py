def PhoneLetterCombination(num):
	n = str(num)
	d = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
	res = ['']
	temp =[]
	for i in n:
		for j in d[i]:
			for k in res:
				temp.append(k+j)
		res = temp
		temp =[]
	return res

print PhoneLetterCombination(23)