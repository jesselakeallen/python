def bigger(a, b):
    if a > b:
       return a
    else:
       return b

def biggest(a, b, c):
    return bigger(bigger(a,b), c)

print biggest(1,2,3)
print max(1,2,3)
