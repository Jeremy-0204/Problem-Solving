n = 1260
count = 0

coins = [500,100,50,10]

for coin in coins:
    count += n // coin # 몫을 갯수로
    n %= coin # 나머지를 다시 n으로

print(count)