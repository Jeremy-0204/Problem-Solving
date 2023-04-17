from collections import deque

def dfs(graph, v, visited, ):
    visited[v] = True
    print(v, end = ' ')
    
    for i in graph[v]:
        if not visited[i]: dfs(graph, i, visited)

def bfs(graph, start, visited):
    que = deque([start])
    visited[start] = True

    while que:
        v = que.popleft()
        print(v, end = ' ')

        for i in graph[v]:
            if not visited[i]:
                que.append(i)
                visited[i] = True


n, m, v = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(m)]

graph = [[] for _ in range(n + 1)]

for i in array:
    graph[i[0]].append(i[1])
    graph[i[1]].append(i[0])

for i in range(1, n + 1):
        graph[i].sort()
  
visited_d = [False] * (n + 1)
visited_b = [False] * (n + 1)

dfs(graph, v, visited_d)
print()
bfs(graph, v, visited_b)