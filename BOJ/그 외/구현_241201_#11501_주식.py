t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int,input().split()))
    #3
    #10 7 6
    #감소수열은 아무것도 안사고, 안파는게 맞음

    #3
    #3 5 9
    #증가 수열은 하루에 하나씩 사고, 마지막날에 전부 파는거

    #5
    #1 1 3 1 2
    #증가 동안 사고, 최고점때 팔고
    #다시 증가 동안 사고...

    # 역순으로 처리?
    
    max_price=0
    result=0

    for i in range(n-1,-1,-1):
        if a[i]>max_price:
            max_price = a[i]
        else:
            result+=max_price-a[i]
    print(result)
    