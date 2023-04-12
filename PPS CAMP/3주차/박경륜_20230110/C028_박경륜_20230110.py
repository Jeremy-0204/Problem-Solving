import sys
N = int(input())
lists = []
for i in range(N):
    A, B = map(int, sys.stdin.readline().rstrip().split())
    lists.append(A+B)

for i in lists: print(i)