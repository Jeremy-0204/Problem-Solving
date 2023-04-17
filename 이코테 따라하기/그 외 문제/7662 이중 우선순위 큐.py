from collections import deque
import sys

input = sys.stdin.readline
n = int(input())

for _ in range(n):
    que = deque()

    m = int(input())


    for _ in range(m):
        commands = list(input().split())

        if commands[0] == "I": 
            que.append(commands[1])
            que = deque(sorted(map(int, list(que))))

        elif commands[0] == "D" and commands[1] == "1": 
            if len(que) > 0: que.pop()
        elif commands[0] == "D" and commands[1] == "-1": 
            if len(que) > 0: que.popleft()

    result = list(que)

    if len(result) == 0: print("EMPTY")
    else: print(max(result), min(result))