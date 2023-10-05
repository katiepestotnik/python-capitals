if(total == len(states)):
    guess = input('Do you want to play again? \n Type \'yes\' to improve your score!\n Otherwise type \'no\' to quit.')
    if(guess == 'Yes'):
        total = 0
        correct = 0
        wrong = 0
    else:
        total = len(states)