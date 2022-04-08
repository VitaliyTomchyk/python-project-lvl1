import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def rules(rule):
    print(rule)


def answer_getter(game_question):
    user_answer = prompt.string('Question: ' + game_question 
                                + '\nYour answer: ')
    return user_answer


def checker(correct_answer, user_answer):
    if user_answer == correct_answer:
        return True
    else:
        return False


def lost_game(user_answer, correct_answer):
    print(f"'{user_answer}' is wrong answer ;(.\
Correct answer was '{correct_answer}'.\
\nLet's try again, {name}!")


def victory(name):
    print(f'Congratulations, {name}!')

