
# dp[0][0]=1

# for i in range(m):
#     for j in range(n):
#         left=0
#         right=0
#         down=0
#         print(f'현재는 {i} {j} 원소값은 {dp[i][j]}')
#         if dp[i][j]!=0:
#             if j+1<n and arr[i][j+1]-arr[i][j]>0:
#                 dp[i][j]=max(dp[i][j], dp[i][j+1])
#                 print(f'우측 탐색 {i},{j+1} 원소값 {dp[i][j+1]}')
#             if i+1<m and arr[i+1][j]-arr[i][j]>0:
#                 dp[i][j]=max(dp[i][j],dp[i+1][j])
#                 print(f'하단 탐색 {i+1},{j} 원소값 {dp[i+1][j]}')
#             if j-1>0 and arr[i][j-1]-arr[i][j]>0:
#                 dp[i][j]=max(dp[i][j],dp[i][j-1])
#                 print(f'좌측 탐색 {i},{j-1} 원소값 {dp[i][j-1]}')
#             if i-1>0 and arr[i-1][j]-arr[i][j]>0:
#                 dp[i][j]=max(dp[i][j],dp[i-1][j])
#                 print(f'상단탐색 {i-1},{j} 원소값 {dp[i-1][j]}')
#             if j+1<n and arr[i][j]-arr[i][j+1]>0:
#                 dp[i][j+1]=max(dp[i][j], dp[i][j+1]+1)
#                 print(f'우측 탐색 {i},{j+1} 원소값 {dp[i][j+1]}')
#             if i+1<m and arr[i][j]-arr[i+1][j]>0:
#                 dp[i+1][j]=max(dp[i][j],dp[i+1][j]+1)
#                 print(f'하단 탐색 {i+1},{j} 원소값 {dp[i+1][j]}')
#             if j-1>0 and arr[i][j]-arr[i][j-1]>0:
#                 dp[i][j-1]=max(dp[i][j],dp[i][j-1]+1)
#                 print(f'좌측 탐색 {i},{j-1} 원소값 {dp[i][j-1]}')
#             if i-1>0 and arr[i][j]-arr[i-1][j]>0:
#                 dp[i-1][j]=max(dp[i][j],dp[i-1][j]+1)
#                 print(f'상단탐색 {i-1},{j} 원소값 {dp[i-1][j]}')

# print(dp)
# print(dp[m-1][n-1])
import sys
sys.setrecursionlimit(10 ** 9)
m,n = map(int,sys.stdin.readline().split())
arr = [list(map(int,sys.stdin.readline().split())) for _ in range(m)]

dp = [[-1]*n for _ in range(m)]
dp[-1][-1]=1

dx=[0,0,1,-1]
dy=[1,-1,0,0]
def dfs(y,x):
    if y==m-1 and x==n-1:
        return 1

    if dp[y][x]==-1:
        dp[y][x]=0
        for i in range(4):
            ay,ax = y+dy[i], x+dx[i]
            if -1<ax<n and -1<ay<m and arr[y][x]>arr[ay][ax]:
                dp[y][x]+=dfs(ay,ax)
    return dp[y][x]

print(dfs(0,0))