n,m,l,k = map(int, input().split())
a=[]
for _ in range(k):
    a.append(list(map(int,input().split())))

ans=0
for i in range(k):
    for j in range(k):
        cnt=0
        sx,sy = min(a[i][0], a[j][0]), min(a[i][1], a[j][1])
        for x,y in a:
            if sx<=x<=sx+l and sy<=y<=sy+l:
                cnt+=1
        ans = max(ans,cnt)
print(k-ans)