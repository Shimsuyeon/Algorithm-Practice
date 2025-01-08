import sys
from collections import defaultdict
input = sys.stdin.readline
 
 
def solution(N:int, words:list) -> int:
    cnt = 0
    # 단어 개수를 저장할 dict 리스트 생성
    word = [defaultdict(int) for _ in range(N)]
    
    # 단어 정보 저장
    for i in range(N):
        for w in words[i]:
            word[i][w] += 1
    # 1. 해당 단어에서 기준 단어를 개수만큼 뺌
    # 2. 해당 단어의 개수가 2보다 작으면서, 개수를 모두 더 했을 때 절댓값이
    # 1보다 작으면 카운트
    for i in range(1, N):
        inw = 0
        absi = 0
        for j in word[0].keys():
            word[i][j] -= word[0][j]
        for j in word[i].values():
            inw += j
            absi += abs(j)
            if absi > 2:
                break
        else:
            if abs(inw) <= 1:
                cnt += 1
 
    return cnt 
 
 
 
if __name__ == "__main__":
    N = int(input())
    print(solution(N, [input().strip() for _ in range(N)]))