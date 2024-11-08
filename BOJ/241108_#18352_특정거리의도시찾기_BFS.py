from collections import deque



n,m,k,x = map(int, input().split())

graph = [[] for _ in range(n+1)]

for i in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)


distance = [-1]*(n+1)
distance[x] = 0
q = deque([x])
while q:
    cur = q.popleft()
    for next in graph[cur]:
        if distance[next]==-1:
            distance[next]=distance[cur]+1
            q.append(next)
check=False
for i in range(1,n+1):
    if distance[i]==k:
        print(i)
        check=True
if check==False:
    print(-1)
    