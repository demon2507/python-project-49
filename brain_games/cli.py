import prompt


def welcome_user():
    name = ''
    while name == '': 
        print('May I have your name? ', end='') 
        name = prompt.string('May I have your name? ')
    print('Hello, ' + name + '!')








