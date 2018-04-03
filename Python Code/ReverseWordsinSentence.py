def ReverseWordsinSentence(sentence):
	words = sentence.split()
	res = ''.join(word + ' ' for word in reversed(words))
	return res

print ReverseWordsinSentence("I am shreya Kate")