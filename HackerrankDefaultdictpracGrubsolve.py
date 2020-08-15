from collections import defaultdict
x, y = input().split()
d = defaultdict(list)
for i in range(int(x)):
    d[input()].append(str(i + 1))
for i in range(int(y)):
    b = input()
    if b in d:
        print(' '.join((d[b])))
    else:
        print('-1')
