N = int(input())
answer = []
for i in range(N):
    nlist = list(map(int, input().split()))
    nlist.sort()
    answer.append(nlist[-3])
    
for i in answer:
    print(i)