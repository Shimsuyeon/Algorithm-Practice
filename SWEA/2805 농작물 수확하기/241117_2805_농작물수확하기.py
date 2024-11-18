t = int(input())
for i in range(t):
    n = int(input())
    left = right = n//2
    s=0
    for j in range(n):
        s+=sum(list(map(int,input()))[left:right+1])
        if j<n//2:
            left-=1
            right+=1
        else:
            left+=1
            right-=1
    print(f'#{i+1} {s}')
