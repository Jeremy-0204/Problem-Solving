n, m = map(int, input().split())

chess = []

for _ in range(n):
    chess.append(list(input()))

array = []

for a in range(n - 7):
    for b in range(m - 7):
        countW, countB = 0, 0
        for i in range(a, a + 8):
            for j in range(b, b + 8):
                if (i + j) % 2 == 0:
                    if chess[i][j] != 'W': countW += 1
                    if chess[i][j] != 'B': countB += 1

                else: 
                    if chess[i][j] != 'W': countB += 1
                    if chess[i][j] != 'B': countW += 1                    

        array.append(min(countW, countB))

print(min(array))
'''
1번째 알파벳을 기준으로
i % 2 == 1은 첫번째 알파벳
i % 2 == 0은 두번째 알파벳

j도 마찬가지
'''