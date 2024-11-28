# This program creates a number guessing game using the tkinter library for the graphical user interface (GUI). 
# The game allows the user to guess a number between 1 and 10, and the user has 3 tries to guess the correct number.
# If the user guesses correctly, a message is displayed, and the buttons are disabled. 
# If the user does not guess correctly within the allotted tries, the correct number is revealed, and the game automatically closes after a countdown.

import tkinter as tk
from random import randint

class GuessingGame:
    def __init__(self, root):
        self.number_of_tries = 3  # Number of attempts the user has

        self.root = root
        self.root.title("Guessing Game")  # Set the title of the window

        # Quit button to exit the game
        self.quit_button = tk.Button(root, text="Quit", command=self.quit_game)
        self.quit_button.grid(row=3, column=0, columnspan=5, pady=10)

        # Instruction label
        self.label = tk.Label(root, text="Enter a number 1-10. You have 3 tries to get it")
        self.label.grid(row=0, column=0, columnspan=5, pady=10)

        # Target number to be guessed
        self.target_number = str(randint(1, 11))

        buttons = []
        # Create number buttons from 1 to 10
        for i in range(1, 11):
            button = tk.Button(root, text=str(i), command=lambda num=i: self.play(str(num)))
            buttons.append(button)

        # Arrange buttons in a grid layout
        for i, button in enumerate(buttons):
            button.grid(row=1 + i // 5, column=i % 5, padx=10, pady=20)

        # Label to display the result of the guess
        self.result_label = tk.Label(root, text="")
        self.result_label.grid(row=4, column=0, columnspan=5, pady=30)

        # Label to display the countdown timer
        self.timer_label = tk.Label(root, text="")
        self.timer_label.grid(row=5, column=0, columnspan=5, pady=30)

    def quit_game(self):
        # Quit the game and close the window
        self.play("Quit")
        self.root.destroy()

    def play(self, guess):
        if guess == self.target_number:
            self.result_label.config(text=f"Correct! The number was {guess}")
            self.disable_buttons()  # Disable buttons if the guess is correct
        else:
            self.number_of_tries -= 1  # Decrement the number of tries
            self.result_label.config(text=f"Incorrect! You have {self.number_of_tries} tries left")
            if self.number_of_tries < 1:
                self.result_label.config(text=f"You lost! The correct number was {self.target_number}")
                self.disable_buttons()  # Disable buttons if no tries are left
                self.timer_label.config(text="Game will automatically close in 5 seconds")
                self.timer(5)  # Start the countdown timer

    def disable_buttons(self):
        # Disable all number buttons to prevent further guesses
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Button) and widget != self.quit_button:
                widget.config(state=tk.DISABLED)

    def timer(self, seconds):
        # Countdown timer to automatically close the game
        if seconds > 0:
            self.timer_label.config(text=f"Game will automatically close in {seconds} seconds")
            self.root.after(1000, self.timer, seconds - 1)
        else:
            self.root.destroy()  # Close the game window

# Create the main window and run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = GuessingGame(root)
    root.mainloop()
