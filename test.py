def solution(n, k, B_cards):

    # 각 카드의 점수를 계산하는 함수
    def get_card_score(card_num):
        return min(B_cards[card_num], k - B_cards[card_num])

    # 영희의 점수를 계산하는 함수
    def calculate_h_score():
        h_score = 0
        for i in range(1, n+1):
            score = get_card_score(i)
            if score > 0:
                h_score += score
        return h_score

    # 철수의 점수를 계산하는 함수
    def calculate_b_score():
        b_score = 0
        for i in range(1, n+1):
            score = get_card_score(i)
            if score > 0:
                b_score += k - score
        return b_score

    # 영희가 이길 수 있는 최대 점수 차이를 계산하는 함수
    def calculate_max_score_diff():
        h_score = calculate_h_score()
        b_score = calculate_b_score()
        if h_score > b_score:
            return h_score - b_score
        else:
            return -1

    return calculate_max_score_diff()