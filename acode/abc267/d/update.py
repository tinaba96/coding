N, M = list(map(int, input().split()))
A = list(map(int, input().split()))

# dp[i][m] iまで決めた上で、選んだ数mの時の最大ち

INF = 100100100100  # this is too small

dp = [[-INF for i in range(M+2)] for j in range(N+2)]

dp[0][0] = 0

for x in range(N):
    for t in range(M+1):
        dp[x+1][t+1] = max(dp[x+1][t+1], dp[x][t]+((t+1)*A[x]))
        dp[x+1][t] = max(dp[x+1][t], dp[x][t])

ans = 0 # this is too small
for a in range(N+1):
    ans = max(ans, dp[a][-2])

print(ans)


