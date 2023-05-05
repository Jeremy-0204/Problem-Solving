import sys
N = int(sys.stdin.readline().strip())
squares = [n ** 2 for n in range(1, int(N ** (1 / 2)) + 1)] # 현재 숫자의 제곱근까지의 숫자들을 담아놓음

total = 0
nums = [N]

while len(nums) > 0:
    total += 1
    temp = set()

    # nums에는 원래 리스트의 원소에서 자기보다 작은 제곱근들을 뺀 숫자들을 담는다
    for num in nums:
        for n in squares:
            if n <= num:
                temp.add(num - n)
    if 0 in temp: # 0이 들어있으면 제곱근들로 연산이 마쳤다는 뜻
        break
    nums = list(temp) # nums를 새로 뺀 값으로 업데이트 한다
print(total)