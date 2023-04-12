n, m = map(int, input().split())

# n * m 만큼의 방문한 위치용 리스트 생성
d = [[0] * m for _ in range((n))]
x, y, dir = map(int, input().split())
d[x][y] = 1

array = []
for i in range(n):
    array.append(list(map(int, input().split())))

# 북, 동, 남, 서 -> dir 값에 따라 바뀜
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global dir
    dir -= 1
    if dir == -1: dir = 3 # dir 다시 초기화

count = 1
turn_count = 0 # 몇번 회전했는지, 4번하면 더이상 갈곳이 없는 것임

while True:
    turn_left()

    nx = x + dx[dir]
    ny = y + dy[dir]

    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_count = 0
        continue

    else: turn_count += 1 # 회전했는데 앞이 바다거나 이미 가본곳

    if turn_count == 4: # 4번 다 돌아서 이제 갈 곳 없는 경우
        nx = x - dx[dir]
        ny = y = dy[dir]
        
        # 뒤로 갈 수 있음 이동
        if array[nx][ny] == 0: 
            x = nx
            y = ny
        
        else: break
        turn_count = 0
    
print(count)