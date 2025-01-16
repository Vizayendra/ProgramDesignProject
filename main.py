# ************************************************************************* 
# Program: main.py 
# Course: CSP1114 PROBLEM SOLVING AND PROGRAM DESIGN 
# Lecture / Lab Section: TC1L / TL7L 
# Trimester: 2430 
# Names: Zul Fadhli Bin Zaiman | Vizayendra A/L V. Nadarajah
# IDs: 241FC24001 | 241FC240K1  
# Emails: ZUL.FADHLI.BIN.ZAIMAN@student.mmu.edu.my | VIZAYENDRA.MOGAN@student.mmu.edu.my
# *************************************************************************
import random
import time

print('Welcome to Wordle Game based on Python!')
time.sleep(1)

# Asks user for their name
username = input("What is your name? ")
print(f"Hello, " + username.capitalize() + "! The rules are simple: ")

# Explains the rules of the game
print("Enter a FIVE-LETTER word of that language.\nYou will be given feedback on the letters you have guessed.")
time.sleep(2.5)
print("The code will let you know if letters are correct\n and/or in the correct position.")
time.sleep(2)

# Asks user if they are ready to play
ready = input(f"Are you ready, " + username.capitalize() +"? Y/N (cap-sensitive): ")

while True:
    if ready == "Y":
        print("Great! Let's start!")
        try:
            with open("MMU_wordle.txt", "r") as file:
                words = file.read().splitlines()  # Read all lines and split into a list
        except FileNotFoundError:
            print("Error: 'MMU_wordle.txt' not found. Please ensure the file is in the same directory.")
            break
            # Chooses a random word as the Wordle
            wordle = random.choice(seq=words)

         # Defines the 'check for correct place' function
        def check_place(char_g, char_w, place):
            if char_g == char_w:
                print(place , " letter: right letter, right place!")
       
        # User's first guess
        guess = input("Enter a word: ")

        while len(guess) != 5:
                print("Invalid input! Please try again.")
                guess = input("Enter a word: ")

        # For loop repeats the guesses five more times for a total of six times
        for i in range(5):
            # Checks if the guess is correct
            if guess == wordle:
                print("Congratulations! You have guessed the word correctly!")
                break
            check_place(guess[0], wordle[0], "First")
            if guess[0] == wordle[1] or guess[0] == wordle [2] or guess[0] == wordle [3] or guess[0] == wordle[4]:
                print("First letter: right letter, wrong place.")

                check_place(guess[1], wordle[1], "Second")
            if guess[1] == wordle[0] or guess[1] == wordle [2] or guess[1] == wordle [3] or guess[1] == wordle[4]:
                print("Second letter: right letter, wrong place.")

                check_place(guess[2], wordle[2], "Third")
            if guess[2] == wordle[0] or guess[2] == wordle [1] or guess[2] == wordle [3] or guess[2] == wordle[4]:
                print("Third letter: right letter, wrong place.")

                check_place(guess[3], wordle[3], "Fourth")
            if guess[3] == wordle[0] or guess[3] == wordle [1] or guess[3] == wordle [2] or guess[3] == wordle[4]:
                print("Fourth letter: right letter, wrong place.")

                check_place(guess[4], wordle[4], "Fifth")
            if guess[4] == wordle[0] or guess[4] == wordle [1] or guess[4] == wordle [2] or guess[4] == wordle[3]:
                print("Fifth letter: right letter, wrong place.")

                 # Prints a "sorry" message if the user is unsuccessful
            if guess != wordle:
                print("You have used up your guesses. The Wordle was " + wordle + ".")
                print("Try again next time!")
                break
            else:
                # Checks if the guess is correct
                for i in range(5):
                    check_place(guess[i], wordle[i], i+1)
                # User's next guess
                guess = input("Enter a word: ")
        break 
    elif ready == "N":
        print("That's okay! Take your time.")
        break
    else:
        print("Invalid input! Please try again.")
    break 
print("Thank you for playing Wordle!")
print("Goodbye!")
