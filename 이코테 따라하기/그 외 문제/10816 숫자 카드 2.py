import sys
input = sys.stdin.readline

n = int(input())
numlist = sorted(list(map(int, input().split())))
m =  int(input())
checklist = list(map(int, input().split()))

dic = {}

for n in numlist:
    if n in dic: dic[n] += 1
    else: dic[n] = 1

print(' '.join(str(dic[m]) if m in dic else '0' for m in checklist))