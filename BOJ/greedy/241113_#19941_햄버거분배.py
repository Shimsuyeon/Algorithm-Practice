n, k = map(int, input().split())
s = list(input())  # 문자열을 리스트로 변환
ans = 0

# 모든 사람의 위치에서 가장 가까운 햄버거를 탐색
for i in range(n):
    if s[i] == 'P':  # 현재 위치에 사람이 있는 경우
        # i-K부터 i+K까지의 범위에서 햄버거를 탐색
        for j in range(max(0, i - k), min(n, i + k + 1)):
            if s[j] == 'H':  # 햄버거가 있다면 먹음
                s[j] = '0'  # 해당 햄버거를 '먹음' 상태로 변경
                ans += 1
                break

print(ans)
