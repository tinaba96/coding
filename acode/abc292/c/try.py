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

import math

def count(n):
    ok = 1
    mid = math.sqrt(n)
    if int(mid)**2 == n:
    #if mid**2 == n:
        ok = 0
    val = 0
    if n == 2 or n == 3:
        return 2
    for i in range(1, int(mid) + ok):
        if n % i == 0:
            val += 1
    if ok == 0:
        return 2*val + 1
    else:
        return 2*val


N = int(input())

ans = 0

mp = [0 for j in range(N+1)]

#half = N // 2
#half2 = N - half

for m in range(1, N+1):

    #print(prime_factorize(m))
    #print(count(m))
    mp[m] = count(m)


#print(mp)
k = max(mp)

#print(mp.index(k))
#print(mp[240])
#print(mp[241])

for a in range(1, N):
    ans += mp[a]*mp[N-a]

print(ans)


