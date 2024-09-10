import sys

s = str(input())

for i in range(len(s)):
    if s[i:] == s[i:][::-1]:
        print(len(s+s[:i][::-1]))
        break