const = 1.0
L = []
for i in range(100):
    if i % 2 == 0:
        L.append(i)
L2 = []
L3 = []
for j in range(len(L)):
    if j % 2 == 0:
        L2.append(L[j])
    else:
        L3.append(L[j])
def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)
L2.pop(0)
def cos(x):
    count = 0
    countNegative = 0
    countPositive = 0
    for k in L2:
        countPositive = countPositive + (x ** k)/(factorial(k))
    for l in L3:
        countNegative = countNegative + (x ** l) / (factorial(l))
    # print(countNegative)
    hardpart = countPositive - countNegative
    print(const + hardpart)
    print(len(L2))
    print(len(L3))
test = float(input())
cos(test)
