e, s, m = map(int, input().split())
year = 1
# 1 �� E �� 15, 1 �� S �� 28, 1 �� M �� 19

while True:
    if (year - e)  % 15 == 0 and (year - s) % 28 == 0 and (year - m) % 19 == 0:
        break
    year += 1

print(year)