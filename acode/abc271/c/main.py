import sys
sys.setrecursionlimit(500005)
#import pypyjit # this is for solving slow issue for pypy when using recursion but python will not need this (test will fail but submit works)
#pypyjit.set_param('max_unroll_recursion=-1')

N = int(input())
a = list(map(int, input().split()))

a.sort()

A = [a[0]]
B = []

#print(a)

for k in range(1, N):
    if a[k-1] != a[k]:
        A.append(a[k])
    else:
        B.append(a[k])

A.extend(B)

#print(A)

ans = 0
ind = 0

#for i in range(len(a)):
#while True:
for j in range(N):
    #print(a)
    if ind > len(A)-1:
        break
    if A[ind] == ans+1:
        ans += 1
        ind += 1
        continue
    else:
        #if ind+1 > len(a)-1 or a[-1] == a[ind+1] or a[-2] == a[ind+1]:
        if ind-1 >= len(A)-2:
            break
        #A = A[:len(A)-2]
        A.pop()
        A.pop()
        ans += 1

print(ans)


