t = int(input())
def dfs(index, taste, cal):
    global max_score
    if cal>l:
        return
    if max_score<taste:
        max_score=taste
    if index==n:
        return
    t,c = a[index]
    dfs(index+1,taste+t, cal+c)
    dfs(index+1,taste,cal)

for i in range(t):
    n,l = map(int,input().split())
    a = [list(map(int,input().split())) for _ in range(n)]
    max_score=0
    a.sort()
    dfs(0,0,0)
    print(f'#{i+1} {max_score}')



    