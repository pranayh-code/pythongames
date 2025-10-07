# number guesing game

#user input asking pick a number from 1-10:


import random

def inpute():
    while True:
        x = input('Select number from 1-10: ')
        if x.isdigit():
            x = int(x)
            if 1 <= x <= 10:
                print(f"You guessed number {x}")
                return x
            else:
                print('Number must be between 1-10.')
        else:
            print('Enter a number.')


def randomizze():
    return random.randint(1, 10)



def wanna():

	jj = input('Do you wanna play again!? y/n \n').lower()

	while True:
		if jj == 'y':
			return True
		elif jj == 'n':
			return False
		else:
			print('enter y for yes and n for no')


def gameplay(x,y):

	if x == y:
		print('You are guessed correct. Well Done!! ')
	else:
		print(f'Your guess is wrong: The correct guess was {y}')



if __name__ == '__main__':
	game_on = True
	while game_on:

		user_input = inpute()
		randomized_value = randomizze()
		gameplay(user_input,randomized_value)
		game_on = wanna()










