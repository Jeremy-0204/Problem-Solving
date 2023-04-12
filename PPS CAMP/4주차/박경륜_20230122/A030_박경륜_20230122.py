N, flag = map(int, input().split())
gg, gb, bg, bb = map(float, input().split())

good = [0 for i in range(N)]
bad = [0 for i in range(N)]

if flag == 0:
    good[0], bad[0] = gg, gb
else:
    good[0], bad[0] = bg, bb

for i in range(1, N):
    good[i] = good[i-1] * gg + bad[i-1] * bg
    bad[i] = good[i-1] * gb + bad[i-1] * bb

print(round(good[N-1] * 1000))
print(round(bad[N-1] * 1000))