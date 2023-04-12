# 반복문
def fact_iter(n):
    result = 1

    for i in range(1, n + 1): result *= i
    return result

# 재귀함수
def fact_rec(n):
    if n <= 1: return 1

    return n * fact_rec(n-1)

print('반복문:', fact_iter(5))
print('재귀함수:', fact_rec(5))