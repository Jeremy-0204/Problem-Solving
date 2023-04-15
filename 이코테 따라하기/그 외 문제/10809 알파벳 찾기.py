s = input()

for i in range(97, 122 + 1):
    for j in range(len(s)):
        if chr(i) == s[j]: 
            print(j, end = ' ')
            break

        if chr(i) not in s: 
            print(-1, end = ' ')
            break