n = int(input())
for i in range(1, n+1):
    for k in range(n-1-i, -1, -1):
        print(" ", end='')
    for j in range(1, i+1):
        print("*", end='')
    print()
    