n = int(input())
flower=[list(map(int,input().split())) for _ in range(n)]

flower.sort()

i=0
result=0
last_end = (3,1)

while i<n:
    sm,sd,em,ed = flower[i]
    if (sm,sd) <= last_end < (em,ed):
        max_end = (em,ed)
        while i<n-1:
            nsm,nsd,nem,ned = flower[i+1]
            if last_end<(nsm,nsd):
                break
            if max_end<(nem,ned):
                max_end=(nem,ned)
            i+=1
        result+=1
        last_end=max_end
        if(11,30)<last_end:
            print(result)
            exit(0)
    i+=1
print(0)



# 0301 부터 1130까지

