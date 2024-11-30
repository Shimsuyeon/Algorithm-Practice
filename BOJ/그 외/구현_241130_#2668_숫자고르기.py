n = int(input())
graph = [0]*(n+1)

for i in range(1,n+1):
    graph[i] = int(input())

visited=[False]*(n+1)


def cycle(graph,n):
    result=set()
    def dfs(node,path):
        if visited[node]:
            if node in path:
                result.update(path[path.index(node):])
            return
        visited[node]=True
        path.append(node)
        dfs(graph[node],path)
        path.pop()
    for i in range(1,n+1):
        if not visited[i]:
            dfs(i,[])
    return sorted(result)

result = cycle(graph,n)
print(len(result))

print("\n".join(map(str,result)))