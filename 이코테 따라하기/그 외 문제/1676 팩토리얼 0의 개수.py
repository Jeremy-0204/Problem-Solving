n = int(input())
fact = 1
for i in range(n, 1, -1):
    fact *= i

array = list(str(fact))[::-1]

count = 0
for i in array:
    if i == "0": count += 1
    else: break

print(count)