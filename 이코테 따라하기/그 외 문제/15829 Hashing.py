n = int(input())
array = list(input())

sum = 0
for i in range (len(array)):
    num = ord(array[i]) - 96
    sum += num * (31 ** i)

print(sum  % 1234567891)