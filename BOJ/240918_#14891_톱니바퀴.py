#빙글뱅글 톱니바퀴 14891

import sys

# 8*4 배열 초기화
array=[]
for i in range(4):
    array.append([int(x) for x in input()])

k = int(input())
turn = []
for _ in range(k):
    a, b = map(int, input().split())
    turn.append((a, b))
# -1 반시계 1 시계
for num,direction in turn:
    rotate_dir = [0]*4
    rotate_dir[num-1] = direction
    for i in range(num-1, 3):
        if array[i][2] != array[i+1][6]:
            rotate_dir[i+1] = -rotate_dir[i]
        else:
            break
    for i in range(num-1, 0, -1):
        if array[i][6] != array[i-1][2]:
            rotate_dir[i-1] = -rotate_dir[i]
        else:
            break
    for i in range(4):
        if rotate_dir[i] !=0:
            if rotate_dir[i] ==1:
                array[i] = [array[i][-1]] + array[i][:-1]
            elif rotate_dir[i] == -1:
                array[i] = array[i][1:] + array[i][:1]

result = 0
for i in range(4):
    if array[i][0] == 1:
        result += 2**i
print(result)