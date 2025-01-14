n,d = map(int, input().split())

info=[]
dp = [i for i in range(d+1)]
for i in range(n):
    start,dest,length = map(int,input().split())
    if dest-start>length:
        info.append((start,dest,length))
info.sort()

for start,dest,length in info:
    for i in range(1,d+1):
        if dest==i:
            dp[i]=min(dp[i],dp[start]+length)
        else:
            dp[i]=min(dp[i],dp[i-1]+1)

print(dp[d])

