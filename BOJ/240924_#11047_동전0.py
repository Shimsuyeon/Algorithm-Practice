import sys

n,k = map(int, sys.stdin.readline().split())

coin = [int(sys.stdin.readline()) for _ in range(n)]

coin.sort(reverse=True)

result = 0

for i in coin:
    result += k // i
    k %= i

print(result)