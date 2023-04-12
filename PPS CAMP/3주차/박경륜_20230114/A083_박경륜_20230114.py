N = int(input())
nlist = list(map(int, input().split()))

for i in sorted(list(set(nlist))):
    print(i, end = ' ')