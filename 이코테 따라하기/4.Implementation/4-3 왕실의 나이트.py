# 체스판 위치 받아서 말이 이동할 수 있는 경우의 수 세기

now = input()
row = int(now[1])
column = int(ord(now[0])) - int(ord('a')) + 1 # 알파벳을 숫자로 (a -> 1)

moves = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]

result = 0
for move in moves:
    new_row = row + move[0]
    new_col = column + move[1]

    if new_row >= 1 and new_row <= 8 and new_col >=1 and new_col <= 8:
        result += 1

print(result)