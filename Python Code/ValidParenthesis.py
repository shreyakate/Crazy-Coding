def ValidParenthesis(s):
	if len(s)%2 != 0: return False
	stack =[]
	for p in s:
		if p == '(' or p == '{' or p =='[':
			stack.append(p)
		elif p == ')':
			if stack :
				x =stack.pop()
				if x != '(': return False
		elif p == '}':
			if stack :
				x =stack.pop()
				if x != '{': return False
		elif p == ']':
			if stack :
				x =stack.pop()
				if x != '[': return False
	
	return len(stack)==0


print ValidParenthesis('()')