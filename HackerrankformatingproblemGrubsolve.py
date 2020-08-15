n = int(input())
L = len(bin(n)[2:])
for i in range(1,n + 1):
    print(str(i).rjust(L," ") + oct(i)[2:].rjust(L+1," ") + hex(i)[2:].upper().rjust(L+1," ") + bin(i)[2:].rjust(L+1," "))
