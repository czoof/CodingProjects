# This program creates a Rock-Paper-Scissors game using the tkinter library for the graphical user interface (GUI).
# The user can choose rock, paper, or scissors, and the computer makes a random choice.
# The program keeps track of the number of wins for both the user and the computer.

import random
import tkinter as tk

class RPSGame:
    def __init__(self, root):
        self.user_wins = 0  # Initialize user win count
        self.computer_wins = 0  # Initialize computer win count
        self.options = ['rock', 'paper', 'scissors']  # Possible choices for the game

        self.root = root
        self.root.title("Rock-Paper-Scissors Game")  # Set the title of the window

        # Create and place the label that prompts the user to choose
        self.label = tk.Label(root, text="Choose Rock, Paper, or Scissors")
        self.label.pack(side=tk.LEFT, padx=20)

        # Create and place the rock button
        self.rock_button = tk.Button(root, text="Rock", command=lambda: self.play('rock'))
        self.rock_button.pack(side=tk.LEFT, padx=20)

        # Create and place the paper button
        self.paper_button = tk.Button(root, text="Paper", command=lambda: self.play('paper'))
        self.paper_button.pack(side=tk.LEFT, padx=20)

        # Create and place the scissors button
        self.scissors_button = tk.Button(root, text="Scissors", command=lambda: self.play('scissors'))
        self.scissors_button.pack(side=tk.LEFT, padx=20)

        # Create and place the result label
        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=20)

        # Create and place the score label
        self.score_label = tk.Label(root, text=f"User Wins: {self.user_wins} | Computer Wins: {self.computer_wins}")
        self.score_label.pack(pady=10)

        # Create and place the quit button
        self.quit_button = tk.Button(root, text="Quit", command=root.quit)
        self.quit_button.pack(pady=10)

    def play(self, user_choice):
        # Function to handle the game logic when a choice is made
        computer_choice = random.choice(self.options)  # Computer randomly chooses
        result = ""

        # Determine the result of the game
        if user_choice == computer_choice:
            result = "It's a tie!"
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            result = "You Win!"
            self.user_wins += 1  # Increment the user's win count
        else:
            result = "Computer Wins"
            self.computer_wins += 1  # Increment the computer's win count

        # Update the result and score labels
        self.result_label.config(text=f"You chose {user_choice}, computer chose {computer_choice}. {result}")
        self.score_label.config(text=f"User wins: {self.user_wins} | Computer wins: {self.computer_wins}")

if __name__ == "__main__":
    root = tk.Tk()  # Create the main Tkinter window
    game = RPSGame(root)  # Instantiate the RPSGame class
    root.mainloop()  # Start the Tkinter event loop



