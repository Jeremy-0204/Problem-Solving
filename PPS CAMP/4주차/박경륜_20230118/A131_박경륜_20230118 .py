'''
nlist = []
for _ in range(int(input())):
    nlist.append(int(input()))

nlist.sort()

# 평균
print(round(sum(nlist) / len(nlist)))

# 중앙값
if len(nlist) == 1 : print(nlist[0])
else : print(nlist[len(nlist)//2])

# 최빈값
req = {}
max = 0
for i in nlist:
    if nlist.count(i) >= max: 
        max = nlist.count(i)
        freq[i] = (nlist.count(i))
freq = sorted(freq.items(), reverse = True)

for i in range(len(freq)-1): 
    if freq[i][0] != freq[0][0]: freq.remove(freq[i])
if(len(freq)) > 1: print(freq[-2][0])
else: print(freq[0][0]) 


# 범위
sum = 0
if len(nlist) == 1: sum = 0
else: sum = nlist[-1] - nlist[0]
print(sum)

'''

from collections import Counter
import sys



numbers = []
for _ in range(int(sys.stdin.readline())):
    num = int(sys.stdin.readline())
    numbers.append(num)

numbers.sort()

cnt = Counter(numbers).most_common(2)

print(round(sum(numbers) / len(numbers)))
print(numbers[len(numbers) // 2])
if len(numbers) > 1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])
print(max(numbers) - min(numbers))