n = int(input())

array = list(map(int, input().split()))

# array 받고, dict에 key 값으로 하나씩 지정, sorted로 오름차순 정렬
#dict key를 가져오면서 enumerate로 인덱스를 value로 추가

temp = sorted(list(set(array)))
d = dict()
for i in range(len(set(array))):
    d[temp[i]] = i

for i in array:
    if i in d:
        print(d[i], end = ' ')
