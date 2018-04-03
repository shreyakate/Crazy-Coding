from collections import OrderedDict

def DictTrial(arr):
	d = OrderedDict()
	for i in arr:
		d[i] = d.get(i,0) + 1
	return d

print DictTrial([1,4,2,46,7,8,9,91,3,4,5,51,1,1,1,3]) 