#접시, 초밥가짓수, 연속, 쿠폰번호
n,d,k,c = map(int,input().split())

a = [int(input()) for _ in range(n)]

#쿠폰번호가 포함되지 않은 k개를 먹으면 최대가짓수?

dp = [0]*n

#i번째 위치에서 k개를 먹을 때 가짓수?
s=0
for i in range(n):
    if i<=n-k:
        temp = set(a[i:i+k])
    else:
        temp = set(a[i:])
        temp.update(a[:(i+k)%n])
    temp.add(c)
    s = max(s,len(temp))

    
print(s)
