from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = [[0 for _ in range(n)] for __ in range(n)] 
for i in range(n):
    graph[i] = list(map(str, input())) # 색 그래프
visited = [[0 for _ in range(n)] for __ in range(n)] # 방문 여부 그래프

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(start, end, graph):
    visited[start][end] == 1 # 첫 시작이니 방문 처리
    que = deque([(start, end)]) # 좌표를 원소로 하는 deque 생성

    # 다음으로 방문할 정보는 que에 담게 되어 있음

    while que:
        x, y = que.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            # 새로 좌표를 계산했을때 그래프 범위 안에 있는 경우만
            if nx < 0 or ny < 0 or nx >= n or ny >= n: continue

            # 아직 방문도 안한 상태이면서 동시에 현재 위치 알파벳이랑 같을때만 이동
            if visited[nx][ny] == 0 and graph[nx][ny] == graph[x][y]:
                que.append((nx, ny))
                visited[nx][ny] = 1 # 방문 처리 해버림


normal = 0
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0: # 얘가 그럼 다시 다른 색 bfs 돌려주는 거임
            bfs(i, j, graph) # 그럼 처음 0,0 부터 같은 색은 다 1로 바뀌겠지?
            normal += 1

# 다시 초기화
abnormal = 0
visited = [[0 for _ in range(n)] for __ in range(n)] # 방문 여부 그래프

# 적록색약 처리
for i in range(n):
    for j in range(n):
        if graph[i][j] == 'R':
            graph[i][j] = 'G'

# 적록색약 bfs 돌리기
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0:
            bfs(i, j, graph)
            abnormal += 1

print(normal, abnormal)