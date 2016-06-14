import itertools

a = ['a', 'b', 'c']
b = itertools.permutations(a, 2)

for i in b:
    print i

