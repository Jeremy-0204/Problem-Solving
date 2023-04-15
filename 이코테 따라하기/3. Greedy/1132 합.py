n = int(input())
array = []

for _ in range(n):
    array.append(str(input()))

array = sorted(array, key = lambda word: len(word), reverse = True)
alpha = sorted(set(''.join(array))) # 지금까지 들어있는 알파벳만 추출
alpha = {a : 0 for a in alpha} # 알파벳 A~J, 가중치 dict 생성

print(alpha)

for target in alpha.keys():
    count = 0
    for word in array:
        index = [len(word) - i for i, char in enumerate(word) if char == target]
        count += sum(index)
    alpha[target] = count

print(alpha)


# ABC
# BCA 가중치는 len(word) - i로 주면 되겠다

# A - 4, B - 5, C - 3
# 8, 9, 7
# 9, 7, 8

# dict 생성 
# 알파벳 별로 다 만들어야 하나?