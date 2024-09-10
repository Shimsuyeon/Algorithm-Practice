# N-Queen 문제는 크기가 N × N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

# N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

import sys

n = int(input())

arr = [0] * n
cnt = 0

def det(num): # 검증 함수
    for v in range(num):
        if arr[num] == arr[v] or abs(arr[num] - arr[v]) == num - v: # 같은 위치, 대각선 검증
            return 0
    return 1
    
def func(num):
    global cnt
    
    if num == n : # 여기까지 도달하게 되면 cnt += 1을 통해 경우의 수를 카운트
        cnt += 1
        return
        
    for i in range(n):
        arr[num] = i
        if det(num): # 검증을 통과하면 func(num + 1) 호출
            func(num + 1)
func(0)
print(cnt)