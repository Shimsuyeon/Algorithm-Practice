n = int(input())
a = list(map(int,input().split()))

start=0
end=0
visited=[False]*100001
answer=0

while start<=end and end<n:
    if not visited[a[end]]:
        visited[a[end]]=True
        end+=1
        answer+=end-start
    else:
        while visited[a[end]]:
            visited[a[start]]=False
            start+=1
print(answer)
        