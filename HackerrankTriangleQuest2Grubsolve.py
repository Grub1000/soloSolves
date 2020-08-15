Num = int(input())
L = []
for i in range(1, Num + 1):
    L.append(str(i))
for i in range(1, Num + 1):
    L2 = L[::-1]
    print(''.join(L[0:i-1]) + ''.join(L2[(Num-i):Num]))




# for i in range(1,int(input())+1):
#     print((round(10**i/9))**2)