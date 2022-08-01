import random

number = random.randrange(100)

# print(number)

while True:
    guess = int(input('Enter a number between 0-100 : '))

    if guess > number:
        print('A little lower...')
    elif guess < number:
        print('A little higher...')
    else:
        print('You are mind reader!!!')
        break
