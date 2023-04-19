dp = [0] * 40

dp[0], dp[1] = 0, 1


for _ in range(int(input())):
    n = int(input())

    print(fib(n))

    
