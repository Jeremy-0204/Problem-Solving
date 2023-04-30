# n, m, b = map(int, input().split())
# land = []
# mndif = [[0 for _ in range(m)] for _ in range(n)]
# mxdif = [[0 for _ in range(m)] for _ in range(n)]

# for _ in range(n):
#     land.append(list(map(int, input().split())))

# mn, mx = 256, 0
# for i in range(n):
#     if mn >= min(land[i]): mn = min(land[i])
#     if mx <= max(land[i]): mx = max(land[i])

# # print(mn, mx)

# for i in range(n):
#     for j in range(m):
#         mndif[i][j] = land[i][j] - mn
#         mxdif[i][j] = mx - land[i][j]
# # print(mndif, mxdif)
# summn, summx = sum(map(sum, mndif)), sum(map(sum, mxdif))

# if summx < summn and land.count(mn) < b: print(summx, mx)
# else: print(summn * 2, mn)

import sys
n, m, b = map(int, sys.stdin.readline().split())
table = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
height = 0
ans = 1e9

for i in range(257):
    max = 0
    min = 0
    for j in range(n):
        for k in range(m):
            if table[j][k] < i:
                min += (i - table[j][k])
            else:
                max += (table[j][k] - i)
    inventory = max + b
    if inventory < min:
        continue
    time = 2 * max + min
    if time <= ans:
    # 시간이 같을 때는 높이가 높은 순으로 출력하라는 조건에 맞게
    # for i in range(257)은 항상 i가 오름차순으로 돌기 때문에
    # 시간이 같아도 최종적으로는 높이가 높은 순으로 나오게 된다
        ans = time
        height = i
print(ans, height)


# 빼는데 2초, 더하는데 1초
# Min 값을 찾고, Max 값을 찾음
# 각각 계산해보고 땅이 제일 높은걸 출력해야함
# 만약 Max 값이 제일 땅이 높아서 블럭을 쌓아야 하는데,
# Max 값보다 작은 값들의 합이 b보다 작으면 min 값으로 변경