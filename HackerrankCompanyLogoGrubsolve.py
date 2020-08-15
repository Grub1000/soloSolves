from collections import Counter, OrderedDict
L = []
for i in (Counter(sorted(input()))).items():
    L.append(i)
def sort(X):
   return sorted(X,key=lambda x: x[1], reverse=True)
B = sort(L)
for i in range(3):
     print(B[i][0] + ' ' + str(B[i][1]))
