N = int(input())

mp = [[0 for i in range(5)] for j in range(10**5+1)]

for i in range(N):
    T, X, A = list(map(int, input().split()))
    mp[T][X] = A

# dp[t][x] t 秒後の位置xの最大値
# もらうDP

INF = 100100100100

dp = [[-INF for i in range(5)] for j in range(10**5+1)] # INF is important different from 0
# using INF make it possible that it will disable unless you put data in dp[][]

dp[0][0] = 0

for t in range(1, 10**5+1):
    for x in range(5):
        if x == 0:
            dp[t][x] = max(dp[t][x], dp[t-1][x]+mp[t][x], dp[t-1][x+1]+mp[t][x])
        elif x == 4:
            dp[t][x] = max(dp[t][x], dp[t-1][x-1]+mp[t][x], dp[t-1][x]+mp[t][x])
        else:
            dp[t][x] = max(dp[t][x], dp[t-1][x-1]+mp[t][x], dp[t-1][x]+mp[t][x], dp[t-1][x+1]+mp[t][x])


        '''
        if x == 0:
            if t < 2:
                dp[t][x] = max(dp[t][x], dp[t-1][x]+mp[t][x])
            else:
                dp[t][x] = max(dp[t][x], dp[t-1][x]+mp[t][x], dp[t-1][x+1]+mp[t][x])
        elif x == 4:
            if t >= 4:
                dp[t][x] = max(dp[t][x], dp[t-1][x-1]+mp[t][x], dp[t-1][x]+mp[t][x])
            else:
                continue
        else:
            if t >= 4:
                dp[t][x] = max(dp[t][x], dp[t-1][x-1]+mp[t][x], dp[t-1][x]+mp[t][x], dp[t-1][x+1]+mp[t][x])
            elif x < t:
                dp[t][x] = max(dp[t][x], dp[t-1][x-1]+mp[t][x], dp[t-1][x]+mp[t][x], dp[t-1][x+1]+mp[t][x])
            elif x == t:
                dp[t][x] = max(dp[t][x], dp[t-1][x-1]+mp[t][x], dp[t-1][x]+mp[t][x])
            elif x == t+1:
                dp[t][x] = max(dp[t][x], dp[t-1][x-1]+mp[t][x])
        '''

#print(dp[:5])
ans = 0
for a in range(5):
    ans = max(ans, dp[-1][a])

print(ans)

