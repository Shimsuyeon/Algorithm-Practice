n,s = map(int, input().split())

a = list(map(int,input().split()))

# 연속 부분합 중 합이 s가 되는 것 중 가장 짧은 것


ans=100001
start=0
end=0
partial=a[0]

while True:
    if partial<s:
        end+=1
        if end==n:
            break
        partial+=a[end]
    else:
        partial-=a[start]
        ans = min(ans, end-start+1)
        start+=1

if ans==100001:
    print(0)
else:
    print(ans)
