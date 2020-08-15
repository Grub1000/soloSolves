from itertools import product
N = list(map(int,input().split()))
M = list(map(int,input().split()))
T = (list(product(N,M)))
for i in T:
    print(i, end= ' ')