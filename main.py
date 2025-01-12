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
import os
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
ready = input(f"Are you ready, " ,username.capitalize(), "? Y/N (cap-sensitive): ")

