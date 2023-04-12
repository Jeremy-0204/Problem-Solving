ndict = {}
nlist = []
answer = []

for _ in range(int(input())):
    name = input()
    nlist.append(name[0])

nset = set(nlist)

for i in nset:
    ndict[i] = nlist.count(i)

for key, value in ndict.items():
    if value >= 5: answer.append(key)

if len(answer) == 0: print("PREDAJA")
else:
    answer.sort()
    for i in answer:
        print(i, end='')