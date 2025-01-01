import sys
input = sys.stdin.readline

n,m = map(int,input().split())

a = set([input().strip() for _ in range(n)])

for _ in range(m):
    cur = set(input().strip().split(','))
    a-=cur
    print(len(a))

