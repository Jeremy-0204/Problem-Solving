n = int(input())
array = []

for _ in range(n):
    array.append(str(input()))

array = sorted(array, key = lambda word: len(word), reverse = True) # 단어 길이 역순으로 정렬시키기
print(array)

alpha = sorted(set(''.join(array))) # 지금까지 들어있는 알파벳만 추출
alpha = {a : 0 for a in alpha} # 알파벳 A~J, 가중치 dict 생성
print(alpha)


# 가중치 부가
for target in alpha.keys(): # target은 dict안의 빈도수를 찾아야 할 알파벳
    count = 0
    for word in array:
        index = [10**(len(word) - i) for i, char in enumerate(word) if char == target] # len(word) - i 하면 각자의 자릿수에 맞는 가중치를 받음. 이를 10의 제곱수로 가중치를 차례로 부여함
        count += sum(index) # 가중치 합계
    alpha[target] = count # 딕셔너리 업데이트

alpha = dict(sorted(alpha.items(), key = lambda x: x[1])) # 가중치 순서대로 정렬

print(alpha)

for i in alpha:
    flag = 0
    for word in array[::-1]:
        if i[0] in word and len(set(word)) == 1: 
            break
        elif i[0] in word and len(set(word)) > 1: # 한글자가 예외가 아니라, 같은 글자만 있으면 0이 될 수 없으니까 set으로 묶어서 원소가 여러개면 0으로 바꿔도 됨
            print(word, i[0])
            flag = 1
            alpha[i[0]] *= -1
            break
    if flag == 1: break

print(alpha)
alpha = dict(sorted(alpha.items(), key = lambda x: x[1], reverse = True))
print(alpha)


# 주어진 가중치 별 숫자 부여
i = 9
for a in alpha:
    if i > 0:
        alpha[a] = i
        i -= 1
    else: alpha[a] = i

print(alpha)


# str을 숫자로 변환
result = []
for word in array:
    new_word = ''
    for i in range(len(word)):
        if word[i] in alpha: new_word += str(alpha[word[i]])
    result.append(new_word)

print(result)

# 숫자들 합 구하기
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