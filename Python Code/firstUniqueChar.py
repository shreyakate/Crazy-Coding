from collections import OrderedDict
def firstUniqueChar(s):
	d = OrderedDict()
	for ch in s:
		d[ch] = d.get(ch,0) + 1
	for k,v in d.items():
		if v == 1:
			return k
	return ''

print firstUniqueChar("loveleetcode")
