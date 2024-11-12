from collections import deque
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]



def bfs(i,j,k,visited):
    q=deque()
    q.append([i,j])
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    while q:
        y,x = q.popleft()
        visited[y][x] = True
        for i in range(4):
            y_=y+dy[i]
            x_=x+dx[i]
            if 0<=y_<n and 0<=x_<n and not visited[y_][x_] and arr[y_][x_]>k:
                visited[y_][x_]=True
                q.append([y_,x_])


max_height = max(max(row) for row in arr)
m = 0

for k in range(max_height + 1):
    visited = [[False for _ in range(n)] for _ in range(n)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] > k and not visited[i][j]:
                bfs(i, j, k, visited)
                cnt += 1
    m = max(cnt, m)

print(m)