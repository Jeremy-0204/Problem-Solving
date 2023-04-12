A, B, C = map(int, input().split())

# A + Bx < Cx 손익 분기점
# A < (C-B)x
# A / (C-B) < x

if (C <= B): print(-1)

else: print(int((A / (C-B) + 1)))