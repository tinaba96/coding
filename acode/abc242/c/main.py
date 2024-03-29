import sys

sys.setrecursionlimit(10**6)

N = int(input())

cnt = 0

mp = [[-1 for i in range(10)] for j in range(10000)]

def memo(l, n, f):
    # it is not good to have global variable since it becomaes hard to reuse
    global cnt

    if l == N-1:
        cnt += 1
        # this is same as mp[N-1][f]? this must be wrong
        mp[l][f] = cnt
    elif l == N:
        return

    if mp[l][n] != -1:
        if N-l > l:
            l += l
            #l is the integer u passed and not the rest
            cnt += mp[l][n]
        
    if n != 1 and n != 9:
        memo(l+1, n-1, f)
        memo(l+1, n, f)
        memo(l+1, n+1, f)
    elif n == 1:
        memo(l+1, n, f)
        memo(l+1, n+1, f)
    elif n == 9:
        memo(l+1, n-1, f)
        memo(l+1, n, f)

ans = 0

for i in range(1, 10):
    memo(0, i, i)

print(cnt)

# this is not an approach like dp or memorization
# for this approach, if you try to count part by part, you need to multiply not adding -> although start integer are many, the length of each case should be same in order to do it part by part 
# --->> multiply is not going to work. since 1 and 10 are not allowed, it cannot be simply done by multiplying (if you multiply, you can only get tyhe answer that can be got by multiplying and Prime number cannot be got bby multiplying) -> part by part is not going to work since those are not independent
# and if you want find the memo that had maximum length, u need another O(N) to find it
# but actually u cannot do part by part since you cannot know the first integer to start with. u have basically 3 differnt integer that has different memo length.
# this leads to the solution shown in video tutorial
# this approach does not use "漸化式", u should use the idea of "漸化式" in order to solve this efficiently

# if you want to do it part by part and do multiplying, you need to know the last interger. You need to knoow the number of cases that ends with same integer (ex. 100 cases which end with 3) which is almost same as "総当たり"
