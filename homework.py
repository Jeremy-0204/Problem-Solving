# import sys
# input = sys.stdin.readline 
# 512 character buffer 제한으로 긴 문장을 못 받아옴

def question_one(words):
    print("\n")
    print("=====Q1 Text from users")
    print("Teach me words: ")
    words.extend(list(input().split()))

def question_two_a(words):
    print("\n")
    num_words = len(words)
    print(f"=====Q2-A All words {num_words} words")
    print(words)

def question_two_b(words):
    print("\n")
    temp_words = [word.lower() for word in words]
    words.clear()
    words.extend(list(set(temp_words)))
    num_words = len(words)
    print(f"=====Q2-B Duplicated removed (case-insensitive) {num_words} words")
    print(words)

def question_two_c(words, min_length_word):
    print("\n")
    temp_words = [word for word in words if len(word) > min_length_word]
    words.clear()
    words.extend(temp_words)
    num_words = len(words)
    print(f"=====Q2-C Words whose length is greater than {min_length_word} {num_words} words")
    print(words)

def question_two_d(words, punctuations):
    print("\n")
    punc_words = []
    for word in words:
        for i in range(len(word)):
            if word[i] in punctuations:
                punc_words.append(word)
                break

    temp_words = list(set(words) - set(punc_words))
    
    words.clear()
    words.extend(temp_words)
    num_words = len(words)

    print(f"=====Q2-D Words with punctuation marks removed {num_words} words")
    print(words)
            
    # words에서 단어 하나씩 빼와서
    # word의 각 char마다 punctuation이랑 비교
    # 있으면 해당 word는 제거

def question_two_e(words):
    print("\n")
    temp_words = sorted(words)
    words.clear()
    words.extend(temp_words)
    print(f"=====Q2-E Words in ascending order")
    print(words)

def game_initiate(words): 
    min_length_word = 2
    punctuations = '''!()-[]{};:—'"‘\,<>./?@#$%^&*_~'''

    question_one(words)
    question_two_a(words)
    question_two_b(words)
    question_two_c(words, min_length_word)
    question_two_d(words, punctuations)
    question_two_e(words)

# words중 랜덤하게 단어 선택 후 출력
import random
import datetime
now = datetime.datetime.now

def question_three(words):
    print("\n")
    print(f"=====Q3 Let's play the game with this word:")
    current_word = random.choice(words)
    print(current_word)
    return current_word

def question_four(current_word):
    print("\n")
    print(f"=====Q4 User's word")
    print(f"Enter a at-least-3-characters word starting with the last letter of {current_word}:")
    user_word = input().lower()
    return user_word

def question_five(user_word, last_char):
    if last_char != user_word[0] or len(user_word) < 3:
        return False
    else:
        return True

def question_six(words, last_char):
    temp_list = [word for word in words if last_char == word[0]]
    return temp_list
    
def question_seven(dictionary):
    print("\n")
    print(f"=====Q7 User's WIN")
    current_time = now().strftime("%Y/%m/%d %H:%M:%S")
    print(f"User Win! Recorded at", current_time)
    dictionary[current_time] = 'user'

def question_eight(words, dictionary):
    print("\n")
    print(f"=====Q8 RESTART")
    print("Do you like to play the game one more time? (yes): ")
    answer = input().lower()

    if answer == "yes":
        game_start(words, dictionary)

    else:
        question_nine(dictionary)
        return False
    
def question_nine(dictionary):
    print("\n")
    print(f"=====09 History of winning records")
    for key, value in dictionary.items():
        print(key, value)



def game_start(words, dictionary):
    # 랜덤으로 처음 단어 선택
    current_word = question_three(words)

    while True:
        # 유저가 단어 입력
        user_word = question_four(current_word)

        if question_five(user_word, current_word[-1]):
            current_word = user_word
            #만약 컴퓨터가 이기면 (False), 5번 출력
            #만약 유저가 이기면 그냥 6번 바로 출력
            
        else: 
            print("\n")
            print(f"=====Q5 Computer's WIN")
            current_time = now().strftime("%Y/%m/%d %H:%M:%S")
            print(f"Computer Win! Recorded at", current_time)
            dictionary[current_time] = 'computer'
            if not question_eight(words, dictionary): break

        
        if len(question_six(words, current_word[-1])) == 0:
            question_seven(dictionary)
            if not question_eight(words, dictionary): break
        
        else:
            current_word = random.choice(question_six(words, current_word[-1]))
            print("\n")
            print(f"=====Q6 Cpmputer's word")
            print(current_word, "\n")
    


def main():
    # print("안녕 메인 함수 실행해볼게")
    words = []
    dictionary = dict()
    game_initiate(words)
    game_start(words, dictionary)


if __name__ == "__main__":
    main()