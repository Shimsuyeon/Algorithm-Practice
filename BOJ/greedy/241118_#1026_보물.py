n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
a.sort()
s=0
for i in range(n):
    b_ = max(b)
    s+=a[i]*b_
    b.remove(b_)
    

print(s)