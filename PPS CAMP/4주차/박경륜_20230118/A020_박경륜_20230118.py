sum, max = 0, 0
for i in range(4):
    A, B = map(int, input().split())
    sum += B - A
    if max <= sum: max = sum

print(max)