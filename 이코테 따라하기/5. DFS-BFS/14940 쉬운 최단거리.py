# n, m 크기의 방문여부를 나타내는 새로운 배열 생성
# 모두 방문하지 않음 곳임으로 -1로 초기화

# 2는 시작지점임으로 0으로 초기화
# 상하좌우로 움직이면서 1씩 증가
# 0을 만나면 변동 없음
# 방문할때마다 visited 배열은 true를 뜻하는 1로 변경

# 마지막에 visited가 -1인 곳들은 원본 배열도 -1로 변경

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

visited = [[-1 for _ in range(m)] for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(start, end):
    visited[start][end] = 1
    graph[start][end] = 0

    que = deque([(start, end)])

    while que:
        x, y = que.popleft()

        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y

            # 범위 체크
            if nx < 0 or ny < 0 or nx >= n or ny >= m: continue

            if visited[nx][ny] == -1 and graph[nx][ny] != 0:
                visited[nx][ny] = 1
                que.append((nx, ny))
                graph[nx][ny] = graph[x][y] + 1

flag = 0
for i in range(n):
    for j in range(m):
        if graph[i][j] == 2:
            bfs(i, j)
            flag = 1
            break
    if flag == 1: break    

for i in range(n):
    for j in range(m):
        if visited[i][j] == -1 and graph[i][j] > 0: graph[i][j] = -1

for i in range(n):
    for j in range(m):
        print(graph[i][j], end = ' ')
    print()

# print("GRAPH RESULT")
# for i in range(n):
#     print(graph[i])

# print("VISITED RESULT")
# for i in range(n):
#     print(visited[i])