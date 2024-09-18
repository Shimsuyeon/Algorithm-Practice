n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# 네 방향 이동 (상, 하, 좌, 우)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
max_sum = 0
visited = [[False] * m for _ in range(n)]

# DFS를 통해 테트로미노 탐색 (4칸)
def dfs(x, y, depth, total):
    global max_sum

    # 깊이 4에 도달하면 최대값 갱신
    if depth == 4:
        max_sum = max(max_sum, total)
        return

    # 네 방향으로 이동
    for dx, dy in directions:
        nx, ny = x + dx, y + dy

        # 범위 내에 있고 아직 방문하지 않았다면
        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs(nx, ny, depth + 1, total + arr[nx][ny])
            visited[nx][ny] = False

# ㅗ, ㅜ, ㅏ, ㅓ 모양의 테트로미노 처리
def check_special_shapes(x, y):
    global max_sum
    special_shapes = [
        # ㅗ 모양
        [(0, 0), (0, 1), (0, 2), (-1, 1)],
        # ㅜ 모양
        [(0, 0), (0, 1), (0, 2), (1, 1)],
        # ㅏ 모양
        [(0, 0), (1, 0), (2, 0), (1, 1)],
        # ㅓ 모양
        [(0, 0), (1, 0), (2, 0), (1, -1)],
    ]
    
    for shape in special_shapes:
        try:
            total = 0
            for dx, dy in shape:
                total += arr[x + dx][y + dy]
            max_sum = max(max_sum, total)
        except IndexError:
            continue

# 모든 좌표에서 DFS와 특수 모양 체크 수행
for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, 1, arr[i][j])  # 깊이 1부터 시작
        visited[i][j] = False
        
        # 특수 모양 처리
        check_special_shapes(i, j)

print(max_sum)
