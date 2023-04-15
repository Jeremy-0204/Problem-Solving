array = []
for _ in range(9):
    array.append(int(input()))

max = sorted(array)[-1]

for i in range(9):
    if array[i] == max: 
        print(max)
        print(i+1)