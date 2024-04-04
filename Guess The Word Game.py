import random

name = input("Enter your name! ")

print("Good Luck !" , name)

char = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


word = random.choices(char)

print('Guess the character')

guesses = ''

turns = 10

while turns > 0:
    failed = 0

    for char in word:
        if char in guesses:
            print(char)

        else:
            print("(ツ)")    
            
            failed += 1

    if failed == 0:

        print("You Win")

        print("The word is:" , word)
        break        

    guess = input('guess a character:')

    guesses += guess

    if guess not in word:

        turns -= 1

        print("wrong")

        print("You have", + turns, 'more guesses')

        if turns == 0:
            print("Char is: ",word)
            print('You Loose')
