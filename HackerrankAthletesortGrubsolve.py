a, b = input().split()
Lmain = []
for i in range(int(a)):
    L1 = list(map(int, input().split()))
    Lmain.append(L1)
k = int(input())
def sort(Lmain):
    return sorted(Lmain, key= lambda x: x[k])
L2 = sort(Lmain)
for i in L2:
    print(*i)