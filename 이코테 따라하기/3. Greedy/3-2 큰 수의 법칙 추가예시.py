n, m, k = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

fisrt = numbers[-1]
second = numbers[-2]

count = (m / (k + 1)) * k # first가 반복되는 횟수
count += m % (k + 1) # m이 k+1로 안나눠질때 남은 first를 더해야 할 갯수

result = 0
result += count * fisrt
result += (m - count) * second

print(int(result))