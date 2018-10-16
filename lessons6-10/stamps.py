def stamps(n):
    # Your code here
    p5 = n / 5
    p2 = (n - p5 * 5) / 2 
    p1 = (n - p5 * 5 - p2 * 2)
    return p5, p2, p1

print stamps(8)
print stamps(5)
print stamps(29)
