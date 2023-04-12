A, B = map(int, input().split())
nlist = []
for i in range(1, B+1):
    for j in range(i):
        nlist.append(i)
print(sum(nlist[A-1:B]))