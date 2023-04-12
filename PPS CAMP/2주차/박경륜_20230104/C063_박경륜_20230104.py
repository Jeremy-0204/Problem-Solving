def binary_search(array, target, start, end):
    if start > end:
        return 0
    
    mid = (start + end) // 2

    if (int(array[mid]) == target): return 1

    elif int(array[mid]) > target: return binary_search(array, target, start, mid - 1)
    else: return binary_search(array, target, mid + 1, end)

n = int(input())
nlist = list(map(int, input().split()))

m = int(input())
mlist = list(map(int, input().split()))

nlist.sort()

for i in mlist:
    print(binary_search(nlist, i, 0, len(nlist)-1))

