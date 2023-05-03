import sys
input = sys.stdin.readline

n, m = list(map(int, input().split()))
num_li = list(map(int, input().split()))

# 이전까지의 합을 구해서 빼는 방식으로 진행
sum_li = [0]
sum_num = 0
for i in num_li:
    sum_num += i
    sum_li.append(sum_num)

for i in range(m):
    a, b = map(int, input().split())
    print(sum_li[b] - sum_li[a-1])