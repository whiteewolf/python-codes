import random

def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x} : '))
        if guess < random_number:
            print('Nop, number too low... ')
        elif guess > random_number:
            print('Nop, number too high...')

    print(f'WoW! Congrats! You have guessed the number {random_number}! You WIN')

# guess(10)

def computer(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c' and low != high:
        guess = random.randint(1, x)
        feedback = input(f"Is this the number {guess} ? Type 'l' for low, 'h' for high and 'c' for correct! : ")
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        elif feedback == 'c':
            print(f'Nice! I guessed the number! Win for me')

computer(10)