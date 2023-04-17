from collections import deque
m, n = map(int, input().split())
graph = []
x, y = 0, 0
for _ in range(n):
    graph.append(list(map(int, input().split())))

# 이동할 네 방향 (상,하,좌,우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    que = deque()

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 1:
                que.append((i, j))

    while que:
        x, y = que.popleft()

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]

            # 그래프 범위 벗어나면 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m: continue

            # 토마토가 없어도 무시
            if graph[nx][ny] == -1: continue

            # 아직 안익은 경우
            if graph[nx][ny] == 0:
                graph[nx][ny] = graph[x][y] + 1
                que.append((nx, ny))
        
        # for i in range(n):
        #     print(graph[i])
        # print()


bfs()

result = max(max(graph)) - 1
for i in range(n):
    for j in range(m):
        if graph[i][j] == 0: 
            result = -1
            break
    if result == -1: break

print(result)

# 1이 어디있는지 찾아야 할까?

# 찾으면 상하좌우로 bfs

# bfs는 deque로 구현
# 현재 위치를 매개변수로 입력받아서 큐에 넣는다
# 큐에 들어있는 애들은 방문해야 할 좌표
# 일단 시작점을 큐에 넣음

# 큐가 빌때까지
# 새로운 좌표 확인
# 만약 0보다 작거나, n,m 보다 크거나, -1인 경우는 pass
# 0인 경우면 1로 만들고 days += 1