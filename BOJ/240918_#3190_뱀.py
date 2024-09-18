n = int(input())
k = int(input())

# 사과 위치 (1-based -> 0-based로 변환)
apples = set(tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(k))

# 방향 변환 정보
l = int(input())
turns = [input().split() for _ in range(l)]
turns = [(int(t), d) for t, d in turns]

# 초기 방향 (동, 남, 서, 북)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 초기 뱀 위치
snake = [(0, 0)]

# 초기 방향
direction = 0

# 시간
time = 0

# 현재 변환 정보
turn_idx = 0

# 게임 진행
while True:
    time += 1
    x, y = snake[-1]  # 뱀의 머리
    nx, ny = x + dx[direction], y + dy[direction]  # 새로운 머리 위치

    # 벽에 부딪히거나 자기 자신과 부딪히면 종료
    if nx < 0 or nx >= n or ny < 0 or ny >= n or (nx, ny) in snake:
        break

    # 사과가 있는 경우
    if (nx, ny) in apples:
        apples.remove((nx, ny))  # 사과를 먹음
        snake.append((nx, ny))   # 머리를 늘림 (꼬리 유지)
    else:
        snake.append((nx, ny))   # 머리를 늘림
        snake.pop(0)             # 꼬리 이동

    # 방향 전환 (turns 리스트에 남아 있는 경우)
    if turn_idx < len(turns) and time == turns[turn_idx][0]:
        t, d = turns[turn_idx]
        if d == 'L':
            direction = (direction - 1) % 4  # 왼쪽 회전
        else:
            direction = (direction + 1) % 4  # 오른쪽 회전
        turn_idx += 1  # 다음 방향 전환 정보로

print(time)
