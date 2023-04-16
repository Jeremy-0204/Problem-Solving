n = int(input())
array, result = [], []
count = 1
for _ in range(n):
    target = int(input())
    while count <= target:
        array.append(count)
        result.append(True)
        count += 1
        
    if array[-1] == target:
        array.pop()
        result.append(False)
    
    else: 
        result = []
        break

if len(result) >= 1:
    for i in result:
        if i == True: print("+")
        else: print("-")
else: print("NO")