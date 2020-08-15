n = int(input())
d = {}
for i in range(n):
    name,*line = input().split()
    seq = list(map(float,line))
    d[name] = seq
given_name = input()
def average():
   n = sum(d[given_name])
   m = format(float(n) / float(3), '.2f')

   return m
print(average())
