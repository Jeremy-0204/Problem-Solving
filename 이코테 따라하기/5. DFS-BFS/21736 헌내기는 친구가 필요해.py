from collections import deque

n, m = map(int, input().split())
graph = [list(input()) for _ in range(n)]
visited = [[0] * m for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(start, end):
    count = 0
    que = deque([(start, end)])
    visited[start][end] = 1

    while que:
        x, y = que.popleft()

        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y

            if nx < 0 or ny < 0 or nx >= n or ny >= m: continue

            if visited[nx][ny] == 0 and graph[nx][ny] != 'X':
                visited[nx][ny] = 1
                que.append((nx, ny))

                if graph[nx][ny] == 'P': 
                    count += 1
    
    if count == 0: print("TT")
    else: print(count)

flag = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 'I':
            flag = 1
            bfs(i, j)
            break
    if flag == 1: break