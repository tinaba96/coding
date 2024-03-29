import sys
sys.setrecursionlimit(500005)
#import pypyjit # this is for solving slow issue for pypy when using recursion but python will not need this (test will fail but submit works)
#pypyjit.set_param('max_unroll_recursion=-1')

import math
A, B = list(map(int, input().split()))
a2 = 4*(B**2)
b2 = B**2


def ch(x):
    val = (1+x)**3
    if a2*val < A**2:
        return 0
    else:
        return 1

left = 0
right = 10**6+1


while True:
    v = (left+right)//2
    if ch(v) == 0:
        left = v
    else:
        right = v
    if right - left < 2:
        break


def f(g) :
    return B*(g-1)+(A/(math.sqrt(g)))
def f2(g) :
    return B*(g-1)+math.sqrt(A/(g**2))
    

#print(right, left)

ans = min(f(3), f(1), f(2), f(4))

for i in range(10):
    ans = min(f(left+i), ans)

print(ans)




