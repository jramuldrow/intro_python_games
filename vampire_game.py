import random
import time

def displayIntro():
    print('''You are transporated back to the time of NOSFERATU
aka, Vampire swamp lands. You have two choices and a desire for immortality.
You can either live forever with riches or die trying, as there are two vampires one to
grant your wish and one to drain your blood. Pick the right castle...''')
    print()

def chooseCastle():
    castle = ''
    while castle!= '1' and castle != '2':
        print('Which Castle will you go into? (1 or 2)')
        castle = input()

    return castle

def CheckCastle(chooseCastle):
    print('You enter the Castle ...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('You look up the sprial staircase, illuminated by many candles')
    time.sleep(2)
    print('A dark figure reveals themselve to you, its a vampire and...')
    print()
    time.sleep(2)

    friendlyCave = random.randint(1, 2)

    if chooseCastle == str(friendlyCave):
        print('They granted you the gift of immortality with a sweet kiss on the neck!')
    else:
        print('They do not like you and bited you on the neck. Drianing your blood!')

playAgain = 'yes'
while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    castleNumber = chooseCastle()
    CheckCastle(castleNumber)

    print('Do you want to play again? (yes or no)')
    playAgain = input()
