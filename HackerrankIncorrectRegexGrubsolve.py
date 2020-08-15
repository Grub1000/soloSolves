import re
N = int(input())
for i in range(N):
    Ptrn = str(input())
    try:
        re.compile(Ptrn)
    except re.error:
        print(False)
    else:
        print(True)