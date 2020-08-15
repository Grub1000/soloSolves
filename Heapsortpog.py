# from heapq import _heapify_max
# L = [2,16,32,41,24,61,72,23,80,34,21,22,]
# def heapsort(L):
#     if L[0] <= L[0:len(L)]:
#         return 0
#     if L[0] >= 0:
#         L[0], L[len(L)] = L[len(L)], L[0]
#         if L[0] < L[1]

from heapq import _heapify_max, _heappop_max

L = [2,16,32,41,24,61,72,23,80,34,21,22]


_heapify_max(L)
print(L)


for i in range(3):
    print(L[0])
    _heappop_max(L)








