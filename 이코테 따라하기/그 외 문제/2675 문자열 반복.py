n = int(input())
for _ in range(n):
    array = input().split()
    r, s = int(array[0]), array[1]
    result = ""
    for i in range(len(s)):
        result += s[i] * r
    print(result)