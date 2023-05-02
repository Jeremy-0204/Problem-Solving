import sys
input = sys.stdin.readline

n, m = map(int, input().split())
pokedex = dict()

for i in range(1, n + 1):
    pokemon = input().rstrip()
    pokedex[i] = pokemon
    pokedex[pokemon] = i

for _ in range(m):
    check = input().rstrip()
    if check.isdigit(): print(pokedex[int(check)])
    else: print(pokedex[check])