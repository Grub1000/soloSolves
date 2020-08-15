# I = str(input())
# IL = len(I)
# VWL = 'AEIOU'
# count1 = 0
# for i in range(len(I)):
#     if I[i] in VWL:
#         for j in range(i,IL):
#             # print(I[i:j + 1])
#             count1 = count1 + 1
# count2 = 0
# # print("#____________________________________________________#")
# for i in range(IL):
#     if I[i] not in VWL:
#         for j in range(i,IL):
#             # print(I[i:j+1])
#             count2 = count2 + 1
#
# if count1 > count2:
#     print("Kevin " + str(count1))
# elif count2 > count1:
#     print("Stuart " + str(count2))
# else:
#     print("Draw")
# __________________________________________
# # This is the optimized version of the code above;
# s = str(input())
#
# vowels = 'AEIOU'
#
# kevsc = 0
# stusc = 0
# for i in range(len(s)):
#     if s[i] in vowels:
#         kevsc += (len(s)-i)
#     else:
#         stusc += (len(s)-i)
#
# if kevsc > stusc:
#     print("Kevin", kevsc)
# elif kevsc < stusc:
#     print("Stuart", stusc)
# else:
#     print("Draw")




