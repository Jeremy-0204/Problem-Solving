def solution(arr, divisor):
    answer = []
    arr.sort()
    
    for i in range(0,len(arr)):
        if arr[i] >= divisor and arr[i] % divisor == 0: answer.append(arr[i])
        
    if len(answer) == 0: answer.append(-1)
    return answer