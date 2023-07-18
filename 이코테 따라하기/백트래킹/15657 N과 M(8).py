import sys
input = sys.stdin.readline

n, m = map(int, input().split())
numbers = sorted(list(map(int, input().split())))
s= []

def dfs(start):
    if len(s) == m:
        print(*s)
        return
    
    for i in range(start, n):
        s.append(numbers[i])
        dfs(i)
        s.pop()

dfs(0)
