import random

print("Password Generator\n")

characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@$%&*().,?0123456789'
number = input('How many passwords we should generate for you?: ')
number = int(number)

length = input('What should be the length of your passwords?: ')
length = int(length)

print('\nGenerated Passwords: ')

for pwd in range(number):
    passwords = ''
    for c in range(length):
      passwords += random.choice(characters)
    print(passwords)