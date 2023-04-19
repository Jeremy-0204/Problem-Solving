import sys
from collections import deque

input = sys.stdin.readline

def bfs(start, end):
    que = deque([(start, end)])
    visited[start][end] = 1

    while que:
        x, y = que.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if nx < 0 or nx >= len(graph) or ny < 0 or ny >= len(graph[0]): continue
            
            if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                que.append((nx, ny))
                visited[nx][ny] = 1



dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for _ in range(int(input())):
    m, n, k = map(int, input().split())

    count = 0

    graph = [[0 for _ in range(m)] for __ in range(n)]
    visited = [[0 for _ in range(m)] for __ in range(n)]

    for i in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1
    
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1 and visited[i][j] == 0: 
                bfs(i, j)
                count += 1
    
    # for i in range(n):
    #     print(graph[i])

    # print()

    # for i in range(n):
    #     print(visited[i])

    print(count)


    