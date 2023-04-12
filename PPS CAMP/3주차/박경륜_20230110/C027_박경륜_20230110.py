e, s, m = map(int, input().split())
year = 1
# 1 ¡Â E ¡Â 15, 1 ¡Â S ¡Â 28, 1 ¡Â M ¡Â 19

while True:
    if (year - e)  % 15 == 0 and (year - s) % 28 == 0 and (year - m) % 19 == 0:
        break
    year += 1

print(year)