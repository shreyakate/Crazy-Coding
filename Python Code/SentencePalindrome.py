import re
def SentencePalindrome(sentence):
	letters = re.sub(r'[^a-zA-Z]','',sentence).lower()
	l, r = 0, len(letters)-1
	while l<r:
		if letters[l] != letters[r]:
			print letters[l] ,letters[r]
			return False
		l +=1
		r -=1 
	return True

def SentencePalindrome1(sentence):
	l, r = 0, len(sentence)-1
	sentence = sentence.lower()
	while l<r:
		if ('a'<=sentence[l]<='z' and 'a'<=sentence[r]<='z' ):
			if sentence[l] == sentence[r]:
				l += 1
				r -= 1
			else:
				return False
		if not ('a'<=sentence[l]<='z'):
			l+=1
		if not ('a'<=sentence[r]<='z'):
			r -= 1
	return True

print SentencePalindrome("Too hot to hoot.")
print SentencePalindrome1("Too hot to hoot.")