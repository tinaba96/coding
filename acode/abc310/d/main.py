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

import itertools




N, T, M = list(map(int, input().split()))
mp = [[] for i in range(N+1)]

for i in range(M):
    A, B = list(map(int, input().split()))
    mp[A].append(B)
    mp[B].append(A)

l = []
for i in range(N):
    l.append(i+1)

cases = list(itertools.combinations(l, T))


visit = [0 for i in range(N+1)]

cnt = 0

def solv(vi, q):
    global cnt
    if len(q) == 0:
        return
    v = q.pop()
    if sum(vi) == N:
        cnt += 1
        return
    for i in range(1, N+1):
        if visit[i] == 1:
            continue
        if i != v and i not in mp[v]: # you have to check all the team member (not only v)
            visit[i] = 1
            q.append(i)
            solv(vi, q)
            # pop and visit[i] = 0 is needed
    return


for c in cases:  # o(nCt) -> 10C5 = 252
    visit = [0 for i in range(N+1)]
    for i in c:
        visit[i] = 1

    # O(T!) -> 10! = 3628800
    for e in itertools.permutations(c): # this is not needed (solv() is already incorrect but solve() is doing the similar operations)
        e = list(e)
        solv(visit, e)


print(cnt)

# this will count duplicated case
# maybe you need to do numbering to each node (to identify the team)

# if you want to implement BFS, you should use either recurrsion or while&queue
# here, you are implementing both and making confusions
