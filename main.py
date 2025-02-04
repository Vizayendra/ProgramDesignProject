# ************************************************************************* 
# Program: main.py 
# Course: CSP1114 PROBLEM SOLVING AND PROGRAM DESIGN 
# Lecture / Lab Section: TC1L / TL7L 
# Trimester: 2430 
# Names: Zul Fadhli Bin Zaiman | Vizayendra A/L Mogan
# IDs: 241FC24001 | 241FC240K1  
# Emails: ZUL.FADHLI.BIN.ZAIMAN@student.mmu.edu.my | VIZAYENDRA.MOGAN@student.mmu.edu.my
# *************************************************************************
import random
import time
import os
import json

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

def save_game(username, difficulty, secret_word, attempts, guesses):
    game_data = {
        'username': username,
        'difficulty': difficulty,
        'secret_word': secret_word,
        'attempts': attempts,
        'guesses': guesses
    }
    save_dir = 'saves'
    save_file = f"{username}_checkpoint.json"
    full_path = os.path.join(save_dir, save_file)
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
        print(f"Save directory '{save_dir}' created.")
    try:
        with open(full_path, 'w') as f:
            json.dump(game_data, f, indent=4)
        print(f"Game saved successfully for {username} at {full_path}.")
    except Exception as e:
        print(f"Error saving game: {e}")

def load_game(username):
    save_dir = 'saves'
    save_file = f"{username}_checkpoint.json"
    full_path = os.path.join(save_dir, save_file)
    if os.path.exists(full_path):
        try:
            with open(full_path, 'r') as f:
                game_data = json.load(f)
            required_fields = {'username', 'difficulty', 'secret_word', 'attempts', 'guesses'}
            if required_fields.issubset(game_data.keys()):
                print(f"Game loaded successfully for {username}.")
                return game_data
            else:
                print("Error: Saved game file is missing some required fields.")
                return None
        except Exception as e:
            print(f"Error loading game: {e}")
            return None
    else:
        print(f"No saved game found for {username} at {full_path}.")
        return None

def check_place(char_g, char_w, place, wordle):
    if char_g == char_w:
        return f"{place} letter: right letter, right place!"
    elif char_g in wordle:
        return f"{place} letter: right letter, wrong place."
    else:
        return f"{place} letter: wrong letter."

def game_over():
    print("Thank you for playing Wordle!")
    print("Goodbye!")
    print("End of program.")

while True:
    ready = input(f"Are you ready, " + username.capitalize() +"? Y/N (cap-sensitive): ")
    if ready == "Y":
        print("Great! Let's start!")
        while True:
            load = input("Would you like to load a saved game? (Y/N) ")
            if load == "Y":
                loaded_game = load_game(username)
                if loaded_game is not None:
                    wordle = loaded_game['secret_word']
                    guesses = loaded_game['guesses']
                    attempts = loaded_game['attempts']
                    for guess_num in range(1, attempts + 1):
                        print(f"Attempt {guess_num}: {guesses[guess_num - 1]}")
                    print("Game loaded successfully.")
                    break  # Break out of the inner loop after loading the game
                else:
                    print("Error loading game. Please try again.")
                    continue
            elif load == "N":
                print("That's okay! Let's start a new game.")
                try:
                    with open("MMU_wordle.txt", "r") as file:
                        words = file.read().splitlines()
                except FileNotFoundError:
                    print("Error: 'MMU_wordle.txt' not found. Please ensure the file is in the same directory.")
                    break
                
                wordle = random.choice([word for word in words if len(word) == 5])  # Ensure the chosen word is 5 letters long
                guesses = []  # Initialize an empty list to store guesses
                attempts = 0  # Initialize attempts
                break
            else:
                print("Invalid input! Please try again.")
        
        while True:
            guess = input("Enter a word: ")
            while len(guess) != 5:
                print("Invalid input! Please try again.")
                guess = input("Enter a word: ")

            guesses.append(guess)  # Add the guess to the list of guesses
            attempts += 1  # Increment attempts

            if guess == wordle:
                print("Congratulations! You have guessed the word correctly!")
                game_over()
                break

            feedback = []
            feedback.append(check_place(guess[0], wordle[0], "First", wordle))
            feedback.append(check_place(guess[1], wordle[1], "Second", wordle))
            feedback.append(check_place(guess[2], wordle[2], "Third", wordle))
            feedback.append(check_place(guess[3], wordle[3], "Fourth", wordle))
            feedback.append(check_place(guess[4], wordle[4], "Fifth", wordle))

            for fb in feedback:
                print(fb)

            # Save the game state after each guess
            save_game(username, 'normal', wordle, attempts, guesses)

            if attempts == 6 and guess != wordle:
                print(f"You have used up your guesses. The Wordle was " + wordle)
                print("Try again next time!")
                break
    elif ready == "N":
        print("That's okay! Take your time.")
    else:
        print("Invalid input! Please try again.")