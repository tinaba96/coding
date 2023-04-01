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


L, N1, N2 = list(map(int, input().split()))

s1 = {}
s2 = {}

ind1 = 0
ind2 = 0

for i in range(N1):
    v, l = list(map(int, input().split()))
    val = 0
    base = 2**l-1 # 111111
    val = val | (base >> ind)
    print(bin(val))
    ind += l


# approach here
# you will have each range by using '1' for N1 and N2 in each v
# for example for v == 1
# N1: 00110001
# N2: 00000111
# and then N1 AND N2 -> 00000001
# which means this is the overrapped part
# finally you do this for all v and sum up.
# however this is O(N*L) which is too big -> N: min(num of unique v for N1, num of unique v for N2) -> only common v -> maximum 10**5
# L: 10**12

