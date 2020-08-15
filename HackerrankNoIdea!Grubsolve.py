from timeit import timeit
a, b = input().split()
L = map(int, input().split())
Lhappy = set(map(int, input().split()))
Lnothappy = set(map(int, input().split()))
count = 0
for i in L:
    if i in Lhappy:
        count += 1
    elif i in Lnothappy:
        count -= 1
    else:
        continue
print(count)
print(timeit())