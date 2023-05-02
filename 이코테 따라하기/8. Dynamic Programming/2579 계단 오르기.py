import sys
input = sys.stdin.readline

n = int(input())
num = [0]
dp = [0] * (n + 1)

for _ in range(n):
    num.append(int(input()))

if len(num) <= 2: # 계단이 2개 이하일땐 그냥 다 더해서 출력
    print(sum(num))

else: # 계단이 3개 이상일 때
    dp[0], dp[1], dp[2] = 0, num[1], num[2] + num[1]

    for i in range(3, n + 1):
        dp[i] = max(dp[i - 2] + num[i], dp[i - 3] + num[i - 1] + num[i])

    print(dp[n])