N = int(input())

nlist = list(map(int, input().split()))
nilst = nlist.sort()
sum = 0
for i in range(len(nlist)-1):
    sum += nlist[i]
print(sum)