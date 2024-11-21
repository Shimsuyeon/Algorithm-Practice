from itertools import permutations
n = int(input())
k = int(input())

l = [i for i in range(n)]
if n-k<k:
    print(0)
else:
    a = permutations(l,k)
    for i in a:
        print(i)
