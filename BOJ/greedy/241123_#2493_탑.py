n = int(input())
a = list(map(int, input().split()))
ans=[0]*n
stack=[]
for i in range(n):
    t = a[i]
    while stack and a[stack[-1]]<t:
        stack.pop()
    if stack:
        ans[i]=stack[-1]+1
    stack.append(i)

print(*ans)
