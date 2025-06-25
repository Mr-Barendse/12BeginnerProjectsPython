import logging
import random


def guess_user(x):
    guess = random.randint(1,x)
    while True:
        user = int(input("Please enter a number!"))
        if user > guess:
            print('Guess is too high!')
        elif user < guess:
            print('Guess is too small!')
        else:
            print('Correct guess!')
            return False

def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low,high)
        else:
            guess = low
        feedback = input(f'Is {guess} too High (H) or Too Low (l) or Correct (C)').lower()
        if feedback == 'h':
            high = guess -1
        elif feedback == 'l':
            low = guess + 1
    print('You guess the correct number !')


computer_guess(12)





