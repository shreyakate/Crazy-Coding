from collections import defaultdict
file = open('testfile.txt','w') 

file.write("Shreya Kate\n") 
file.write("Anil Joshi\n") 
file.write("Vaibhav Bhalerao\n") 
file.write("Shrikant Joshi\n") 
file.write("Shrikant Joshi\n") 
file.close() 

file = open('testfile.txt','r')
d = defaultdict()
top = 0
surname = ''
contents = file.readlines()  
for i in contents:
	x = i.split()
	d[x[1]] = d.get(x[1],0)+1
	if d[x[1]] > top:
		top = d[x[1]]
		surname = x[1]
print surname

