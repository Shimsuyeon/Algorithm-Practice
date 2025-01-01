s = input()

#a를 모두 연속으로 만들기 위해 필요한 교환의 횟수를 최소로

result=[]
size = s.count('a')

for i in range(len(s)):
    b_count=0
    for j in range(size):
        index=i+j
        if index>len(s)-1:
            index-=len(s)
        if s[index]=="b":
            b_count+=1
    result.append(b_count)

print(min(result))