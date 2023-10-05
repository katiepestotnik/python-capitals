from capitals import states
import random

#shuffle existing list
random.shuffle(states)
print("""
Welcome to guess the captial game!\n
Test your geography knowledge.\n 
See how many capitals you get correct.
""")
#dict to hold number of guesses, correct, wrong
guess_count = {
    'total': 0,
    'correct': 0,
    'wrong': 0,
    'game_count': 1
}
guess = None
play_again = None
total = guess_count['total']
correct = guess_count['correct']
wrong = guess_count['wrong']
game_count = guess_count['game_count']
def game_play(states, guess, total, correct, wrong, game_count):
    while(total < len(states)):
        for state in states:
            single_state = state['name']
            single_capital = state['capital']
            guess=input(f'Guess the capital of {single_state} or type \'quit\' to end game: ').title()
            if guess == state['capital']:
                correct += 1
                total += 1
                print('Yep! You are correct.')
                print(f'So far you have answered {correct} correctly out of {total} states.')
            else:
                wrong += 1
                total += 1
                print(f'Nope, wrongo! Correct anwer: {single_capital}')
                print(f'So far you have answered {wrong} incorrectly out of {total} states.')
    if(total == len(states)):
        re_play(guess, total, correct, wrong, play_again, game_count)
        print(f'Game {game_count} results. You got {correct} capitals correct out of {total} states.')

def re_play(guess, total, correct, wrong, play_again, game_count):
    print(game_count, 'in replay function')
    play_again = input("""
    Do you want to play again?
    Enter 'yes' to improve your score.
    Enter 'no' to end game.
    """).capitalize()
    if(play_again == 'Yes'):
        game_count += 1
        guess = None
        total = 0
        correct = 0
        wrong = 0
        game_play(states, guess, total, correct, wrong, game_count)
    else:
        print('Game end: see results below.')

game_play(states, guess, total, correct, wrong, game_count)

