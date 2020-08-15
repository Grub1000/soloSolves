import numpy
x = int(input())
L1 = []
for i in range(x):
    templist = list(map(float, input().split()))
    L1.append(templist)
answer = numpy.linalg.det(L1)
print(round(answer, 2))