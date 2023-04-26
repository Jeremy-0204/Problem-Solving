array = []
for _ in range(int(input())):
    array.append(list(map(int, input().split())))

# array.sort(key = lambda x: (x[0], x[1]))

for i in range(len(array)):
    count = 0
    for j in range(len(array)):
        if array[i][0] < array[j][0] and array[i][1] < array[j][1]: count += 1
    print(count+1)