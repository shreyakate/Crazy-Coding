import re
def ValidPalindrome(s):
	if not s :return False
	s = re.sub(r'[^a-zA-Z0-9]', '',s).lower()
	print s
	l, r = 0, len(s)-1
	while l<r:
		if s[l]==s[r]:
			l += 1
			r -= 1
		else:
			return False
	return True
print ValidPalindrome("A man, a plan, a canal: Panama")
print ValidPalindrome("race a car")
print ValidPalindrome("1234567777654321")

