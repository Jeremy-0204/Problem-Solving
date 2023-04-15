n = int(input())
array = []

for _ in range(n):
    array.append(str(input()))

array = sorted(array, key = lambda word: len(word), reverse = True)
print(array)

alpha = sorted(set(''.join(array))) # 지금까지 들어있는 알파벳만 추출
alpha = {a : 0 for a in alpha} # 알파벳 A~J, 가중치 dict 생성

print(alpha)

for target in alpha.keys():
    count = 0
    for word in array:
        index = [len(word) - i for i, char in enumerate(word) if char == target]
        count += sum(index)
    alpha[target] = count

alpha = dict(sorted(alpha.items(), key = lambda x: x[1]))

print(alpha)

for i in alpha:
    flag = 0
    for word in array[::-1]:
        if i[0] in word and len(word) == 1: 
            break
        elif i[0] in word and len(word) > 1: 
            print(word, i[0])
            flag = 1
            alpha[i[0]] *= -1
            break
    if flag == 1: break

print(alpha)
alpha = dict(sorted(alpha.items(), key = lambda x: x[1], reverse = True))
print(alpha)

i = 9
for a in alpha:
    if i > 0:
        alpha[a] = i
        i -= 1
    else: alpha[a] = i

print(alpha)

result = []

for word in array:
    new_word = ''
    for i in range(len(word)):
        if word[i] in alpha: new_word += str(alpha[word[i]])
    result.append(new_word)

print(result)
count = 0
for i in result:
    count += int(i)

print(count)

# ABC
# BCA 가중치는 len(word) - i로 주면 되겠다

# A - 4, B - 5, C - 3
# 8, 9, 7
# 9, 7, 8

# dict 생성 
# 알파벳 별로 다 만들어야 하나?