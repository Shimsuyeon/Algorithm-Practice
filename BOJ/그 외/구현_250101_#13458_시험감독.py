import math
n = int(input())
a = list(map(int,input().split()))
b,c = map(int,input().split())

total=0
for i in range(n):
    a[i]-=b
    total+=1
    if a[i]>0:
        total+=math.ceil(a[i]/c)

print(total)