import sys

m,n = map(int,input().split())
l = sorted(list(map(int,sys.stdin.readline().split())))

print(l[n-1])