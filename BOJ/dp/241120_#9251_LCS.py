a = list(input().strip())
b = list(input().strip())

al = len(a)
bl = len(b)

arr = [[0 for _ in range(al+1)] for _ in range(bl+1)]

for i in range(1,bl+1):
    for j in range(1,al+1):
        if a[j-1]==b[i-1]:
            arr[i][j]=arr[i-1][j-1]+1
        else:
            arr[i][j]=max(arr[i-1][j],arr[i][j-1])
print(arr[bl][al])