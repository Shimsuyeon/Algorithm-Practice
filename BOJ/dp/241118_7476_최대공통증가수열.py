n = int(input())
a = list(map(int,input().split()))
m = int(input())
b = list(map(int,input().split()))

arr = [[0 for _ in range(m+1)] for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        if a[i-1]==b[j-1]:
            for k in range(i):
                if a[k - 1] < a[i - 1]:
                    arr[i][j] = max(arr[i][j], arr[k][j] + 1)
        else:
            arr[i][j] = max(arr[i-1][j], arr[i][j-1])
length = max(max(row) for row in arr)
print(length)
result=[]
x,y = n,m
while x > 0 and y > 0:
    if arr[x][y] == arr[x - 1][y]:
        x -= 1
    elif arr[x][y] == arr[x][y - 1]:
        y -= 1
    elif arr[x][y] == arr[x - 1][y - 1] + 1 and a[x - 1] == b[y - 1]:
        result.append(a[x - 1])
        x -= 1
        y -= 1
    else:
        x -= 1

print(*result[::-1])


