for _ in range(int(input())):
    nlist = list(map(int, input().split()))

    N = nlist[0]
    nlist.remove(nlist[0])
    avg = sum(nlist) / N
    count = 0
    for i in range(len(nlist)):
        if nlist[i] > avg:
            count += 1
    print(f'{round(count/N, 5) * 100:.3f}%')