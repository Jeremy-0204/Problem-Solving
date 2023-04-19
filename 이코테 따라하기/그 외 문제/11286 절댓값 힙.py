import sys, heapq
input = sys.stdin.readline

n = int(input())
abs_heap = []

for _ in range(n):
    num = int(input())

    if num != 0: heapq.heappush(abs_heap, (abs(num),num))

    else:
        if len(abs_heap) == 0: print(0)
        else: print(heapq.heappop(abs_heap)[1])