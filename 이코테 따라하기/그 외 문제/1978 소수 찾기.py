n = int(input())
array = list(map(int, input().split()))
MAX = max(array) + 1

sieve = [True] * MAX
sieve[0], sieve[1] = False, False

mid = int(MAX ** 0.5)

for i in range(2, mid + 1):
    if sieve[i] == True:
        for j in range(i+i, MAX, i): sieve[j] = False
result = [i for i in range(len(sieve)) if sieve[i] == True]

count = 0
for i in array:
    if i in result: count += 1

print(count)