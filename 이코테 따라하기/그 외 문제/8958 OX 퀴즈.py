n = int(input())

for _ in range(n):
    s = input()
    count, score = 0, 0
    for i in s:
        if i == "O": 
            count += 1
            score += count
        else: count = 0
    print(score)
