import prompt


def welcome_user():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def rules(rule):
    print(rule)


def tasks(game_question):
    task = prompt.string('Question: ' + game_question + '\nYour answer: ')
    return task


def checker(correct_answer, user_answer):
    user_answer == tasks()
    if user_answer == correct_answer:
        return True
    else:
        return False


def lost_game(message):
    print(message)


def victory(message):
    print(message)


def rounds():
    questions_made = 0
    while questions_made < 3:
        if checker == True:
            questions_made = questions_made + 1
            print('Correct!')
        else:
            questions_made = 3
            return print('NOOO')
    else:
        return print('NOOO')