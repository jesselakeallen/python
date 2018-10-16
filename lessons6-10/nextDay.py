def nextDay(year, month, day):
    if month == 12 and day == 30:
        year += 1
        month = 1
        day = 1
    elif day == 30:
        day = 1
        month += 1
    else:
        day += 1
    return year, month, day

print nextDay(1999,12,30)
