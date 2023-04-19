n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

print(graph)


# 전체 종이가 같은 숫자면 그만

# 숫자가 다르면 종이를 9등분 함
# 어떻게 9등분을 할까? 이중반복문으로 

for i in range(0, n):
    for j in range(0, n):
        