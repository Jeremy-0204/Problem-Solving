from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
que = deque()

for _ in range(n):
    commands = list(input().split())

    if commands[0] == "push":
        que.append(int(commands[1]))

    elif commands[0] == "pop":
        if len(que) > 0: print(que.popleft())
        else: print(-1)
    
    elif commands[0] == "front":
        if len(que) > 0: print(que[0])
        else: print(-1)

    elif commands[0] == "back":
        if len(que) > 0: print(que[-1])
        else: print(-1)

    elif commands[0] == "size":
        print(len(que))

    elif commands[0] == "empty":
        if len(que) > 0: print(0)
        else: print(1)