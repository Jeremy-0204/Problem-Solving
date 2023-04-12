N, M = map(int, input().split())
# a = []
# b = []
answer = []

for i in range(N+M):
    answer.append(input())

sans = list(set(answer))
answer.sort()
print(len(answer)-len(sans))

for i in sans:
    if i in answer: answer.remove(i)

for i in answer:
    print(i)

# for _ in range(N):
#     a.append(input())

# for _ in range(M):
#     b.append(input())

# for i in a:
#     if i in b:  answer.append(i)
# answer.sort()
# print(len(answer))
# for i in answer:
#     print(i)