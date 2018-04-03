from collections import defaultdict
def anagramGroups(arr):
	d = defaultdict()
	for i in arr:
		a = tuple(sorted(i))
		print a
		d[a] = d.get(a,[])+[i]
	return d.values()

print anagramGroups(["eat", "tea", "tan", "ate", "nat", "bat"])





