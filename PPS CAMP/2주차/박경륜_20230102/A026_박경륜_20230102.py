def solution(x):
    answer = True
    st_num = str(x)
    copy = x
    num = len(st_num)
    sum = 0
    
    
    sib = 10 ** (num-1)
    print(sib)
    
    
    while True:
        if sib < 1 or copy < 1: break;
        print(sib)
        print(copy // sib)
        
        sum += copy // sib
        copy %= sib
        sib //= 10
    
    if x % sum != 0: answer = False
    return answer