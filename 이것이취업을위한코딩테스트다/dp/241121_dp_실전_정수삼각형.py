n = int(input())

dp=[]
for i in range(n):
    if i==0:
        a = int(input())
        dp.append(a)
    else:
        a = list(map(int,input().split()))
        al = len(a)
        # print(a)
        # print(dp)
        new_dp=[]
        new_dp.append(dp[0]+a[0])
        for j in range(1,al-1):
            # print(j)
            new_dp.append(max(a[j]+dp[j-1],a[j]+dp[j]))
        new_dp.append(dp[-1]+a[-1])
        dp=new_dp
# print(dp)
print(max(dp))