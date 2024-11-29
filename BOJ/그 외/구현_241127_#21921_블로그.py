n,x = map(int,input().split())


a = list(map(int,input().split()))
cur = sum(a[:x])
ma= cur
cnt=1
for i in range(x,n):
    cur+=a[i]-a[i-x]
    if cur>ma:
        cnt=1
        ma=cur
    elif cur==ma:
        cnt+=1
if ma>0:
    print(ma)
    print(cnt)
else:
    print("SAD")