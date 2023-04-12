string = input()
for i in range(1, len(string)+1):
    if i % 10 == 0:    print(string[i-1])
    else:   print(string[i-1], end="")