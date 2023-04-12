import itertools
import math

# �Ҽ����� �ƴ����� �Ǻ��ϴ� �Լ��̴�.
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
    # nums �迭�� 3���� �����Ͽ� ���� �� �ִ� ������ ���Ѵ�.
    combi = list(itertools.combinations(nums,3))
    # ���� �迭�� ���� �Ҽ��̸� 1�� ���ϰ� �Ҽ��� �ƴϸ� 0�� ���Ѱ��� answer�� ������ �Ѵ�.
    for i in range(len(combi)):
        answer += prime(sum(combi[i]))
    
    return answer