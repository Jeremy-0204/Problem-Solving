N = int(input())
M = int(input())

def combination(M, N):
    if(N == 0): return 1
    if(M == N): return 1
    return combination(M-1, N-1) + combination(M-1, N)

if(N == 1 and M == 1): print(combination(1,1))
else: print(combination(M-1, N-1))