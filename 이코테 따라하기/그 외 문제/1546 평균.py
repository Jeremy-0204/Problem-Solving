n = int(input())
array = sorted(list(map(int, input().split())), reverse = True)
max = array[0]

for i in range(len(array)):
    array[i] = array[i] / max * 100

print(sum(array) / n)