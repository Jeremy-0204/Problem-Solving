string = input().lower()
slist = list(set(string))
countlist = {}
count = 0
for i in slist:
    countlist[i] = (string.count(i))

countlist = {k: v for k, v in sorted(countlist.items(), key=lambda item: item[1], reverse=True)}

if (len(countlist) > 1) and list(countlist.values())[0] == list(countlist.values())[1]:
    print("?")
else:
    print(list(countlist.keys())[0].upper())
