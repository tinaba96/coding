#尺取り法

import sys
sys.setrecursionlimit(500005)
#sys.setrecursionlimit(10**9)
#import pypyjit # this is for solving slow issue for pypy when using recursion but python will not need this (test will fail but submit works)
#pypyjit.set_param('max_unroll_recursion=-1')

from collections import Counter
#mylist = ["apple","banana","apple","apple","orange"]
#mycounter = Counter(mylist)
from collections import defaultdict
#d = defaultdict(int)


N, M, D = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A.sort()
B.sort()

import bisect

ans = -1

indB = 0

for i in range(N):
    while True:
        if abs(A[i]-B[indB]) <= D:
            ans = max(ans, A[i]+B[indB])
        if indB+1 < M and A[i]+D >= B[indB+1]:
            indB += 1
        else:
            break


'''
# this is also OK
for i in range(N):
    while True:
        if indB >= M or A[i]+D < B[indB]:
            if indB > 0:
                indB -= 1
            break
        if abs(A[i]-B[indB]) <= D:
            ans = max(ans, A[i]+B[indB])
        indB += 1
'''


print(ans)




