import itertools
x, y = input().split(' ')
L = []
for i in x:
    L.append(i)
L2 = sorted(L)
L3 = list(itertools.permutations(L2,int(y)))
for i in range(len(L3)):
    print(''.join(L3[i]))
