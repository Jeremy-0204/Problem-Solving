# import sys
# from collections import deque

# def osaoip(num): return round(num+10**(-len(str(num))-1))

# input = sys.stdin.readline
# list = []

# n = int(input())
# trim = n * 30 / 100
# rtrim = osaoip(trim)

# for _ in range(n):
#     list.append(int(input()))

# que = deque(sorted(list))

# if n <= 0:
#     ans = 0
# else:
#     for _ in range(int(rtrim / 2)):
#         que.popleft()
#         que.pop()
#     ans = osaoip(sum(que) / len(que))

# print(ans)

import sys
input = sys.stdin.readline

from collections import deque

import decimal
context = decimal.getcontext()
context.rounding = decimal.ROUND_HALF_UP

comment =  int(input())

level_list = []

for i in range(comment):
  level = int(input())
  level_list.append(level)

level_list.sort()

deq = deque(level_list)
if comment == 0:
  print('0')
else:
  num = round(decimal.Decimal(comment*0.15),0)
  for i in range(int(num)):
    deq.pop()
    deq.popleft()

  print(round(decimal.Decimal(sum(deq) / len(deq)), 0))