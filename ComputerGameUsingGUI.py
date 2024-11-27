import tkinter as tk
import random

class ColorGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Color Game")
        self.user_points = 0
        self.user_color = None
        self.timer_id = None

        # Initialize UI elements
        self.setup_ui()
        self.restart_game()  # Start a new game

    def setup_ui(self):
        # Title Label
        self.label = tk.Label(self.root, text="Choose a color! If the computer guesses this color, you lose all of your points. Keep going and earn more points if the computer keeps guessing wrong.", wraplength=400)
        self.label.grid(row=0, column=0, columnspan=3, pady=20, padx=20)

        # Frame for color buttons
        self.button_frame = tk.Frame(self.root)
        self.button_frame.grid(row=1, column=0, columnspan=3, pady=10, padx=20)

        # Color buttons
        self.options = ['red', 'orange', 'blue', 'green', 'purple', 'black', 'yellow', 'brown', 'pink']
        self.buttons = [tk.Button(self.button_frame, text=color, command=lambda color=color: self.main_game(color)) for color in self.options]
        for index, button in enumerate(self.buttons):
            button.grid(row=index // 3, column=index % 3, padx=10, pady=10)

        # Result and Status Labels
        self.result_label = tk.Label(self.root, text="", wraplength=400)
        self.result_label.grid(row=4, column=0, columnspan=3, pady=5)

        self.timer_label = tk.Label(self.root, text="")
        self.timer_label.grid(row=5, column=0, columnspan=3, pady=10)

        self.keep_going_label = tk.Label(self.root, text="")
        self.keep_going_label.grid(row=6, column=0, columnspan=3, pady=5)

        # Play Again, Yes, and Quit Buttons
        self.yes_button = tk.Button(self.root, text="Yes", command=self.continue_game, state=tk.DISABLED)
        self.yes_button.grid(row=7, column=1, pady=10)

        self.play_again_button = tk.Button(self.root, text="Play Again?", command=self.restart_game, state=tk.DISABLED)
        self.play_again_button.grid(row=3, column=1, pady=10)

        self.quit_button = tk.Button(self.root, text="Quit", command=self.quit_game)
        self.quit_button.grid(row=2, column=1, pady=10)


    def restart_game(self):
        self.user_color = None
        self.user_points = 0
        self.guessed_colors = set()
        self.enable_buttons()
        self.result_label.config(text="")
        self.timer_label.config(text="")
        self.keep_going_label.config(text="")
        self.play_again_button.config(state=tk.DISABLED)
        self.yes_button.config(state=tk.DISABLED)
        self.cancel_timer()

    def enable_buttons(self):
        for button in self.buttons:
            button.config(state=tk.NORMAL)

    def disable_buttons(self):
        for button in self.buttons:
            button.config(state=tk.DISABLED)

    def timer(self, seconds):
        if seconds > 0:
            self.timer_label.config(text=f"Game will automatically close in {seconds} seconds")
            self.timer_id = self.root.after(1000, self.timer, seconds - 1)
        else:
            self.quit_game()

    def cancel_timer(self):
        if self.timer_id:
            self.root.after_cancel(self.timer_id)
            self.timer_id = None

    def main_game(self, color):
        if self.user_color is None:
            self.user_color = color

        self.disable_buttons()
        self.computer_choice = random.choice([c for c in self.options if c not in self.guessed_colors])

        if self.computer_choice == self.user_color:
            self.result_label.config(text="The computer guessed your color! You lost all of your points!")
            self.keep_going_label.config(text="Play Again? or 'Quit?'")
            self.timer(10)
            self.play_again_button.config(state=tk.ACTIVE)
            self.yes_button.config(state=tk.DISABLED)
        else:
            self.guessed_colors.add(self.computer_choice)
            self.user_points += 10
            self.result_label.config(text=f"You chose {self.user_color}. Computer guessed {self.computer_choice}. You received {self.user_points} points")
            self.keep_going_label.config(text="Do you want the computer to guess again? Press 'Yes', or 'Quit' to leave")
            self.yes_button.config(state=tk.ACTIVE)

    def continue_game(self):
        self.computer_choice = random.choice([c for c in self.options if c not in self.guessed_colors])

        if self.computer_choice == self.user_color:
            self.result_label.config(text=f"The computer guessed your color '{self.user_color}'! You lost all of your points!")
            self.keep_going_label.config(text="Play Again? or 'Quit?'")
            self.timer(10)
            self.play_again_button.config(state=tk.ACTIVE)
            self.yes_button.config(state=tk.DISABLED)
        else:
            self.guessed_colors.add(self.computer_choice)
            self.user_points += 10
            self.result_label.config(text=f"You chose {self.user_color}. Computer guessed {self.computer_choice}. You received {self.user_points} points")
            self.keep_going_label.config(text="Do you want the computer to guess again? Press 'Yes', or 'Quit' to leave")
            self.yes_button.config(state=tk.ACTIVE)

    def quit_game(self):
        self.root.destroy()

# Create the main window and run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = ColorGame(root)
    root.mainloop()

















