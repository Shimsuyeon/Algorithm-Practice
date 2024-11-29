n = int(input())

info=[]
result=0
for i in range(n):
    position, height = map(int,input().split())
    info.append([position, height])
info.sort()

i=0
for h in info:
    if h[1]>result:
        result=h[1]
        idx=i
    i+=1

height = info[0][1]

for i in range(idx):
    if height<info[i+1][1]:
        result+=height*(info[i+1][0]-info[i][0])
        height=info[i+1][1]
    else:
        result+=height*(info[i+1][0]-info[i][0])
height=info[-1][1]

for i in range(n-1, idx, -1):
    if height<info[i-1][1]:
        result+=height*(info[i][0]-info[i-1][0])
        height=info[i-1][1]
    else:
        result+=height*(info[i][0]-info[i-1][0])
print(result)