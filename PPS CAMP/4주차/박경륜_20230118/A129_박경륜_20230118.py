def answer(num):
    dp = dict()
    dp[0], dp[1], dp[2] = 1, 2, 4

    for i in range(3, num):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    print(dp[num-1])

for _ in range(int(input())):
    answer(int(input()))