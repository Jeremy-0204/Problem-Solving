import sys
input = sys.stdin.readline
array = []

for _ in range(int(input())):
    array.append(list(map(int, input().split())))

array.sort(key = lambda x: (x[0], x[1]))

for i in array: print(i[0], i[1])