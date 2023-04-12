T = int(input())
ans = []
for i in range(T):
    H, W, N = map(int, input().split())
    if(N % H == 0) : 
        floor = H
        room = N // H
    else: 
        floor = N % H # 앞자리 층수
        room = N // H + 1 # 호수

    if room < 10: roomstr = '0' + str(room)
    else: roomstr = str(room)

    answer = str(floor) + roomstr
    ans.append(answer)

for i in ans:
    print(i)