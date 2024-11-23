import sys
import heapq

n,k = map(int,sys.stdin.readline().split())

jewel=[]
for _ in range(n):
    heapq.heappush(jewel, list(map(int,sys.stdin.readline().split())))
bag = [int(input()) for _ in range(k)]

jewel.sort()
bag.sort()

max_heap=[]
result=0
j=0
for b in bag:
    while j<n and jewel[j][0]<=b:
        heapq.heappush(max_heap, -jewel[j][1])
        j+=1
    if max_heap:
        result-=heapq.heappop(max_heap)

print(result)
