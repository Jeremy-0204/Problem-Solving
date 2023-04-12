def rec_func(i):
    if i == 100: return

    print(f'{i}번째 함수에서 {i+1}번째 함수를 호출합니다.')
    rec_func(i+1)
    print(f'{i}번째 함수를 종료합니다.')

rec_func(1)