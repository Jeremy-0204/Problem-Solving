# import sys
# input = sys.stdin.readline

# array = set()
# for _ in range(int(input())):
#     commands = input().strip().split()

#     if commands[0] == "add":
#         array.add(int(commands[1]))

#     elif commands[0] == "remove":
#         array.discard(int(commands[1]))
    
#     elif commands[0] == "check":
#         print(1 if int(commands[1]) in array else 0)

#     elif commands[0] == "toggle":
#         if int(commands[1]) in array: array.discard(int(commands[1]))
#         else: array.add(int(commands[1]))

#     elif commands[0] == "all":
#         array = set([i for i in range(1, 21)])
import sys

S = set()
T = int(sys.stdin.readline())
for i in range(T):
    cmdAndX = sys.stdin.readline().split()
    if len(cmdAndX) == 1:
        if cmdAndX[0] == 'all':
            S = set([x for x in range(1, 21)])
        else:
            S = set()

    else:
        cmd, x = cmdAndX[0], int(cmdAndX[1])
        if cmd == 'add':
            S.add(x)
        elif cmd == 'check':
            if x in S:
                print(1)
            else:
                print(0)
        elif cmd == 'remove':
            if x in S:
                S.discard(x)
        elif cmd == 'toggle':
            if x in S:
                S.discard(x)
            else:
                S.add(x)