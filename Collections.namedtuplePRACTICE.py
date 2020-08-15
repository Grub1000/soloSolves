# import collections
# N = int(input())
# A, B, C, D = input().split()
# stuff = str(A + ' ' + B + ' ' + C + ' ' + D)
# LIST = collections.namedtuple('LIST', stuff)
# l1 = LIST(A = 92, B = 2, C = 'Calum', D = 1)
# print(l1)

# from collections import namedtuple
# N = int(input());student = namedtuple('student',input().strip().split())
# print(sum(float(student(*input().strip().split()).MARKS) for _ in range(N))/N)

from collections import namedtuple
students = namedtuple('students', input().strip().split())
print(students(*input().strip().split()).MARKS)
S1 = students(100,200,430,200)
print(S1.MARKS)