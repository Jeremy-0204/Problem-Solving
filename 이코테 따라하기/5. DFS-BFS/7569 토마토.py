import sys
from collections import deque
m,n,h = map(int,input().split()) # mn크기, h상자수
graph = []
queue = deque([])
 
for i in range(h):
    tmp = []
    for j in range(n):
        tmp.append(list(map(int,sys.stdin.readline().split())))
        for k in range(m):
            if tmp[j][k]==1:
                queue.append([i,j,k])
    graph.append(tmp)
    
dx = [-1,1,0,0,0,0]
dy = [0,0,1,-1,0,0]
dz = [0,0,0,0,1,-1]
while(queue):
    x,y,z = queue.popleft()
    
    for i in range(6):
        a = x+dx[i]
        b = y+dy[i]
        c = z+dz[i]
        if 0<=a<h and 0<=b<n and 0<=c<m and graph[a][b][c]==0:
            queue.append([a,b,c])
            graph[a][b][c] = graph[x][y][z]+1
            
day = 0
for i in graph:
    for j in i:
        for k in j:
            if k==0:
                print(-1)
                exit(0)
        day = max(day,max(j))
print(day-1)

# from collections import deque
# m, n, h = map(int, input().split())
# graph = [[list(map(int, input().split())) for _ in range(n)] for _ in range(h)]

# x, y, z = 0, 0, 0

# # 이동할 네 방향 (상,하,좌,우)
# dx = [0, 0, 0, 0, -1, 1]
# dy = [0, 0, -1, 1, 0, 0]
# dz = [-1, 1, 0, 0, 0, 0]

# def bfs():
#     que = deque()

#     for i in range(h):
#         for j in range(n):
#             for k in range(m):
#                 if graph[i][j][k] == 1:
#                     que.append((i, j, k))

#     while que:
#         x, y, z = que.popleft()

#         for i in range(6):
#             nx, ny, nz = x + dx[i], y + dy[i], z + dz[i]

#             # 그래프 범위 벗어나면 무시
#             if nx < 0 or ny < 0 or nz < 0 or nx >= h or ny >= n or nz >= m: continue

#             # 토마토가 없어도 무시
#             if graph[nx][ny][nz] == -1: continue

#             # 아직 안익은 경우
#             if graph[nx][ny][nz] == 0:
#                 graph[nx][ny][nz] = graph[x][y][z] + 1
#                 que.append((nx, ny, nz))

# bfs()
# # print(graph)
# result = 0
# for i in range(h):
#     for j in range(n):
#         for k in range(m):
#             if graph[i][j][k] == 0:
#                 result = -1
#                 break

#         if result == -1: break
    
#     if result == -1: break

# if result == -1: print(result)
# else: print(max(max(map(max, graph))) - 1)

# # # 모든 토마토가 다 익은 경우
# # if all(0 not in row for row in graph): print(max(max(map(max, graph))) - 1)

# # # 일부 토마토가 익지 않은 경우
# # else: print(-1)


# # 1이 어디있는지 찾아야 할까?

# # 찾으면 상하좌우로 bfs

# # bfs는 deque로 구현
# # 현재 위치를 매개변수로 입력받아서 큐에 넣는다
# # 큐에 들어있는 애들은 방문해야 할 좌표
# # 일단 시작점을 큐에 넣음

# # 큐가 빌때까지
# # 새로운 좌표 확인
# # 만약 0보다 작거나, n,m 보다 크거나, -1인 경우는 pass
# # 0인 경우면 1로 만들고 days += 1
