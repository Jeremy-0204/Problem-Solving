n, m = map(int,input().split())

graph = []

for _ in range(n + m):
    x, y = map(int, input().split())
    graph.append((x,y))

print(graph)

# 시작은 (1,1)

# x를 만나면 y로 이동

# 주사위를 몇개 던져야 최대가 될지를 어떻게 구하지?

# 