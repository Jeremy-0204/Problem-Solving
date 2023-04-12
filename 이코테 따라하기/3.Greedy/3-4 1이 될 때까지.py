# n을 1로 빼거나 k로 나누는 최소 횟수
# 그냥 n을 k로 나눠질때까지 뺀 다음에 확 k로 나눠버리기
n, k = map(int, input().split())
count = 0

while (n % k == 0):
    n -= 1
    count +=1

print(count+1)