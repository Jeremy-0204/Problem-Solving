N = int(input())
slist = []
for i in range(0, N):
    slist.append(input())

s = list(set(slist))

sortlist = []
for i in s:
    sortlist.append((len(i), i))
result = sorted(sortlist)

for _, word in result:
    print(word)



