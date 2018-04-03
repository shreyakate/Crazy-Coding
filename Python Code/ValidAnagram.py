def Divisibleby9(s):
	while s>10:
		num = str(s)
		s = sum([int(ch) for ch in num])
	return s == 9

print Divisibleby9(273456783)


