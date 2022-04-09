import random
from random import randint
from brain_games.scripts.games_logic import victory, welcome_user
from brain_games.scripts.games_logic import rules
from brain_games.scripts.games_logic import answer_getter
from brain_games.scripts.games_logic import checker


def progression_generator():
    value = randint(1, 99)
    sum_number = randint(1, 20)
    ListOfNumbers = [value]
    for i in range(0, 9):
        value = value + sum_number
        ListOfNumbers.append(value)
    return ListOfNumbers[0:9]


def question_maker():
    result = ''
    progression = progression_generator()
    correct_answer = random.choice(progression)
    i = 0
    while i < 9:
        if correct_answer == progression[i]:
            result = result + ('.. ')
            i = i + 1
        else:
            result = result + (str(progression[i]) + ' ')
            i = i + 1
    return result, str(correct_answer)


def gameplay():
    name = welcome_user()
    rules('What number is missing in the progression?')
    i = 0
    while i < 3:
        question = question_maker()
        user_answer = answer_getter(question[0])
        if checker(question[1], user_answer):
            print('Correct!')
            i = i + 1
        else:
            return print(f"'{user_answer}' is wrong answer ;(.\
 Correct answer was '{question[1]}'.\nLet's try again, {name}!")
    return victory(name)


def main():
    gameplay()


if __name__ == '__main__':
    main()
