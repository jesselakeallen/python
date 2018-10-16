def set_range(a,b,c):
    # Your code here
    big = max(a,b,c)
    small = min(a,b,c)
    range = big - small
    return range

print set_range(10, 4, 7)
#>>> 6  # since 10 - 4 = 6

print set_range(1.1, 7.4, 18.7)
#>>> 17.6 # since 18.7 - 1.1 = 17.6
