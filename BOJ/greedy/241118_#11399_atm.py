n = int(input())
a = list(map(int,input().split()))

# p1=3
# p2=1
# pe=4
# p4=3
# p5=2

# [1,2,3,4,5]

# 3 3+1 3+1+4 3+1+4+3 3+1+4+3+2

# [2,5,1,4,3]

# 1 1+2 1+2+3 1+2+3+3 1+2+3+3+4

a.sort()
s=0
t=0
for i in a:

    s+=i
    t+=s
print(t)
