n = int(input())
MAX = 1003002
sieve = [True] * MAX

m = int(MAX ** 0.5)

for i in range(2, m + 1):
    if sieve[i] == True: # i가 소수인 경우
        for j in range(i + i, MAX, i): # i이후 i의 배수들은 False 판정
            sieve[j] = False

# 소수 목록 산출
array = [i for i in range(2, MAX) if sieve[i] == True and str(i) == str(i)[::-1]]

for i in range(len(array)): 
    if array[i] >= n: 
        print(array[i])
        break