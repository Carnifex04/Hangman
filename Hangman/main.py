#importing modules
import random
from hangman_words import word_list
from hangman_art import logo,stages

#selecting a random word from the word_list in hangman_words.py
chosen_word = random.choice(word_list)
length = len(chosen_word)

#initializing a boolean variable to keep track of the game, and a remaining lives counter
end_of_game = False
lives = 6

#Printing the Welcome Screen
print("Welcome to")
print(logo)
print("\n" + stages[0])

#Testing code
#print(f'Pssst, the solution is {chosen_word}.')

#Creating blanks
display = ["_"]*length
print(f"{' '.join(display)}\n")

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    #If the user has entered a letter they've already guessed, printing the letter and letting them know.
    if guess in display:
      print(f"You have already guessed the letter '{guess}'. Please guess a new letter...")
      print(stages[6-lives])
      print(f"{' '.join(display)}")
      continue

    #Checking guessed letter
    letter_found=False
    for position in range(length):
        if chosen_word[position] == guess:
            display[position] = chosen_word[position]
            letter_found=True

    #Checking if user is wrong.
    if not letter_found:
      lives-=1
      print(f"The letter '{guess}' is not present in the word. Guess Again...")
    else:
      print(f"You guessed correct. The letter '{guess}' is present in the word")

    #printing the ASCII art of hangman stages
    print(stages[6-lives])

    #Joining all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}\n")

    #Checking if user has got all letters.
    if lives==0:
      end_of_game=True
      print(f"The word was '{chosen_word}'")
      print("The Hangman died. You Lose :(")
    if "_" not in display:
        end_of_game = True
        print(f"The word was '{chosen_word}'")
        print("You saved the Hangman. You win!!!")

    