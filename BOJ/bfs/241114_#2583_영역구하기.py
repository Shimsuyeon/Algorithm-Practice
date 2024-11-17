from collections import deque

m, n, k = map(int, input().split())
arr = [[0 for _ in range(n)] for _ in range(m)]

# Fill in rectangles
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    for y in range(y1, y2):
        for x in range(x1, x2):
            arr[m - y - 1][x] = 1  # Flip y-axis for correct indexing

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def bfs(y, x, visited):
    q = deque()
    q.append((y, x))
    visited[y][x] = 1
    cnt = 1
    while q:
        cur_y, cur_x = q.popleft()
        for i in range(4):
            x_ = cur_x + dx[i]
            y_ = cur_y + dy[i]
            if 0 <= x_ < n and 0 <= y_ < m and visited[y_][x_] == 0 and arr[y_][x_] == 0:
                visited[y_][x_] = 1
                q.append((y_, x_))
                cnt += 1
    return cnt

visited = [[0 for _ in range(n)] for _ in range(m)]
cnt = 0
areas = []

# Find and count separate areas
for i in range(m):
    for j in range(n):
        if visited[i][j] == 0 and arr[i][j] == 0:
            area_size = bfs(i, j, visited)
            areas.append(area_size)
            cnt += 1

# Output the results
print(cnt)  # Number of separate areas
print(" ".join(map(str, sorted(areas))))  # Sorted area sizes
