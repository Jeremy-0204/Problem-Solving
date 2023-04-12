N, K = map(int, input().split())
coins = []
count = 0

for i in range(N):
  coins.append(int(input()))

coins.sort(reverse=True)

for i in coins:
  if (K >= i):
    count += K // i
    K %= i
  else: pass

print(count)