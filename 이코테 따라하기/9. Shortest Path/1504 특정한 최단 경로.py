# sys, heapq import 하기
import sys
import heapq

# 입력 받을 준비
input = sys.stdin.readline
INF = sys.maxsize
v, e = map(int, input().split())

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 그래프 생성
# ex) graph[1] = (3, 2) -> 1부터 2까지 거리는 3이다.
graph = [[] for _ in range(v + 1)]

# 그래프 초기화 해주기
for i in range(e):
    a, b, c = map(int, input().split()) # a 시작, b 도착, c 거리
    # 방향이 없는 그래프이므로 양 노드에 대해 생성해준다
    graph[a].append((c, b))
    graph[b].append((c, a))

# 다익스트라 함수 생성
def dijkstra(start):
    # 거리 테이블 dp -> dp[노드] = 거리
    # q에는 튜플 형식으로 (거리, 시작노드) 정보가 들어감
    dp = [INF] * (v + 1) 
    q = []

    # 가중치 테이블에서 시작 노드에 해당되는 거리는 0으로 초기화
    dp[start] = 0
    heapq.heappush(q, (0, start))

    # 힙에 원소가 없을때까지 반복
    while q:
        dist, now = heapq.heappop(q)

        # 현재 테이블과 비교해서 거리가 더 크면 무시
        if dp[now] < dist: continue

        for dis, next in graph[now]:
            # 지금 노드까지 거리 + 다음 노드까지 거리 = 다음 노드까지 거리
            next_dist = dist + dis

            # 다음 노드까지의 거리가 현재보다 작으면 업데이트
            if next_dist < dp[next]:
                dp[next] = next_dist
                # 다음 노드까지 거리랑 노드 정보를 튜플로 최소힙에 삽입
                heapq.heappush(q, (next_dist, next))
    
    return dp # 반환은 최단 거리 배열

v1, v2 = map(int, input().split())

# 출발점 start 노드가 각각 1, v1, v2 일때의 거리 배열들
original_distance = dijkstra(1)
v1_distance = dijkstra(v1)
v2_distance = dijkstra(v2)

v1_path = original_distance[v1] + v1_distance[v2] + v2_distance[v]
v2_path = original_distance[v2] + v2_distance[v1] + v1_distance[v]

result = min(v1_path, v2_path)
print(result if result < INF else -1)
