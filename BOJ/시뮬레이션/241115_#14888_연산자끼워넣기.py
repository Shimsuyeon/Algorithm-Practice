n = int(input())
arr = list(map(int,input().split()))

plus, minus, cross, div = list(map(int,input().split()))

max_ = - int(1e9)
min_ = int(1e9)

def dfs(plus, minus, cross, div, sum, idx):
    global max_, min_
    if idx == n:
        max_ = max(max_, sum)
        min_ = min(min_, sum)
        return
    if plus:
        dfs(plus-1, minus, cross, div, sum+arr[idx], idx+1)
    if minus:
        dfs(plus, minus-1, div, sum-arr[idx], idx+1)
    if cross:
        dfs(plus, minus, cross-1, div, sum*arr[idx], idx+1)
    if div:
        dfs(plus, minus, cross, div-1, int(sum/arr[idx]), idx+1)

dfs(plus, minus, cross, div, arr[0],1)
print(max_)
print(min_)