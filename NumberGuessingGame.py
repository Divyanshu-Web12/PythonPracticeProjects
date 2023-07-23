import random


def guess_number(max_num):
    min_num = 1
    guess = random.randint(min_num, max_num)

    feedback = ''
    while feedback != 'c':
        print("Computer's guess is : " + str(guess))
        feedback = input("Is the guess high h, low l or correct c ? ")
        if feedback == 'h':
            guess = guess - 1
        elif feedback == 'l':
            guess = guess + 1
        elif feedback == 'c':
            print("Computer's guess is correct !!")


guess_number(10)
