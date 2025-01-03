n = int(input())
s = list(map(int,input().split()))

s.sort()
result=float('inf')

for i in range(n):
    temp = s[i]+s[2*n-i-1]
    result = min(result,temp)

print(result)