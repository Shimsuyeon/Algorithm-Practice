import sys

s = str(input())

for i in range(len(s)):
    # print(s, s[i:], s[i:][::-1], s[:i][::-1])
    if s[i:] == s[i:][::-1]:
        print(len(s+s[:i][::-1]))
        break