from collections import deque
import sys

cards = deque()

for i in range(1, int(sys.stdin.readline()) + 1):
    cards.append(i)

while len(cards) != 1:
    cards.remove(cards[0])
    temp = cards[0]
    cards.popleft()
    cards.append(temp)

print(cards[0])