n, m = map(int, input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

# dfs로 특정한 노드를 방문한 뒤에 연결된 모든 노드들까지 방문
def dfs(x, y):
    # 주어진 범위를 벗어나면 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m: return False

    # 현재 노드를 아직 방문하지 않았다면
    if graph[x][y] == 0:
        graph[x][y] = 1
        
        # 상, 하, 좌, 우 차례로 모두 dfs 재귀적으로 호출
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)

        return True
    return False



# (0,0) 부터 (n,m) 까지 차례로 dfs 수행
# True 반환되면 모든 0들이 1로 변환된거임
# 그럴때마다 return 1개 추가

result = 0
for i in range(n):
    for j in range(m):
        if dfs(i,j) == True: result += 1

print(result)