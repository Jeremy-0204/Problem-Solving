import sys
input = sys.stdin.readline

T = int(input())

while T:
    ans = 999999
    T -= 1
    n = int(input())
    mbti = list(map(str, input().split()))

    if n > 32: print(0)
    else:
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    tmp = 0
                    if i == j or j == k or i == k:
                        continue
                    for x in range(4):
                        if mbti[i][x] != mbti[j][x]: tmp += 1
                        if mbti[j][x] != mbti[k][x]: tmp += 1
                        if mbti[i][x] != mbti[k][x]: tmp += 1
                    ans = min(tmp, ans)
        print(ans)