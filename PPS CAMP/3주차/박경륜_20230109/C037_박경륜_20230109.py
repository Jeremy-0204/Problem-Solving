# answer = []
# while True:
#   a, b = map(int, input().split())

#   if (a == 0 and b == 0):
#     break

#   dp = dict()
#   dp[0], dp[1] = 1, 2
#   i = 2
#   count = 0

#   while(dp[i-1] <= b):
#     dp[i] = dp[i-1] + dp[i-2]
#     if (a<=dp[i]<=b): count += 1
#     i += 1
  
#   answer.append(count)

# for i in range(0, len(answer)):
#   print(answer[i])

dp = [0 for i in range(1001)]
dp[1] = 1
dp[2] = 2
for i in range(3,1001,1):
  dp[i] = dp[i - 1] + dp[i - 2]

while 1:
  a,b = map(int,input().split())
  if a==0 and b==0:
    break
  cnt = 0
  for i in range(1,1001,1):
    if a <= dp[i] and dp[i] <= b:
      cnt+=1
  print(cnt)