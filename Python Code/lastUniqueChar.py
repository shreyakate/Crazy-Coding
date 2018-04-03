from collections import OrderedDict
def lastUniqueChar(s):
	d = OrderedDict()
	for i in s:
		d[i] = d.get(i,0)+1

	for k,v in reversed(d.items()):
		if v == 1:
			return k

print lastUniqueChar("asdfghsdfg")
