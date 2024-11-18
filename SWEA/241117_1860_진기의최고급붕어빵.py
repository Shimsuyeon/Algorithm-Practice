t = int(input())

for i in range(t):
    n,m,k = map(int,input().split())
    # n명의 손님, m초마다 k개 붕어빵
    a = list(map(int,input().split()))
    fish=0
    for j in range(0,max(a)+1):
        if j and j%m==0:
            fish+=k
        if j in a:
            fish-=1
        if fish<0:
            print(f'{i+1} Impossible')
            break
    print(f'{i+1} Possible')