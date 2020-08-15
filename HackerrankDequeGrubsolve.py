import collections
N = int(input())
d = collections.deque()
for i in range(N):
    M = input().split()
    if M[0] == 'append':
        d.append(int(M[1]))
    elif M[0] == 'appendleft':
        d.appendleft(int(M[1]))
    elif M[0] == 'pop':
        d.pop()
    elif M[0] == 'popleft':
        d.popleft()
for i in d:
    print(i,end=' ')