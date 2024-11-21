#google 인터뷰 기출/이취코
# 2,3,5만을 소인수로
# 2,3,5만을 약수로 가지는 합성수
# 1은 못생긴수라고 가정
# n번째 못생긴 수?

n = int(input())

# if n<6:
#     print(n)
# else:
#     dp=[1,1,1,1,1]
#     cnt=5
#     cur=5
#     while cnt<n:
#         cur+=1
        
#         if (cur%2==0 and dp[cur//2-1]==1) or (cur%3==0 and dp[cur//3-1]==1) or (cur%5==0 and dp[cur//5-1]==1):
#             dp.append(1)
#             cnt+=1
#         else:
#             dp.append(0)
#     print(cur)

ugly = [0]*n
ugly[0]=1

i2=i3=i5=0

next2,next3,next5=2,3,5

for l in range(1,n):
    ugly[l] =min(next2,next3,next5)
    if ugly[l]==next2:
        i2+=1
        next2=ugly[i2]*2
    if ugly[l]==next3:
        i3+=1
        next3=ugly[i3]*3
    if ugly[l]==next5:
        i5+=1
        next5 = ugly[i5]*5
print(ugly[n-1])