def countdown(n):
    while n > 0:
	print n
	n = n - 1
    	if n == 0:
		print 'Blastoff!'

# example
def countdown2(n):
    while n > 0:
        print n
        n = n - 1
    print 'Blastoff!'

countdown(5)
countdown2(4)
