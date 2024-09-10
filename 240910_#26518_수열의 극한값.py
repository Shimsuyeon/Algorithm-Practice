import sys
import math

b,c,a1,a2 = map(int, input().split())

# a1, a2 초항
# ai = b*a_(i-1) + c * a_(i-2) (i >= 3)
# a_n / a_(n-1)의 극한 구하기

print((b+math.sqrt(b*b+4*c))/2)