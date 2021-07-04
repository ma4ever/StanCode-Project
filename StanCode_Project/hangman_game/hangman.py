"""
File: hangman.py
Name: Huahua Hung
-----------------------------
This program plays hangman game.
Users sees a dashed word, trying to
correctly figure the un-dashed word out
by inputting one character each round.
If the user input is correct, show the
updated word on console. Players have N_TURNS
chances to try and win this game.
"""


import random
# This constant controls the number of guess the player has.
N_TURNS = 7
def main():
    r = random_word()
    s = '_' * len(r)
    incorrect = 0
    print('The word looks like: ' + str(s))
    print('You have ' + str(N_TURNS - incorrect) + ' left.')
    ans = ''
    while True:
        a = input("Your guess: ")
        a = a.upper()
        # separate single alphabet or not
        if len(a) > 1 or not a.isalpha():
            print('Illegal format.')
        else:
            # separate a in r or not
            if a in r:
                print('You are correct!')
                i = r.find(a)
                ans = s[:i] + a + s[i + 1:]
                s = ans
                # check if there is a repeating word
                for j in range(len(r)):
                    if a == r[j]:
                        ans = s[:j] + a + s[j + 1:]
                        s = ans
                if s.isalpha() and N_TURNS>0:
                    print('You win!')
                    print('The word was: ' + str(r))
                    break
            else:
                incorrect += 1
                print("There is no " + str(a) + "'s in the word.")
                if incorrect > N_TURNS-1:
                    print('You are completely hung: (')
                    print('The word was: '+str(r))
                    break
            print('The word looks like: ' + str(s))
            print('You have ' + str(N_TURNS - incorrect) + ' left.')


def random_word():
    num = random.choice(range(9))
    if num == 0:
        return "NOTORIOUS"
    elif num == 1:
        return "GLAMOROUS"
    elif num == 2:
        return "CAUTIOUS"
    elif num == 3:
        return "DEMOCRACY"
    elif num == 4:
        return "BOYCOTT"
    elif num == 5:
        return "ENTHUSIASTIC"
    elif num == 6:
        return "HOSPITALITY"
    elif num == 7:
        return "BUNDLE"
    elif num == 8:
        return "REFUND"


#####  DO NOT EDIT THE CODE BELOW THIS LINE  #####
if __name__ == '__main__':
    main()
