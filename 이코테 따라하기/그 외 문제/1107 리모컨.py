import sys
input = sys.stdin.readline
n = int(input())
m = int(input())
broken = list(map(int, input().split()))

result = abs(n - 100) # 현재 누르는 최대 개수임 얘를 토대로 최소 횟수 구하기

for num in range(1000001):
    # 누를 수 있는 버튼 중에 가장 n하고 가까운 애를 구하면 되겠지
    for c in str(num):
        if int(c) in broken: break # 숫자 하나라도 버튼이 망가져 있는 애면 최소가 될 수 없음
    else: result = min(result, abs(num - n) + len(str(num))) # +, - 개수 + 숫자 누르는 횟수

print(result)

# n = int(input())
# m = int(input())
# if m != 0: broken = list(map(int, input().split()))
# else: broken =[]

# default, result = 100, 0
# button = [i for i in range(0,10)]

# if len(broken) > 0:
#     for i in broken: 
#         if i in button: button.remove(i)

# array = []
# if button and (int(str(n)[0]) in button or int(str(n)[0]) < button[-1]): 
#     for i in str(n):
#         if int(i) in button: array.append(i)
#         else:
#             sub = sorted([abs(int(i) - j) for j in button])
#             temp = 0
#             for k in sub: 
#                 if k > 0: 
#                     temp = abs(int(i) - k)
#                     break
#             array.append(str(temp))
    
# elif button:
#     for i in str(n):
#         array.append(str(max(button)))

# if n != 100:
#     if not array:
#         result = n
#     else:
#         result = int(''.join(array))
#         result = abs(n - result) + len(array)
# print(result)


