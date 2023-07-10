import sys
from collections import deque
input = sys.stdin.readline

def bfs():
    que = deque()
    que.append(1)
    visited[1] = True

    while que:
        current = que.popleft()
        for i in range(1, 7):
            next_move = current + i

            if 1 <= next_move <= 100 and not visited[next_move]:
                if next_move in snake.keys():
                    next_move = snake[next_move]
                if next_move in ladder.keys():
                    next_move = ladder[next_move]
                if not visited[next_move]:
                    que.append(next_move)
                    visited[next_move] = True
                    board_cnt[next_move] = board_cnt[current] + 1
            


n, m = map(int, input().split())
board_cnt = [0] * 101
visited = [False] * 101

ladder = dict()
snake = dict()

for _ in range(n):
    x, y = map(int, input().split())
    ladder[x] = y

for _ in range(m):
    x, y = map(int, input().split())
    snake[x] = y

bfs()
print(board_cnt[100])