from itertools import combinations
n = int(input())
a=[]
for i in range(1,n+1):
    a.append(i)
arr = [list(map(int,input().split())) for _ in range(n)]

b = combinations(a,2)

for i in b:
    