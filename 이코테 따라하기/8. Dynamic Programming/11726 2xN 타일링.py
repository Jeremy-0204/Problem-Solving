room = [0] * 100008

N = int(input())

room[1] = 1
room[2] = 2

for i in range(3,N+1):
    room[i] = (room[i - 1] + room[i - 2]) % 10007

print(room[N])