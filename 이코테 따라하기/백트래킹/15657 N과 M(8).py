import sys
input = sys.stdin.readline

n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
s= []

def dfs():
    if len(s) == m:
        print(*s)
        return
    
    for i in range(n):
        if numbers[i] not in s:
            s.append(numbers[i])
            dfs()
            s.pop()

dfs()
