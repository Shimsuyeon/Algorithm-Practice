n,m = map(int,input().split())
mon=[]
dp = [10001]*(10001)
mon=[]
for i in range(n):
    coin = int(input())
    dp[coin]=1
    mon.append(coin)

for i in range(1,m+1):
    for j in mon:
        if i>=j:
            dp[i]=min(dp[i], dp[i-j]+1)
if dp[m]==10001:
    print(-1)
else:
    print(dp[m])