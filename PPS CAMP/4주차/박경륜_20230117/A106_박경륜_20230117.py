N = int(input())
answer = []

for i in range(N):
    string = input()
    string = list(set(string))
    sum = 0
    for i in string:
        sum += ord(i)
    answer.append(2015-sum)

for i in answer: print(i)