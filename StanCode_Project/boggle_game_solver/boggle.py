"""
File: boggle.py
Name: Amy Hung
----------------------------------------
This program shows words in 4x4 metrics created by user.
"""

import time

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'


def main():
    start = time.time()

    num = 1  # count the number of line entered by user
    enter_list = []  # place data entered by user
    while True:
        line = input(str(num) + " row of letters: ")
        if len(line) == 4:
            enter_list.append(line)
            num += 1
            if num > 4:
                break
        else:
            print('Illegal input')
            break

    find_words(enter_list)

    end = time.time()
    print(f'The speed of your anagram algorithm: {end - start} seconds.')


def find_words(enter_list):
    # collect words created through permutations
    words_created_in_boggle = get_permutations(enter_list)

    # look the collected words up in the dictionary
    check_dictionary(words_created_in_boggle)


def get_permutations(enter_list):
    # set each letter in 4x4 metrics as starting point, 16 starting points in total.
    words_created_in_boggle = []
    for row in range(4):
        for column in range(4):

            # After the starting point is decided, permutations begin.
            words = get_permutations_helper(enter_list, row, column, list_words=[])

            # put all collected words into words_created_in_boggle
            for word in words:
                words_created_in_boggle.append(word)
    return words_created_in_boggle


def get_permutations_helper(enter_list, row, column, new_word="", list_words=[]):
    if len(new_word) < 6:
        # only new letter can be used (If the letter is used, its value becomes '*'.)
        if enter_list[row][column] != "*":

            # add new letter to the starting letter
            new_word += enter_list[row][column]

            # create another list with the same entered data to assign different value
            number = "1234"
            new_enter_list = [[number[0]]*4, [*number[1]]*4, [*number[2]]*4, [*number[3]]*4]
            for i in range(4):
                for j in range(4):
                    new_enter_list[i][j] = enter_list[i][j]

            # If the letter is used, its value becomes '*'.
            new_enter_list[row][column] = "*"

            # When new word is created, add it to list_words.
            if len(new_word) >= 4:
                list_words.append(new_word)

            # find next letter
            next_move = [(1, 1), (-1, -1), (1, -1), (-1, 1), (1, 0), (0, 1), (-1, 0), (0, -1), ]
            for x, y in next_move:
                if 0 <= row + x <= 3 and 0 <= column + y <= 3:
                    get_permutations_helper(new_enter_list, row + x, column + y, new_word, list_words)
    return list_words


def check_dictionary(words_created_in_boggle):

    # put all words in the dictionary to dictionary_lst
    dictionary_lst = []
    with open(FILE, 'r') as f:
        for line in f:
            word_in_dictionary = line.strip()

            # Since words with fewer than four letters are not accepted, it is not necessary to put those words in
            # the dictionary_lst.
            if len(word_in_dictionary) >= 4:
                dictionary_lst.append(word_in_dictionary)

    count = 0
    for word in words_created_in_boggle:
        if word.lower() in dictionary_lst:
            count += 1
            print('Found "' + str(word) + '"')
    print('There are ' + str(count) + ' words in total.')


def has_prefix(sub_s):
    dictionary_lst = []
    with open(FILE, 'r') as f:
        for line in f:
            word_in_dictionary = line.strip()
            if len(word_in_dictionary) >= 4:
                dictionary_lst.append(word_in_dictionary)

    list_to_string = ''
    for i in range(len(sub_s)):
        list_to_string += sub_s[i]
    for j in range(len(dictionary_lst)):
        if dictionary_lst[j].startswith(list_to_string, 0, 2):
            return True


if __name__ == "__main__":
    main()
