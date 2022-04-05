import prompt
from random import randint


print("Welcome to the Brain Games!")
name = prompt.string('May I have your name? ')


def welcome_user():
    return print(f'Hello, {name}!\nAnswer "yes" if the number is even, otherwise answer "no".')
welcome_user()


def question():
    questions_made = 1
    num = randint(1, 99)
    even = (num % 2) == 0
    print(f'Question: {num}')
    player_answer = prompt.string('Your answer: ')
    if even:
        if player_answer == str('yes'):
            print('Correct!')
            questions_made = questions_made + 1
            if questions_made == 3:
                return (f'Congratulations, {name}!')
            else:
                return question()
        else:
            return print(f"'no' is wrong answer ;(. Correct answer was 'yes'.\nLet's try again, {name}!")
    else:
        if player_answer == str('no'):
            print('Correct!')
            questions_made = questions_made + 1
            if questions_made == 3:
                return (f'Congratulations, {name}!')
            else:
                return question()
        else:
            return print(f"'yes' is wrong answer ;(. Correct answer was 'no'.\nLet's try again, {name}!")
question()