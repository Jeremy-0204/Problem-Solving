from collections import deque

for _ in range(int(input())):
    commands = list(input())
    n = int(input())
    que = list(input().rstrip()[1:-1].split(',')) # "[", "]" 빼고 ","도 거른 상태로 문자열 받기

    if n > 0: que = deque(map(int, que)) # 숫자가 없으면 "[", "]" 그대로 있으니 그냥 error로 마무리 
    else: que = deque()
    
    switch = 0
    error = False

    for c in commands:
        if c == 'R':
            switch += 1
        elif c == 'D':
            if len(que) >= 1: 
                if switch % 2 == 0: que.popleft()
                else: que.pop()
            else: 
                error = True
                break
    if error:
        print('error')
    else:
        if switch % 2 == 1:
            que.reverse()
        print('[{}]'.format(','.join(map(str, que))))