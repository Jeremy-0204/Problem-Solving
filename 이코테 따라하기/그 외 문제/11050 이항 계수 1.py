n, k = map(int, input().split())

def bino_coef(n, k):

    if k > n: return 0

    dp = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]

    def choose(times, get):
        if times == n: return get == k

        if dp[times][get] != -1: return dp[times][get]

        dp[times][get] = choose(times + 1, get) + choose(times + 1, get + 1)
        return dp[times][get]

    return(choose(0, 0)) 

print(bino_coef(n, k))