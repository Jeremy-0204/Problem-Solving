import math

def calculate_winning_probability(p, i, j, n):
    winning_prob = 0
    for k in range(n-i-j, n-j):
        num_combinations = math.comb(n-j, k)
        winning_prob += num_combinations * (p ** (i+k)) * ((1-p) ** (n-i-j-k))
    return winning_prob


p = 0.6
i = 2
j = 1
n = 5

winning_prob = calculate_winning_probability(p, i, j, n)
print(winning_prob)
