# 00:00:00 ~ N:59:59 까지 3이 하나라도 포함되어 있는 개수
# 24, 60, 60 : 3중 반복문

n = int(input())
count = 0

for i in range(n + 1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k): count += 1

print(count)