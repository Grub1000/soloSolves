N, X = map(int, input().split())
StarterList = []
FinalList = []
for i in range(X):
    V = input()
    V2 = map(float, V.split())
    FinalList.append(V2)
v = zip(*FinalList)
for i in v:
    print(sum(i)/float(X))
