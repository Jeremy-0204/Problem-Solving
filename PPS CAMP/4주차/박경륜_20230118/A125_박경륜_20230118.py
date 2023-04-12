nlist = []
for _ in range(int(input())):
    nlist.append(int(input()))

nlist.sort(reverse=True)

for i in range(len(nlist)):
    nlist[i] *= i+1

nlist.sort(reverse=True)
print(nlist[0])