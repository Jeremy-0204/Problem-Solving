n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

a.sort()
b.sort()

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2

        if array[mid] == target: return mid
        elif array[mid] > target: end = mid - 1
        else: start = mid + 1
    return None

for req in b:
    result = binary_search(a, req, 0, len(a) - 1)
    if result == None: print('no', end = ' ')
    else: print('yes', end = ' ')
