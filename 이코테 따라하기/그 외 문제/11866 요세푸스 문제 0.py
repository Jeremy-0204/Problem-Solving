from collections import deque
que = deque()
answer = []
n, k = map(int, input().split())
index = k - 1
for i in range(1, n+ 1): que.append(i)

while True:
    # print(que)
    answer.append(que[index])
    que.remove(que[index])
    
    # 인덱스 pop
    if not que: break

    index = (index + k - 1) % len(que)
    # k만큼 더해서 지운다

print("<" + "".join(str(answer)[1:-1]) + ">")