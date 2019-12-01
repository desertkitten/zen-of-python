# Rock, Paper, Scissors
# Python 3.8
# Written by Cathy Whitteer
#
# This is a game of Rock, Paper, Scissors.
# This code is done with the book:
# Automate the Boring Suff with Python.
# This code also took a lot of searching the internet.
# Remember, Google is your friend.
# This is the gist:
# Rock vs Scissors: Rock wins because rock smashes scissors.
# Rock vs Paper: Paper wins because paper covers rock.
# Scissors vs Paper: Scissors win because scissors cut paper.
#
################################################

from random import randint


#Play options (did i for input):
i = ["Rock", "Paper", "Scissors"]

#Assign a random play to the computer:
computer = i[randint(0,2)]

#Set player to False
player = False

#The while loop:
while player == False:

#Set player to True
    player = input('Rock, Paper, Scissors?')
    if player == computer:
        print('We tied!')
    elif player == "Rock":
        if computer == "Paper":
            print('You lose!', computer, 'covers', player)
        else:
            print('You win!', player, 'smashes', computer)
    elif player == "Paper":
        if computer == "Scissors":
            print('You lose!', computer, 'cut', player)
        else:
            print('You win!', player, 'covers', computer)
    elif player == "Scissors":
        if computer == "Rock":
            print('You lose...', computer, 'smashes', player)
        else:
            print('You win!', player, 'cut', computer)
    else:
        print('What? Check your spelling!')
    #player was set to True because of error, we want player to be False so we continue loop
    player = False
    computer = i[randint(0,2)]
