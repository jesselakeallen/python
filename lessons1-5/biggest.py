def biggest(a, b, c):
    if a > b:
	if a > c:
	    	return a
	else:
		return c
    else:
	if b > c:
		return b
	else:
		return c

print biggest(1,2,3)
print biggest(7,1,3)
print biggest(0,12,3)
