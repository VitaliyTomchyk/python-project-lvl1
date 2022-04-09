from brain_games.scripts.games_logic import victory
from brain_games.scripts.games_logic import answer_getter
from brain_games.scripts.games_logic import checker
from brain_games.scripts.games_logic import rules
from brain_games.scripts.games_logic import welcome_user
from random import randint


def operation_generator():
    fnum = randint(1, 20)
    snum = randint(1, 20)
    operator = randint(1, 3)
    if operator == 1:
        user_answer = answer_getter(f"{fnum} + {snum}")
        correct_answer = fnum + snum
    elif operator == 2:
        user_answer = answer_getter(f"{fnum} * {snum}")
        correct_answer = fnum * snum
    else:
        if fnum < snum:
            user_answer = answer_getter(f"{snum} - {fnum}")
            correct_answer = snum - fnum
        else:
            user_answer = answer_getter(f"{fnum} - {snum}")
            correct_answer = fnum - snum
    return [checker(str(correct_answer), str(user_answer)),
            correct_answer, user_answer]


def game_play():
    name = welcome_user()
    rules("What's the result of the expression?")
    i = 0
    while i < 3:
        result = operation_generator()
        if result[0] is True:
            print('Correct!')
            i = i + 1
        else:
            return print((f"'{result[2]}' is wrong answer ;(.\
 Correct answer was '{result[1]}'.\nLet's try again, {name}!"))
    else:
        return victory(name)


def main():
    game_play()


if __name__ == '__main__':
    main()
