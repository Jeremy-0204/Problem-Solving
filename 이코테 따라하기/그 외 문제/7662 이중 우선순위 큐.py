# from collections import deque
# import sys

# input = sys.stdin.readline
# n = int(input())

# for _ in range(n):
#     que = deque()

#     m = int(input())


#     for _ in range(m):
#         commands = list(input().split())

#         if commands[0] == "I": 
#             que.append(commands[1])
#             que = deque(sorted(map(int, list(que))))

#         elif commands[0] == "D" and commands[1] == "1": 
#             if len(que) > 0: que.pop()
#         elif commands[0] == "D" and commands[1] == "-1": 
#             if len(que) > 0: que.popleft()

#     result = list(que)

#     if len(result) == 0: print("EMPTY")
#     else: print(max(result), min(result))


# 정답 코드

import sys, heapq
input = sys.stdin.readline

input = sys.stdin.readline
n = int(input())

for _ in range(n):
    maxq, minq = [], []
    m = int(input())
    visited = [0] * m


    for i in range(m):
        a, b = input().split()

        if a == "I": 
            heapq.heappush(maxq, (-int(b), i))
            heapq.heappush(minq, (int(b), i))
        
        else: # b=='D'
            if b=="-1":
                while minq and visited[minq[0][1]]:
                    heapq.heappop(minq)
                if minq:
                    visited[minq[0][1]] = 1
                    heapq.heappop(minq)
            else: #b=='1' 최대힙
                while maxq and visited[maxq[0][1]]:
                    heapq.heappop(maxq)
                if maxq:
                    visited[maxq[0][1]] = 1
                    heapq.heappop(maxq)
        
        # print(minq, maxq, visited)

    while maxq and visited[maxq[0][1]]:
        heapq.heappop(maxq)
    while minq and visited[minq[0][1]]:
        heapq.heappop(minq)
    if not minq or not maxq:
        print("EMPTY")
    else:
        print("%d %d" %(-maxq[0][0], minq[0][0]))