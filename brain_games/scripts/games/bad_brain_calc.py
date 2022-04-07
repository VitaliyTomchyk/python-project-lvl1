import prompt
from random import randint


print("Welcome to the Brain Games!")
name = prompt.string('May I have your name? ')
print(f'Hello, {name}!\
\nWhat is the result of the expression?')


def question():
    question_made = 0
    while question_made < 3:
        fnum = randint(1, 30)
        snum = randint(1, 30)
        if question_made == 0:
            answer = fnum + snum
            print(f'Question: {fnum} + {snum}')
            player_answer = prompt.string('Your answer: ')
            if str(player_answer) == str(answer):
                print('Correct!')
                question_made = question_made + 1
            else:
                return print(f"'{player_answer}' is wrong answer ;(.\
 Correct answer was '{answer}'.\nLet's try again, {name}!")
        elif question_made == 1:
            if fnum < snum:
                answer = snum - fnum
                print(f'Question: {snum} - {fnum}')
            else:
                answer = fnum - snum
                print(f'Question: {fnum} - {snum}')
            player_answer = prompt.string('Your answer: ')
            if str(player_answer) == str(answer):
                print('Correct!')
                question_made = question_made + 1
            else:
                return print(f"'{player_answer}' is wrong answer ;(.\
 Correct answer was '{answer}'.\nLet's try again, {name}!")
        else:
            answer = fnum * snum
            print(f'Question: {fnum} * {snum}')
            player_answer = prompt.string('Your answer: ')
            if str(player_answer) == str(answer):
                print('Correct!')
                question_made = question_made + 1
            else:
                return print(f"'{player_answer}' is wrong answer ;(.\
 Correct answer was '{answer}'.\nLet's try again, {name}!")
    else:
        return print(f'Congratulations, {name}!')


def main():
    question()


if __name__ == '__main__':
    main()
