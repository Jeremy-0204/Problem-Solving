N = int(input())


# 백트래킹을 이용한 문제 풀이
def bt(cur):
    answer.append(int(cur))
    for j in range(0, int(cur[-1])):  # 현재 숫자의 끝자리보다 낮은 숫자들만 그 다음 자리수에 추가한다.
        bt(cur + str(j))


if N > 1023:  # 갯수가 1023개인듯... 0 부터 9876543210 까지 이므로 얼마 안나옴
    print(-1)
else:
    answer = []
    for i in range(10):  # 맨 앞자리가 0, 1, ,... , 9
        bt(str(i))

    print(sorted(answer)[N - 1])