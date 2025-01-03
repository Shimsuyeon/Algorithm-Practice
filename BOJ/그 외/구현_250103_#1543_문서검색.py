n = str(input())
key = str(input())
count=0
while True:
    if n.find(key)==-1:
        break
    else:
        count+=1
        idx = n.find(key)

        s = list(n)
        for i in range(idx,idx+len(key)):
            s[i]="1"
        n = ''.join(s)

print(count)
