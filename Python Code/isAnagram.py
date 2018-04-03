def isAnagram(s,t):
	if len(s) != len(t): return False
	if len(set(s)) != len(set(t)): return False
	s = sorted(s)
	t=sorted(t)
	for i in range(len(s)):
		if s[i]!=t[i] : return False
	return True

print isAnagram('anagram','nagaram')
print isAnagram('rat','car')