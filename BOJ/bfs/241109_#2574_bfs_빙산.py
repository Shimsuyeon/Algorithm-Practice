from collections import deque
n,m = map(int, input().split())

arr =[list(map(int,input().split())) for _ in range(n)]
dx=[0,0,1,-1]
dy=[1,-1,0,0]
def bfs(y,x,visited):
    q = deque()
    q.append((y,x))
    visited[y][x] = 1

    while q:
        cur = q.popleft()
        for i in range(4):
            x_ = cur[1]+dx[i]
            y_ = cur[0]+dy[i]
            if 0<=x_<m and 0<=y_<n and visited[y_][x_]==0 and arr[y_][x_]>0:
                visited[y_][x_]=1
                q.append((y_,x_))

def melt():
    temp = [[0 for _ in range(m)] for _ in range(n)]
    for y in range(n):
        for x in range(m):
            if arr[y][x]>0:
                cnt=0
                for i in range(4):
                    x_ = x+dx[i]
                    y_ = y+dy[i]
                    # 0 개수 세서 그만큼 빼주기
                    # 음수가 되지 않게 max 사용
                    if 0<=x_<m and 0<=y_<n and arr[y_][x_]==0:
                        cnt+=1
                temp[y][x] = max(0,arr[y][x]-cnt)
    return temp

year=0

while True:
    visited = [[0 for _ in range(m)] for _ in range(n)]
    count = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] >0 and visited[i][j]==0:
                bfs(i,j,visited)
                count+=1
    if count==0:
        year=0
        break
    if count>=2:
        break
    arr=melt()
    year+=1

    
print(year)