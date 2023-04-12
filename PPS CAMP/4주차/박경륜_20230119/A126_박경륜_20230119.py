N = int(input())
count = 0
for i in range(1, N+1):
    numstr = list(map(int, str(i)))

    if i < 100: count += 1
    elif numstr[0] - numstr[1] == numstr[1] - numstr[2]: count += 1

print(count)