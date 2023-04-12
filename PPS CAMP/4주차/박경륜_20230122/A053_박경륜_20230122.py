import sys
stack = []
for _ in range(int(input())):
    words = sys.stdin.readline().split()
    cmd = words[0]

    if cmd == 'push':
        stack.append(words[1])
    elif cmd == 'pop':
        if len(stack) == 0: print(-1)
        else: print(stack.pop())
    elif cmd == 'size':
        print(len(stack))
    elif cmd == 'empty':
        if len(stack) == 0: print(1)
        else: print(0)
    elif cmd == 'top':
        if len(stack) == 0: print(-1)
        else: print(stack[-1])