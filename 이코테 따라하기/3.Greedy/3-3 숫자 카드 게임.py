# n X m 행렬 중 각 행별로 가장 작은 수들을 뽑는다.
# 가장 작은 수들 중 가장 큰 수를 골라야 함

n, m = map(int, input().split())
result = 0

for i in range (n):
    data = list(map(int, input().split()))
    min_num = min(data)
    result = max(result, min_num)

print(result)