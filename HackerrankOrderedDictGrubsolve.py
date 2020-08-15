from collections import OrderedDict
N = int(input())
d = OrderedDict()
for i in range(N):
    x, y, z = input().rpartition(' ')
    d[x] = d.get(x, 0) + int(z)
for key, value in d.items():
    print(key, value)