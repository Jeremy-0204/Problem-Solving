nlist = []
for _ in range(int(input())):
    num = int(input())
    if num != 0: nlist.append(num)
    else: nlist.pop()
print(sum(nlist))