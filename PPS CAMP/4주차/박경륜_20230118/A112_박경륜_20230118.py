N, M = map(int, input().split())
mina, minb = 1000, 1000
for i in range(M):
    a, b = map(int, input().split())
    if mina >= a: mina = a
    if minb >= b: minb = b

count = 0
if mina <= minb * 6:
    count = (N // 6) * mina
    if N % 6 != 0: 
        a = (N % 6) * minb
        if mina >= a: count+=a
        else: count += mina

else:
    count = N * minb

print(count)