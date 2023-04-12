for _ in range(int(input())):
    num = int(input())
    stop = 0

    while num:
        stop = stop * 2 + 1
        num -= 1
    print(stop)