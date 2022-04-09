from random import randint
from brain_games.scripts.games_logic import (answer_getter, checker,
                                             victory, welcome_user, rules)


def prime():
    num = randint(2, 1000)
    i = 2
    while i < num:
        if num % i != 0:
            i = i + 1
        else:
            return False, num
    return True, num


def gameplay():
    name = welcome_user()
    rules('Answer "yes" if given number is prime. Otherwise answer "no".')
    i = 0
    while i < 3:
        question = prime()
        user_answer = answer_getter(str(question[1]))
        if question[0] is True:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        if user_answer == ('yes'):
            user_answer is True
        elif user_answer == ('no'):
            user_answer is False
        else:
            return print(f"'{user_answer}' is wrong answer ;(. \
Correct answer was '{correct_answer}'.\nLet's try again, {name}!")
        if checker(correct_answer, user_answer):
            print('Correct!')
            i = i + 1
        else:
            return print(f"'{user_answer}' is wrong answer ;(. \
Correct answer was '{correct_answer}'.\nLet's try again, {name}!")
    return victory(name)


def main():
    gameplay()


if __name__ == '__main__':
    main()
