from collections import deque

n, m = map(int, input().split())
graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

# 이동할 네 방향 정의 (상, 하, 좌, 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

# BFS 소스코드 구현
def bfs(x, y):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    que = deque()
    que.append((x, y))

    # 큐가 빌 때까지 반복
    while que:
        x, y = que.popleft()

        # 현재 위치에서 네 방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            # 미로 찾기 공간을 벗어난 경우는 무시
            if nx < 0 or ny < 0 or nx >= n or ny >= m: continue

            # 벽(0)인 경우도 무시
            if graph[nx][ny] == 0: continue

            # 해당 노드를 처음 방문하는 경우에만 최단 거리 기록
            if graph[nx][ny] == 1: # 처음 정상적으로 잘 방문한 곳의 숫자는 1일테니
                graph[nx][ny] = graph[x][y] + 1
                que.append((nx, ny))
    
    return graph[n-1][m-1]



# BFS를 수행한 결과 출력
print(bfs(0,0))