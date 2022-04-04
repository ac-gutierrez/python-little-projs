# Bagels:

# Pico, Fermi, Bagels
# Pico -  one digit is correct but in the wrong position
# Fermi - One digit is correct and in the right position
# Bagels - no digit is correct

num_digits = 3
max_guess = 10

import random

def main():
    print("Bagels by Al Sweigart")
    print("I am thinking of a three-digit number, try guessing it.")
    print("Pico = One digit is correct but in the wrong position. /n Fermi=one digit is correct but in the right position /n Bagels = No digit is correct")

    while True:
        secretNum = getSecretNum()
        print('What number is in my mind?')
        print('You have {} guesses to get it.'.format(max_guess))

        numGuesses = 1

        while numGuesses <= max_guess:
            guess=''
            while len(guess) != num_digits or not guess.isdecimal():
                print('Guess #{}:'.format(numGuesses))
                guess = input('> ')

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break
            if numGuesses > max_guess:
                print('No guess left')
                print('The answer was {}'.format(secretNum))

        print('Play again?')
        if not input('>').lower().startswith('y'):
            break
    print('Thanks for playing')

def getSecretNum():
    """ Returns a string made up of num_digits unique random digits."""
    numbers = list('01234566789')
    random.shuffle(numbers)

    # Get the first num_digits digits in the list for the secret number:

    secretNum = ''
    for i in range(num_digits):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    """Returns a string with the pico, fermi, bagels clues for a guess and secret number pair."""
    if guess == secretNum:
        return 'You got it!'

    clues = []
    for i in range(len(guess)):
        if guess[i] == secretNum[i]:  # A correct digit is in the right place
            clues.append('Fermi')
        elif guess[i] in secretNum:  # A correct digit is in the incorrect place
            clues.append('Pico')

    if len(clues) == 0:
        return 'Bagels'  # There are no correct digits
        clues.sort()
        return ''.join(clues)
    else:
        clues.sort()
        return ''.join(clues)

if __name__ == '__main__':
    main()

