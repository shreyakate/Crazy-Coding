def EgyptianFraction(nr, dr):
	if nr==0 or dr ==0: 
		return
	if dr%nr==0:
		print "1/" + str(dr/nr)
		return
	if nr%dr == 0:
		print str(nr/dr)
		return
	if nr > dr :
		print str(nr/dr) + " + ",
		EgyptianFraction(nr%dr,dr)
		return 
	q = dr/nr + 1
	print "1/"+str(q)+" + ",
	EgyptianFraction(nr*q - dr, dr*q)

EgyptianFraction(123,135)
