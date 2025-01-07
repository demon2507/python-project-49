import prompt
from random import randint

print("Welcome to the Brain Games!")
name = prompt.string("May I have your name? ")
print(f'Hello, {name}!')
print('Answer \"yes\" if the number is even, otherwise answer \"no\"')

def is_even(name):
    qwestion = 'Qwestion:'
    for _ in range(0, 3):
        number = randint(1, 100)
        is_number_even = 'no' if number % 2 != 0 else 'yes';
        print(f'{qwestion} {number}')
        answer = prompt.string('Your answer: ')
        if(answer == is_number_even):
            print('Correct!')
        else: 
            print(f'\'{answer}\' is wrong answer ;(. Correct answer was \'{is_number_even}\'.\nLet\'s try again, {name}!')
            return

    print(f'Congratulations, {name}!')


def main():    
    is_even(name)

if __name__ == '__main__':
    main()

        


        

    
