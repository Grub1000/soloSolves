L = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 34, 43, 53, 71, 73, 81, 95]
# k = int(input())
n = len(L)
def binarysearch(L,n,k):
    l = 1

    h = n
    while(l <= h):
        mid = (l+h)//2
        if k == L[mid]:
            return mid
        if k < L[mid]:
            h = mid - 1
        else:
            l = mid + 1
    return 0

print(binarysearch(L,n,71))
