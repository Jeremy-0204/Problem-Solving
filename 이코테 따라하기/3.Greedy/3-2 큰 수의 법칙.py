# n, m, k 를 입력받는다
# n개의 갯수, m은 총 더할 횟수, k는 연속될 수 있는 갯수
n, m, k = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

first = numbers[-1]
second = numbers[-2]
#print(numbers, first, second)

result = 0

for i in range(1, m + 1):
    if i % k == 0:
        result += second
    else: result += first
    #print(i, result)

print(result)