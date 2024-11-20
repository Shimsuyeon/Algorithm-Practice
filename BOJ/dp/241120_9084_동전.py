t = int(input())

for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.insert(0,0)
    m = int(input())

    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    
    for i in range(n+1):
        dp[i][0]=1
    for i in range(1,n+1):
        for j in range(1,m+1):
            dp[i][j] = dp[i-1][j]
            if j-arr[i]>=0:
                dp[i][j]+=dp[i][j-arr[i]]
    print(dp[n][m])