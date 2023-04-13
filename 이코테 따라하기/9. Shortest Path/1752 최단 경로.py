import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize
v, e = map(int, input().split()) # 정점 개수 v, 간선 개수 e
k = int(input()) # 시작점 k

# 가중치 테이블 dp
dp = [INF] * (v + 1) 
q = []

# 각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for _ in range(v + 1)]

# 초기화
for _ in range(e):
    s, e, d = map(int, input().split())
    graph[s].append((d, e))


def dijkstra(start):
    # 가중치 테이블에서 시작 정점에 해당되는 가중치는 0으로 초기화
    dp[start] = 0
    heapq.heappush(q, (0, start))

    # 힙에 원소가 없을 때 까지 반복
    while q:
        distance, now = heapq.heappop(q)

        # 현재 테이블과 비교해서 거리가 더 크면 무시
        if dp[now] < distance: continue

        for dis, next in graph[now]:
            # 현재 정점까지의 거리 distance + 현재부터 다음 정점까지의 거리 dis
            # = 다음 정점까지의 거리
            next_dis = distance + dis

            # 다음 정점까지의 거리가 현재 보다 작으면 업데이트
            if next_dis < dp[next]: 
                dp[next] = next_dis
                # 다음 정점까지의 거리와 다음 정점에 대한 정보를 튜플로 최소 힙에 삽입
                heapq.heappush(q, (next_dis, next))
    

dijkstra(k)

for i in range(1, v + 1):
    print("INF" if dp[i] == INF else dp[i])