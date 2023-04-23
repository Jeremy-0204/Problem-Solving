def result(m, n, x, y):
    while x <= m * n:
        if (x - y) % n == 0: return x
        x += m
    return -1

for _ in range(int(input())):
    m, n, x, y = map(int, input().split())
    print(result(m, n, x, y))