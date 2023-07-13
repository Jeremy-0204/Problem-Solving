import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = []
visited = [[False] * m for _ in range(n)]
answer = 0

for _ in range(n):
    board.append(list(map(int, input().split())))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(x, y, msum, depth):
    global answer

    if depth == 3:
        answer = max(answer, msum)
        return
    
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx >= n or ny >= m or visited[nx][ny]: continue

            if depth == 1:
                visited[nx][ny] = True
                dfs(x, y, msum + board[nx][ny], depth + 1)
                visited[nx][ny] = False

            visited[nx][ny] = True
            dfs(nx, ny, msum + board[nx][ny], depth + 1)
            visited[nx][ny] = False


for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i, j, board[i][j], 0)
        visited[i][j] = False

print(answer)