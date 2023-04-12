L = int(input())

for _ in range(L):
    pwd = input()

    cur = []
    sub = []

    for i in pwd:
        if i == '<':
            if cur:
                sub.append(cur.pop())
        elif i == '>':
            if sub:
                cur.append(sub.pop())
        elif i == '-':
            if cur:
                cur.pop()
        else:
            cur.append(i)

    print("".join(cur), "".join(sub[::-1]), sep="")