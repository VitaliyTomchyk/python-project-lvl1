from brain_games.scripts.games_logic import answer_getter
from brain_games.scripts.games_logic import rules
from brain_games.scripts.games_logic import victory
from brain_games.scripts.games_logic import welcome_user
from brain_games.scripts.games_logic import checker
from random import randint


def number_creator():
    fnum = randint(2, 100)
    snum = randint(2, 100)
    question = (f'{fnum} {snum}')
    return fnum, snum, question


def gcd(fnum, snum):
    while snum:
        fnum, snum = snum, fnum % snum
    correct_answer = str(fnum)
    return correct_answer


def gameplay():
    name = welcome_user()
    rules('Find the greatest common divisor of given numbers.')
    i = 0
    while i < 3:
        nums = number_creator()
        correct_answer = gcd(nums[0], nums[1])
        user_answer = answer_getter(nums[2])
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
