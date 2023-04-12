for _ in range(int(input())):
    a = input()
    b = a[::-1]

    a, b = int(a), int(b)
    suma = a+b
    sumb = int(str(suma)[::-1])
    if(suma == sumb) : print("YES")
    else : print("NO")