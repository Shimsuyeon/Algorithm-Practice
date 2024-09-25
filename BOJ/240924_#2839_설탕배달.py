import sys

n = int(sys.stdin.readline())

# 정확하게 N 킬로그램 배탈
# 3, 5 킬로그램 봉지
# 최소한의 봉지 개수

result = 0

while n >= 0:
    if n % 5 == 0:
        result += n // 5
        print(result)
        break
    n -= 3
    result += 1
else:
    print(-1)