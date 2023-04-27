# n = int(input())
# dp = [-1] * (n + 1)

# for i in range(3, n + 1):
#     if i % 3 == 0: 
#         if i > 3 : dp[i] = min(i // 3, dp[i-3] + 1)
#         else: dp[i] = i // 3
#     if i % 5 == 0: dp[i] = i // 5

#     elif (dp[i] % 5 != 0 and dp[i - 5] != -1) or (dp[i] % 3 != 0 and dp[i - 3] != -1): dp[i] = min(dp[i - i % 5] + 1, dp[i - i % 3] + 1)

# print(dp[n])


map = [0, 2, 4, 1, 3]
N = int(input())
i = map[N%5]
j = (N - 3*i) // 5
print(i+j if j >= 0 else -1)