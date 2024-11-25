from collections import deque
n = int(input())

color = [list(map(str,input().strip())) for _ in range(n)]

# R과 G의 차이 거의 못느낌

dx=[0,0,1,-1]
dy=[1,-1,0,0]
def no(i,j, char):
    q=deque()
    q.append([i,j])
    visited[i][j]=True
    while q:
        y,x = q.popleft()
        visited[y][x]=True
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<n and not visited[ny][nx] and color[ny][nx]==char:
                visited[ny][nx]=True
                q.append([ny,nx])

def yes(i,j,char):
    q=deque()
    q.append([i,j])
    visited_y[i][j]=True
    while q:
        y,x = q.popleft()
        visited_y[y][x]=True
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0<=nx<n and 0<=ny<n and not visited_y[ny][nx]:
                if char=='B' and color[ny][nx]=='B':
                    visited_y[ny][nx]=True
                    q.append([ny,nx])
                elif (char=='G' or char=='R') and (color[ny][nx]=='G' or color[ny][nx]=='R'):
                    visited_y[ny][nx]=True
                    q.append([ny,nx])


cnt_n=0
cnt_y=0
visited=[[False for _ in range(n)] for _ in range(n)]
visited_y = [[False for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            no(i,j,color[i][j])
            cnt_n+=1
        if not visited_y[i][j]:
            yes(i,j,color[i][j])
            cnt_y+=1

print(cnt_n, cnt_y)