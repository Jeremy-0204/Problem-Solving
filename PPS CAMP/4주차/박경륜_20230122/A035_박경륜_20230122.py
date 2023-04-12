for _ in range(int(input())):
    cal = list(input().split())
    cal[0] = float(cal[0])
    
    for i in range(1, len(cal)):
        if cal[i] == '@': cal[0] *= 3
        elif cal[i] == '%': cal[0] +=5
        elif cal[i] == '#': cal[0] -= 7
    
    print(f'{cal[0]:.2f}')