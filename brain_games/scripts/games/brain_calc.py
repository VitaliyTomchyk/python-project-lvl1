from brain_games.scripts.games_logic import *
from random import randint


def operation_generator():
    fnum = randint(1, 20)
    snum = randint(1, 20)
    operator = randint(1, 3)
    if operator == 1:
        user_answer = answer_getter(f"{fnum} + {snum}")
        correct_answer = fnum + snum
        return checker(correct_answer, user_answer)
    elif operator == 2:
        user_answer = answer_getter(f"{fnum} * {snum}")
        correct_answer = fnum * snum
        return checker(correct_answer, user_answer)
    else:
        if fnum < snum:
            user_answer = answer_getter(f"{snum} - {fnum}")
            correct_answer = snum - fnum
            return checker(correct_answer, user_answer)
        else:
            user_answer = answer_getter(f"{fnum} - {snum}")
            correct_answer = fnum - snum
            return checker(correct_answer, user_answer)

def game_play():
    name = welcome_user()
    rules("What's the result of the expression?")
    i = 0
    while i < 3:
        game
        i = i + 1 in case correct


game_play()