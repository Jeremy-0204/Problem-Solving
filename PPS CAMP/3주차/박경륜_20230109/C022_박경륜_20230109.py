import itertools
import math

# 소수인지 아닌지를 판별하는 함수이다.
def prime(n):
    if n < 2:
        return 0
    else:
        for i in range(2,int(math.sqrt(n)+1)):
            if n % i == 0: 
                return 0
        return 1
    
def solution(nums):
    answer = 0
    # nums 배열중 3개를 선택하여 나올 수 있는 조합을 구한다.
    combi = list(itertools.combinations(nums,3))
    # 조합 배열의 합이 소수이면 1을 더하고 소수가 아니면 0을 더한값을 answer에 누적합 한다.
    for i in range(len(combi)):
        answer += prime(sum(combi[i]))
    
    return answer