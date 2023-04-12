N = int(input())

num = list(map(int, input().split()))
num.sort()
time = 0

for i in range(len(num)):
    num[i] += time
    time = num[i]

print(sum(num))