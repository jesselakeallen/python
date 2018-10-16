def find_last(target, search):
    result = target.rfind(search)
    return result

def find_last2(s, t):
    last_pos = -1
    while True:
	pos = s.find(t, last_pos + 1)
	if pos == -1:
		return last_pos
	last_pos = pos

print find_last('aaaa', 'a')
print find_last2('aaaa', 'a')
