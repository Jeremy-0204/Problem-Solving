n = int(input())

for i in range(1, n + 1):
    num = i + sum(map(int, str(i)))
    if num == n: 
        print(i)
        break
    if i == n: print(0)