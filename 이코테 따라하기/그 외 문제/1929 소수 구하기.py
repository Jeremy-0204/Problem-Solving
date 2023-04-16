m, n = map(int, input().split())
MAX = 1000000
sieve = [True] * MAX
sieve[0], sieve[1] = False, False

mid = int(MAX ** 0.5)

for i in range(2, mid + 1):
    if sieve[i] == True:
        for j in range(i+i, MAX, i): sieve[j] = False

result = [i for i in range(m, n+1) if sieve[i] == True]

for i in result: print(i)