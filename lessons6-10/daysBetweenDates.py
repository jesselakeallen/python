def nextDay(year, month, day):
    """Simple version: assume every month has 30 days"""
    if day < 30:
        return year, month, day + 1
    else:
        if month == 12:
            return year + 1, 1, 1
        else:
            return year, month + 1, 1

def daysBetweenDates(year1, month1, day1, year2, month2, day2):

    # YOUR CODE HERE!
    days = 0
#while dateIsBefore helper procedure
    while (year1, month1, day1) != (year2, month2, day2):
	year1, month1, day1 = nextDay(year1, month1, day1)
	days += 1
	#print days
    return days

print daysBetweenDates(2012,1,1,2013,1,1)
