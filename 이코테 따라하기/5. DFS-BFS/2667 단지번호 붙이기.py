import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [list(map(int, input().rstrip())) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

countlist = []

def bfs(start, end):
    que = deque([(start, end)])
    visited[start][end] = 1
    count = 1

    while que:
        x, y = que.popleft()

        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y

            if nx < 0 or ny < 0 or nx >= n or ny >= n: continue

            if graph[nx][ny] == 1 and visited[nx][ny] == 0:
                count += 1
                visited[nx][ny] = 1
                que.append((nx, ny))
    
    countlist.append(count)




for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and visited[i][j] == 0:
            bfs(i, j)

# print("GRAPH RESULT")
# for i in range(n):
#     print(graph[i])

# print("VISITED RESULT")
# for i in range(n):
#     print(visited[i])

# print("COUNT RESULT")
countlist.sort()
print(len(countlist))
for i in countlist: 
    print(i)