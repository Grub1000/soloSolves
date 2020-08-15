L = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    L.append([name, score])
def sort(L):
    return(sorted(L,key=lambda x: x[1],))
k = sort(L)
k.append(['apple', float(10000000)])
k.append(['apple', float(10000000)])
output = []
T = True
while T:
    for i in range(0, len(k)-1):
        if float(k[i][1]) == float(k[i+1][1]) and float(k[i][1]) > float(k[0][1]):
            output.append(k[i])
        elif float(k[i][1]) == float(k[i-1][1]) and float(k[i][1]) > float(k[0][1]):
            output.append(k[i])
        elif float(k[i][1]) > float(k[0][1]) and float(k[i][1]) < float(k[i+1][1]) :
            output.append(k[i])
            break
    T = False
if output[-1][1] != output[0][1]:
    output.remove(output[-1])
output.sort()
answer = [print(output[x][0]) for x in range(len(output))]













