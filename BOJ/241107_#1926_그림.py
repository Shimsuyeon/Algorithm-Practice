from collections import deque

def bfs(x, y):
    q = deque()
    q.append([x,y])
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    ans = 1

    arr[x][y]=0
    while q:
        node = q.popleft()
        x0, y0 = node[0], node[1]
        for i in range(4):
            y_ = y0 + dy[i]
            x_ = x0 + dx[i]
            if 0 <= x_ < n and 0 <= y_ < m and arr[x_][y_] == 1:
                    ans += 1
                    arr[x_][y_]=0
                    q.append([x_, y_])
    maxi.append(ans)
                    

    
n,m = map(int, input().split())

arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))
maxi=[0]
cnt=0
for i in range(n):
    for j in range(m):
        if arr[i][j]==1:
            bfs(i,j)
            cnt+=1

print(cnt)
print(max(maxi))