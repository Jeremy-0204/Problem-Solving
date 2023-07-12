num=int(input())

def fib(case,n):               #피보나치 함수 생성
    if case[n]!=-1:  #-1의 값을 가진다면 아직 값이 안들어간 상태 >> -1이 아니라면 값이 들어간 상태
        return case[n]
    elif n==0:      #fib(0)=0
        case[n]=0
        return case[n]
    elif n==1:      #fib(1)=1
        case[n]=1
        return case[n]
    else:
        case[n]=fib(case,n-1)+fib(case,n-2)
        return(case[n])

case=[-1 for k in range(num+1)] #함수에 사용될 case 생성해주기 - 값이 안들어가면 -1
print(fib(case,num)) #출력