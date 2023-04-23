n, m = map(int, input().split())
array = list(map(int, input().split()))
mx = 0

for i in range(len(array)):
    for j in range(i + 1, len(array)):
        for k in range(j + 1, len(array)):
            sum = array[i] + array[j] + array[k]

            if sum <= m: mx = max(sum, mx)

print(mx)