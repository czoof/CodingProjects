# This program is an interactive command-line interface that allows users to create an account, generate a strong password, and play various games.
# The program includes the following games: Computer Color Game, Rock Paper Scissors, and a Guessing Game.
# Users must enter a valid email address and create a strong password before they can access the games.

import sys
import subprocess
import string
import random

def games_to_play():
    # Function to select and run a game based on user input
    user_input = input(
        "What game do you want to play: 1:Computer Color Game? 2:Rock Paper Scissors? 3:Guessing Game? Type 1/2/3 to choose ")
    if user_input == "1":
        subprocess.run(["python", "ComputerGameUsingGUI.py"])  # Run Computer Color Game
        sys.exit()
    if user_input == '2':
        subprocess.run(["python", "RockPaperScissorsUsingGUI.py"])  # Run Rock Paper Scissors
        sys.exit()
    if user_input == '3':
        subprocess.run(["python", "GuessingGameUsingGUI.py"])  # Run Guessing Game
        sys.exit()

def email():
    # Function to validate email address
    needed_signs = ["@", "."]
    while True:
        email_input = (input("Enter your email address "))
        if all(sign in email_input for sign in needed_signs):
            strong_password()  # If valid email, proceed to password creation
            return
        else:
            print("Invalid email address. Please try again")

def strong_password():
    # Function to create a strong password or allow user to enter their own
    user_input = input("Strong password? type 'yes' or 'no' to make your own password ").lower()
    if user_input == 'no':
        while True:
            custom_password = input("Enter a custom password ")
            if (any(char in custom_password for char in '!@#$%^&*()_+-=') and
                any(char.isupper() for char in custom_password) and
                any(char.isdigit() for char in custom_password) and
                len(custom_password) >= 7):
                games_to_play()  # If custom password is strong, proceed to game selection
                return
            else:
                print("Password must be at least 7 digits long, contain an uppercase letter, number, and special character ex: %,$,#")

    if user_input == 'yes':
        # Generate a strong password if user chooses
        chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + '!@#$%^&*()_-+='
        password = ''.join(random.choice(chars) for _ in range(16))
        print(f"Your password: {password}")
        while True:
            x = input("Enter the generated password ")
            if x == password:
                games_to_play()  # If user enters generated password correctly, proceed to game selection
                return
            else:
                print("Please enter the correct password")

def main():
    # Main function to start the program
    while True:
        print("Welcome to Landco, create an account to access our games.")
        x = input("Press 'enter' to continue ")
        if x != "":
            continue
        else:
            email()  # Proceed to email validation

main()
