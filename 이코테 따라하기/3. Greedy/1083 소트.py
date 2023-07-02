import sys
input = sys.stdin.readline
# N = int(input())
# nlist = list(map(int, input().split()))
# S = int(input())

# for i in range(0, N - 1, 2):
#     if i <= N and i + 1 <= N and S > 0:
#         nlist[i], nlist[i + 1] = nlist[i + 1], nlist[i]
#         S -= 1

# for i in nlist:
#     print(i, end=' ')

n, nums = int(input()), list(map(int, input().split()))
s = int(input())

for i in range(n):
    # 탐색
    max_num = max(nums[i: min(n, i + s + 1)])
    idx = nums.index(max_num)
    # 교환
    for j in range(idx, i, -1):
        nums[j], nums[j - 1] = nums[j - 1], nums[j]
    # 후처리
    s -= (idx - i)
    if s <= 0: break

print(*nums)