# from heapq import merge
# #
# # seq1 = [1, 3, 5, 7, 9, 11]
# # seq2 = [2, 4, 6, 8, 10, 12]
# # # n = len(seq1)
# # # m = len(seq2)
# # # c = [0 for i in range(m + n)]
# # #
# # # def merging(seq1, seq2, c, m, n):
# # #     i = 0
# # #     j = 0
# # #     k = 0
# # #     while(i <= n and j <= m):
# # #         if seq1[i] < seq2[j]:
# # #             c[k] = seq1[i]
# # #             i = i + 1
# # #             k = k + 1
# # #         else:
# # #             c[k] = seq2[j]
# # #             j = j + 1
# # #             k = k + 1
# # #     for x in seq1[i:n]:
# # #         c[k] = seq1[x]
# # #         k = k + 1
# # #     for y in seq2[j:m]:
# # #         c[k] = seq2[y]
# # #         k = k + 1
# # #
# # # merging(seq1, seq2, c, m, n)
# #
# # #____________________________________
# # result = list(merge(seq1, seq2))
# # result2 = sorted(seq1 + seq2)

def merge(arr1, arr2):
    i = 0
    j = 0
    len1 = len(arr1)
    len2 = len(arr2)
    arr = []
    while i < len1 and j < len2:
        if arr1[i] < arr2[j]:
            arr.append(arr1[i])
            i = i + 1
        else:
            arr.append(arr2[j])
            j = j + 1
    while(i < len1):
        arr.append(arr1[i])
        i = i + 1
    while(j < len2):
        arr.append(arr2[j])
        j = j + 1


    return arr



arr1 = [1,4,9,10]
arr2 = [2,3,6,7,8]
arr = merge(arr1,arr2)

# num = 1234
# res = [int(x) for x in str(num)]
# print(res)
print(arr)


