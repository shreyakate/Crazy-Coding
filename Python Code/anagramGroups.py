from collections import defaultdict
def anagramGroups(arr):
	d = defaultdict()
	for i in arr:
		a = tuple(sorted(i))  
		# print a
		d[a] = d.get(a,[])+[i]
	return d.values()

print anagramGroups(["eat", "tea", "tan", "ate", "nat", "bat"])

def GroupAnagram(words):
	d = defaultdict()
	for word in words:
		d[tuple(sorted(word))] = d.get(tuple(sorted(word)),[]) + [word]
	return d.values()

print GroupAnagram(["eat", "tea", "tan", "ate", "nat", "bat"])

def GrpAnagrams(words):
	asclist = map(chr, range(ord('a'), ord('z') + 1))   #O(n)
	primelist = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47,53,59,61,67,71,73,79,83,89,97,101]
	ascmap = dict(zip(asclist, primelist))        # O(n)
	ascmap = {'a': 2, 'c': 5, 'b': 3, 'e': 11, 'd': 7, 'g': 17, 'f': 13, 'i': 23, 'h': 19, 'k': 31, 'j': 29, 'm': 41, 'l': 37, 'o': 47, 
	'n': 43, 'q': 59, 'p': 53, 's': 67, 'r': 61, 'u': 73, 't': 71, 'w': 83, 'v': 79, 'y': 97, 'x': 89, 'z': 101} # T: O(n) S: O(n)
	res = defaultdict() 
	for word in words:   #O(mk)...where m in number of works int the list and k is max len of string
		val = 1
		for c in word: 
			val *= ascmap[c]
		res[val] = res.get(val,[]) +[word]       # T(nk) S: O(n)
	return sorted(res.values())     #sort might not be necessary

print GrpAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])


