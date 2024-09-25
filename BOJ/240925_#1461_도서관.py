import sys
import math
n,m = map(int,sys.stdin.readline().split())

book = list(map(int, sys.stdin.readline().split()))

book.sort()

result = 0

# 39*2

# 29*2
# 6*2
# 11*2
# 58+12+22=92
# 92+39 = 131

negatives = []
positives = []

max=0
for i in book:
    if abs(i)>abs(max):
        max = i
# max 
for i in book:
    if i<0:
        negatives.append(i)
    elif i>0:
        positives.append(i)

for i in range(0,len(negatives),m):
    result += abs(negatives[i])*2
for i in range(len(positives)-1,-1,-m):
    result += positives[i]*2
print(result-abs(max))
