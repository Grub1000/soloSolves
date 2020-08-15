from collections import Counter
N = int(input())
L = list(map(int,input().split(' ')))
C = int(input())
l = []
D = Counter(L)
for i in range(C):
    Shoe, Given = list(map(int,input().split(' ')))
    l.append([Shoe, Given])
Total = 0
for i in range(len(l)):
    if D[l[i][0]] > 0:
        D[l[i][0]] = (D[l[i][0]]) - 1
        Total = Total + l[i][1]
print(Total)
