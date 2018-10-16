dim = [31,28,31,30,31,30,31,31,30,31,30,31]

def dateRange(y1,m1,d1,y2,m2,d2):
    yearDiff = y2 - y1
    days = yearDiff * 365
    print days
    monthDiff = sum(dim[m1-1:m2-1])
    print monthDiff
    dayDiff = d2 - d1
    print dayDiff
    days = days + monthDiff + dayDiff
    print days

dateRange(2011,1,1,2012,8,8)
dateRange(2011,8,8,2012,1,1)
