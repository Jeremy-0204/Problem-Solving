import sys
input = sys.stdin.readline

n, m = map(int, input().split())
nlist = sorted(list(map(int, input().split())))
s =[]

def dfs():
    if len(s) == m:
        print(' '.join(map(str, s)))
        return
    
    for i in range(n):
        if nlist[i] not in s:
            s.append(nlist[i])
            dfs()
            s.pop()

dfs()