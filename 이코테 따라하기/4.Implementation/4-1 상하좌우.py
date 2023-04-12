# n x n 평면 위 (1,1)에서 시작하여 명령어대로 움직인 후의 좌표 출력

n = int(input())
x, y = 1, 1
commands = input().split()

moves = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for command in commands:
    for i in range(len(moves)):
        if command == moves[i]:
            nx = x + dx[i]
            ny = y + dy[i]

    if nx < 1 or ny < 1 or nx > n or ny > n: continue

    x, y = nx, ny

print(x, y)
    