#making and testing \
n = int(input())
count = 0
for Number in range (1, n):
    count = 0
    for i in range(2, (Number)):
        if(Number % i == 0):
            count = count + 1

    if(count == 0 and Number != 1):
        print(Number, end = ' ')




















