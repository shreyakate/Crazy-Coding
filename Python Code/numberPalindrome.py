def numberPalindrome(n):
	s = str(n)
	l , r = 0, len(s)-1
	while l<r:
		if s[l]!=s[r]:
			return False
		l += 1
		r -= 1
	return True

print numberPalindrome(1234321)