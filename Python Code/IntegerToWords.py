def IntegerToWords(num):
	if num == 0: 
		return 'Zero'

	digits =['','One ','Two ','Three ','Four ','Five ','Six ','Seven ','Eight ', 'Nine ']
	teens = ['Ten ', 'Eleven ', 'Twelve ', 'Thirteen ', 'Fourteen ', 'Fifteen ', 'Sixteen ', 'Seventeen ', 'Eighteen ','Nineteen ']
	tens = ['', '', 'Twenty ', 'Thirty ', 'Forty ', 'Fifty ', 'Sixty ', 'Seventy ', 'Eighty ', 'Ninety ']
	others = ['', 'Thousand ', 'Million ', 'Billion ']
	
	res =''
	x = str(num)
	if len(x)%3 == 1: x ='00'+ x
	elif len(x)%3 == 2: x = '0'+ x
	nums = [x[i:i+3] for i in range(0,len(x),3)][::-1]
	for i in range(len(nums)):
		if nums[i].count('0')==3:
			continue
		res = others[i] + res
		if nums[i][1]=='1':
			res = teens[int(nums[i][2])] + res
		else:
			res = digits[int(nums[i][2])] + res
			res = tens[int(nums[i][1])] + res
		if nums[i][0]>'0':
			res = digits[int(nums[i][0])] + 'Hundred '+ res
	return res.rstrip()

def numberToWords(num):
	if num == 0: 
		return 'Zero'

	digits =['','One ','Two ','Three ','Four ','Five ','Six ','Seven ','Eight ', 'Nine ']
	teens = ['Ten ', 'Eleven ', 'Twelve ', 'Thirteen ', 'Fourteen ', 'Fifteen ', 'Sixteen ', 'Seventeen ', 'Eighteen ','Nineteen ']
	tens = ['', '', 'Twenty ', 'Thirty ', 'Forty ', 'Fifty ', 'Sixty ', 'Seventy ', 'Eighty ', 'Ninety ']
	others = ['', 'Thousand ', 'Million ', 'Billion ']

	
	def helper(num):
		if num == 0 : return ''
		elif num<10: return digits[num]
		elif 9<num<20: return teens[num-10]
		elif num < 100:
			return tens[num/10] + helper(num%10)
		else:
			return digits[num/100] + 'Hundred '+ helper(num%100)

	res = ''
	i = 0
	while num > 0:
		if num%1000 !=0:
			res = helper(num%1000) + others[i] + res
		num /= 1000
		i += 1
	return res.strip()

print IntegerToWords(12345619)
print numberToWords(12345619)



##Extra solution without any function calls

# oneWordInt = "Zero One Two Three Four Five Six Seven Eight Nine Ten \
#                Eleven Twelve Thirteen Fourteen Fifteen Sixteen Seventeen Eighteen Nineteen".split()
#         tens = "Twenty Thirty Forty Fifty Sixty Seventy Eighty Ninety".split()
#         hundred = "Hundred"
#         largeNumbers = "Thousand Million Billion".split()
        
#         words, digits = [], 0
#         while num:
#             currNum, num = num % 1000, num / 1000
#             word = ''
#             if currNum > 99:
#                 word += oneWordInt[currNum / 100] + ' ' + hundred + ' '
#                 currNum %= 100
#             if currNum > 19:
#                 word += tens[currNum / 10 - 2] + ' '
#                 currNum %= 10
#             if currNum > 0:
#                 word += oneWordInt[currNum] + ' '
#             word = word.strip()
#             if word:
#                 word += ' ' + largeNumbers[digits - 1] if digits else ''
#                 words += [word]
#             digits += 1
#         return ' '.join(words[::-1]) or 'Zero'