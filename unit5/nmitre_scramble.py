import random

def scramble_word():
    user_list = input("Enter a word you want to scramble: ")
    some_list = list(user_list)
    random.shuffle(some_list)
    print(some_list)

scramble_word()
