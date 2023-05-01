array = set()
for _ in range(int(input())):
    commands = list(input().split())

    if commands[0] == "add":
        array.add(int(commands[1]))

    elif commands[0] == "remove":
        array.discard(int(commands[1]))
    
    elif commands[0] == "check":
        print(1 if commands[1] in array else 0)

    elif commands[0] == "toggle":
        if commands[1] in array: array.discard(commands[1])
        else: array.add(commands[1])

    elif commands[0] == "all":
        array = set([i for i in range(1, 21)])