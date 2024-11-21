from collections import deque
n,m = map(int,input().split())

a = [list(map(int,input().strip())) for _ in range(n)]

visited = [[False for _ in range(m)] for _ in range(n)]
dx=[0,0,1,-1]
dy=[1,-1,0,0]
def bfs(i,j):
    q = deque()
    q.append([i,j])
    visited[i][j]=True
    while q:
        cur = q.popleft()
        for k in range(4):
            ax = cur[1]+dx[k]
            ay = cur[0]+dy[k]
            if 0<=ax<m and 0<=ay<n and not visited[ay][ax] and a[ay][ax]==0:
                visited[ay][ax]=True
                q.append([ay,ax])

cnt=0
for i in range(n):
    for j in range(m):
        if a[i][j]==0 and not visited[i][j]:
            bfs(i,j)
            cnt+=1

print(cnt)