import sys

n = int(input())
l = [0]+list(map(int,sys.stdin.readline().split()))
dp = [[0 for _ in range(n+1)] for _ in range(n+1)]

for i in range(1,n+1):
    dp[i][i] = 1
for i in range(1,n):
    if l[i] == l[i+1]:
        dp[i][i+1] = 1
    else:
        dp[i][i+1]=0


for length in range(3,n+1):
    for start in range(1,n-length+2):
        end = start+length-1
        if l[start]==l[end] and dp[start+1][end-1]==1:
            dp[start][end]=1
        else:
            dp[start][end]=0

m = int(input())
for _ in range(m):
    s,e = map(int,sys.stdin.readline().split())
    print(dp[s][e])
    