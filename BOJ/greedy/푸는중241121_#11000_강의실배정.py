n = int(input())
c = []
for i in range(n):
    s,t = map(int,input().split())
    c.append([s,t])

cur = [c[0]]
c.sort(key = lambda x: (x[0], x[1]))
count=1
for i in range(1,n):
    s,t = i[1],i[1]
    for j in cur:
        if j[0]<s<
