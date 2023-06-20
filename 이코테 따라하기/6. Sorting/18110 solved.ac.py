import sys
from collections import deque

def osaoip(num): return round(num+10**(-len(str(num))-1))

input = sys.stdin.readline
list = []

n = int(input())
trim = n * 30 / 100
rtrim = osaoip(trim)

for _ in range(n):
    list.append(int(input()))

que = deque(sorted(list))

for _ in range(int(rtrim / 2)):
    que.popleft()
    que.pop()

ans = osaoip(sum(que) / len(que))
print(ans)
