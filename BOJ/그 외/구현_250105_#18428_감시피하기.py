from itertools import combinations

n = int(input())
board = []
teachers = []
spaces = []

for i in range(n):
    row = input().split()
    board.append(row)
    for j in range(n):
        if row[j] == 'T':
            teachers.append((i, j))
        if row[j] == 'X':
            spaces.append((i, j))

def watch(x, y, d):
    if d == 0:  # left
        while y >= 0:
            if board[x][y] == 'S': return True
            if board[x][y] == 'O': return False
            y -= 1
    elif d == 1:  # right
        while y < n:
            if board[x][y] == 'S': return True
            if board[x][y] == 'O': return False
            y += 1
    elif d == 2:  # up
        while x >= 0:
            if board[x][y] == 'S': return True
            if board[x][y] == 'O': return False
            x -= 1
    else:        # down
        while x < n:
            if board[x][y] == 'S': return True
            if board[x][y] == 'O': return False
            x += 1
    return False

def process():
    for x, y in teachers:
        for i in range(4):
            if watch(x, y, i):
                return True
    return False

found = False
for combo in combinations(spaces, 3):
    for x, y in combo:
        board[x][y] = 'O'
    if not process():
        found = True
        break
    for x, y in combo:
        board[x][y] = 'X'

print("YES" if found else "NO")
