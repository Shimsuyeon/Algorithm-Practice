
import heapq
n = int(input())
arr = [list(map(int,input())) for _ in range(n)]

dp=[0]*n

arr.sort()

queue =[]
for i in arr:
    heapq.heappush(queue)