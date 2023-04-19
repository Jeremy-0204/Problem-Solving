import sys, heapq
input = sys.stdin.readline

min_q = []
for _ in range(int(input())):
    n = int(input())

    # 0 받았는데 큐가 비어있을때
    if not min_q and n == 0: print(0)

    elif min_q and n == 0: print(heapq.heappop(min_q))

    else: heapq.heappush(min_q, n)