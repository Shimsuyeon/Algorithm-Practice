n = int(input())
arr = [int(input()) for _ in range(n)]

# 로프 k개이면, 각 로프에는 w/k 만큼 중량이 걸림
arr.sort()
ans=[]

for x in arr:
    ans.append(x*n)
    n-=1

print(max(ans))