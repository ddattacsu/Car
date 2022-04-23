#Testing
secret_number = 3
guess_limit = 3
count = 0


while count < guess_limit:
    guess_number = int(input('Please guess a number between 1 to 9: '))
    #guess_number = int(guess_number)
    count = count + 1
    if guess_number == secret_number:
       print('Congratutation! You Win!')
       break

else:
    print('You loss')

