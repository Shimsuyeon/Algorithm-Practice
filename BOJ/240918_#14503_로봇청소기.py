import sys

n, m = map(int, sys.stdin.readline().split())
r, c, d = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

# 북, 동, 남, 서 방향에 따른 좌표 이동
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 청소 여부 기록
cleaned = [[0] * m for _ in range(n)]
cleaned[r][c] = 1  # 시작 위치는 청소함
result = 1  # 청소한 칸 개수

while True:
    cleaned_flag = False  # 네 방향 모두 청소되었거나 벽인 경우 체크
    for _ in range(4):  # 네 방향을 체크
        d = (d + 3) % 4  # 왼쪽으로 회전
        nx, ny = r + dx[d], c + dy[d]
        
        if 0 <= nx < n and 0 <= ny < m and not cleaned[nx][ny] and arr[nx][ny] == 0:
            # 청소되지 않은 빈 칸이 있다면 이동해서 청소
            r, c = nx, ny
            cleaned[r][c] = 1
            result += 1
            cleaned_flag = True  # 청소할 칸이 있었다
            break
    
    # 네 방향 모두 청소되어 있거나 벽인 경우
    if not cleaned_flag:
        # 후진 가능 여부 확인
        back_x, back_y = r - dx[d], c - dy[d]
        if 0 <= back_x < n and 0 <= back_y < m and arr[back_x][back_y] == 0:
            # 후진 가능하면 후진
            r, c = back_x, back_y
        else:
            # 후진할 수 없으면 작동 멈춤
            break

print(result)
