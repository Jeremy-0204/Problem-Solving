N = int(input())

dp = dict()
dp[0] = 0

for i in range(1, N+1):
    if i >= 7:
        dp[i] = min(dp[i-1], dp[i-2], dp[i-5], dp[i-7]) + 1
    elif i >= 5:
        dp[i] = min(dp[i-1], dp[i-2], dp[i-5]) + 1
    elif i >= 2:
        dp[i] = min(dp[i-1], dp[i-2]) + 1
    else:
        dp[i] = dp[i-1] + 1

print(dp[N])