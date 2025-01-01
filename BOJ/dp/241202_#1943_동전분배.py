for _ in range(3):
    n = int(input())
    half=0
    m=[]
    for i in range(n):
        cost,num = map(int,input().split())
        half+=(cost*num)
        m.append((cost,num))

    #홀수면 반으로 못나누니까 그냥 0 return
    if half%2!=0:
        print(0)
        continue

    
    half//=2
    dp = [False]*(half+1)
    dp[0]=True
    answer=0
    for cost, num in m:
        for n in range(half, cost - 1, -1):
            if dp[n-cost]:
                for j in range(n):
                    if n+cost * j <=half:
                        dp[n+cost*j]=True
                    else:
                        break
        if dp[-1]:
            answer=1
            break
    print(answer)