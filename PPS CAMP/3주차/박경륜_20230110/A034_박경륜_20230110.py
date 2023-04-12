lists = []
for i in range(10):
    lists.append(int(input()) % 42)

print(len(list(set(lists))))