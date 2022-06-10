#This is a guess the number game. Basic learning python while building fun games. 
import random
import time

guessesTaken = 0

print('Hello! What is your name?')
myName = input()

number = random.randint(1, 100) #randomly picks a number from 1 through 20
print('Well, ' + myName + ', I am thinking of a number between 1 and 100.')
time.sleep(2)
print('Can you guess what it is?')
time.sleep(2)

for i in range(10):
    print('Take a guess.') #player takes a guess about the numnber
    guess = input()
    guess = int(guess)

    if guess < number:
        print('Your guess is too low.')

    if guess > number:
        print('Your guess is to high.')
    
    if guess == number:
        break

if guess == number:
    guessesTaken = str(guessesTaken)
    print('Good job, ' + myName + '! You guessed my number in ' + guessesTaken + ' guesses!')

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was ' + number + '.')
