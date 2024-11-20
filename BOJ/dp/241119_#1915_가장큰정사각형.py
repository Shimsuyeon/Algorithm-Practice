n,m = map(int, input().split())

arr = [list(map(int,input().strip())) for _ in range(n)]
dp = [ [0 for _ in range(m+1)] for _ in range(n+1)]
for i in range(n):
    for j in range(m):
        dp[i+1][j+1] = arr[i][j]
ma=0

for i in range(1,n+1):
    for j in range(1,m+1):
        if dp[i][j]!=0:
            dp[i][j]+=min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])
            ma = max(ma,dp[i][j])

print(ma*ma)