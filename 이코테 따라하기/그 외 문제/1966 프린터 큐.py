from collections import deque
t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    q = deque(map(int, input().split()))
    index = deque([i for i, _ in enumerate(q)])
    count = 0
    while True:
        if q[0] < max(q):
            q.append(q.popleft())
            index.append(index.popleft())

        else:
            q.popleft()
            idx = index.popleft()
            count += 1

            if(idx == m):
                print(count)
                break