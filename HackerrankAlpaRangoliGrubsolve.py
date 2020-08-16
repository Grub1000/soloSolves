# RUN this code and enter any number :) -grub
Num = int(input())
L = []
for i in range(97,97+Num):
    L.append(chr(i))
for i in range(1,Num + 1):
    L2 = L[::-1]
    print("-".join((L2[0:i-1])+(L[(Num-i):Num])).center(((Num+Num-1)*2)-1, '-'))
for i in range(Num-1,0,-1):
    print("-".join((L2[0:i-1])+(L[(Num-i):Num])).center(((Num+Num-1)*2)-1, '-'))

