while True:
    array = sorted(list(map(int, input().split())))

    sum = array[0] ** 2 + array[1] ** 2
    if sum == 0: break
    elif sum == array[2] ** 2: print("right")
    else: print("wrong")