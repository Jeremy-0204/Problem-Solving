import sys
input = sys.stdin.readline

n, m = map(int, input().split())
d = dict()
for _ in range(n):
    a, b = input().split()
    d[a] = b

for _ in range(m):
    find = input().split("\n")

    print(d[find[0]])