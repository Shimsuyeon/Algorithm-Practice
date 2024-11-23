s = str(input())
t = str(input())

# 문자열 뒤에 A 추가
# 문자열 뒤에 B 추가하고 문자열 뒤집기

ans=0
def sub(str1,t):
    global ans
    if len(str1)==len(t):
        if str1==t:
            ans=1
        return
    if t[-1] == 'A':
        sub(str1, t[:-1])
    if t[0]=='B':
        sub(str1, t[:0:-1])
sub(s,t)
print(ans)