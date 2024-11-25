from collections import deque
n = int(input())
m = int(input())
f = [[] for _ in range(n+1)]
for i in range(m):
    a,b = map(int, input().split())
    f[a].append(b)
    f[b].append(a)
    
visited=[False]*(n+1)
invite=set()

q = deque([1])
visited[1] = True

while q:
    cur = q.popleft()
    for friend in f[cur]:
        if not visited[friend]:
            visited[friend]=True
            invite.add(friend)
            if cur==1:
                q.append(friend)
print(len(invite))
