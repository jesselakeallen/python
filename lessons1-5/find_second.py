def find_second(search, target):
    first = search.find(target)
    second = search.find(target, first + len(target)) # they used + 1
    return second

danton = "De l'audace, encore de l'audace, toujours de l'audace"
print find_second(danton, 'audace')

twister = "she sells seashells by the seashore"
print find_second(twister,'she')
