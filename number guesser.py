import random

while True:
    print('Guess a number 1-9')
    answer = input('Enter a number (00 to quit)')
    num = random.randrange(1,10)
    answer = int(answer)
    if answer == 00:
        break
    elif answer > num:
        print('Number too big')
    elif answer < num:
        print('num too small')
    elif answer == num:
        print('You win!!!')
