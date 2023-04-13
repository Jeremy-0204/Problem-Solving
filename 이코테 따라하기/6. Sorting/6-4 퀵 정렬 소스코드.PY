array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end: # 원소가 1개인 경우 종료
        return
    
    pivot = start # 피벗은 첫 번째 원소
    left = start + 1
    right = end
    
    while left <= right:
        while left <= end and array[left] <= array[pivot]:
            left += 1
        while right > start and array[right] >= array[pivot]:
            right -= 1
        if left > right: # 엇갈렸다면 작은 데이터와 피벗 교체
            print("엇갈림! right, pivot 교체중")
            print(array)
            print("교체전 :", array[right], array[pivot])
            array[right], array[pivot] = array[pivot], array[right]
            print("교체후 :", array[right], array[pivot])
            print(array)

        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            print("안 엇갈림! left, right 교체중")
            print(array)           
            print("교체전 :", array[left], array[right])
            array[left], array[right] = array[right], array[left]
            print("교체전 :", array[left], array[right])
            print(array)


    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)


quick_sort(array, 0, len(array) - 1)
print(array)