from sys import stdin

N = int(stdin.readline())
price = list(map(int, stdin.readline().split()))
total = int(stdin.readline())

dp = dict()

for i in range(N-1, -1, -1):
    x = price[i]
    print(f"X = {x}")
    for j in range(x, total+1):
        print(f"j = {j}")