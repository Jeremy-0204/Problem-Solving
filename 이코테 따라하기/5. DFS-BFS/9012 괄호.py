for _ in range(int(input())):
    array = list(input())
    stack = []
    result = ""
    for i in array:
        if i == "(": stack.append(i)
        if i == ")" and (stack and stack[-1] == "("): stack.pop()
        elif (not stack or stack and stack[-1] != "(") and i == ")" : 
            stack.append(i)
            
    if len(stack) == 0: result = "YES"
    else: result = "NO"

    print(result)