def ValidNumber(s):
	state = [ {},{'blank':1, 'sign':2, 'digit':3, '.': 4},
			   {'digit':3, '.': 4},
			   {'digit':3,'.':5,'e':6,'blank':9},
			   {'digit': 5},
			   {'digit':5,'e':6,'blank':9},
			   {'sign':7,'digit':8},
			   {'digit':8},
			   {'digit':8, 'blank':9},
			   {'blank':9}]
	currState = 1
	for ch in s:
		if '0'<=ch <='9':
			ch = 'digit'
		if ch == ' ':
			ch = 'blank'
		if ch in ['+','-']:
			ch = 'sign'
		if ch not in state[currState].keys():
			return False
		currState = state[currState][ch]
	if currState not in [3,5,8,9]:
		return False
	return True

print ValidNumber("0")
print ValidNumber("   ")
print ValidNumber(" 00011")
print ValidNumber(" +123e-12")
print ValidNumber(" -123")
print ValidNumber("123")
print ValidNumber("abc")
print ValidNumber(" 01e")
print ValidNumber("2e10 ")
print ValidNumber("1  a")
print ValidNumber(" 01.")
print ValidNumber(".12e+123")
print ValidNumber("  .")
print ValidNumber("2e0")
print ValidNumber("0e")
print ValidNumber("..2")
print  ValidNumber("0..")





