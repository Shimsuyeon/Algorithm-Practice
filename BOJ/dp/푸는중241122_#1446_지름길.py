n,d = map(int,input().split())

a = [list(map(int,input().split())) for _ in range(n)]
a.sort(key = lambda x: (x[0], x[1],x[2]))
print(a)
start=a[0][0]
end=a[0][1]
dis = a[0][0]+a[0][2]

for i in range(1,n):
    if a[i][2]<d:
        if start<=a[i][0]<end:
            temp1 = 
            temp2 = 