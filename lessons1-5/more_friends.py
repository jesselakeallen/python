def is_friend(name):
    if name[0] == 'D':
	return True
    if name[0] == 'N':
       	return True
    else:
	return False

print is_friend('Dave')
print is_friend('Ned')
print is_friend('Jake')

# def is_friend(name):
#     return name[0] == 'D' or name[0] == 'N'
