from collections import defaultdict
n,k = map(int,input().split())

a = list(map(int,input().split()))

count = defaultdict(int)
start=0
max_l = 0

for end in range(n):
    count[a[end]]+=1
    while count[a[end]]>k:
        count[a[start]]-=1
        if count[a[start]]==0:
            del count[a[start]]
        start+=1
    max_l = max(max_l, end-start+1)

print(max_l)