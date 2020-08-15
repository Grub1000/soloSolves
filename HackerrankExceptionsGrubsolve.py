N = int(input())
for i in range(N):
    a, b = input().split(' ')
    try:
        print(round(int(a)/int(b)))
    except ZeroDivisionError:
        print("Error Code: integer division or modulo by zero" )
    except ValueError as e:
        print("Error Code:", e)