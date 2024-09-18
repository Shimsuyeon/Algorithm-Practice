import sys
from itertools import combinations
while True:
    arr = list(map(int, input().split()))
    k = arr[0]
    s = arr[1:]
    if k == 0:
        break
    count=0
    for comb in combinations(s, 6):
        print(' '.join(map(str, comb)))
    print()
        
