import tkinter as tk
from random import randint

class GuessingGame:
    def __init__(self, root):

        self.number_of_tries = 3

        self.root = root
        self.root.title("Guessing Game")

        self.quit_button = tk.Button(root, text="Quit", command=self.quit_game)
        self.quit_button.grid(row=3, column=0, columnspan=5, pady=10)

        self.label = tk.Label(root, text="Enter a number 1-10. You have 3 tries to get it")
        self.label.grid(row=0, column=0, columnspan=5, pady=10)

        self.target_number = str(randint(1,11))

        buttons = []
        for i in range(1, 11):
            button = tk.Button(root, text=str(i), command=lambda num=i: self.play(str(num)))
            buttons.append(button)


        for i, button in enumerate(buttons):
            button.grid(row=1 + i//5, column=i%5, padx=10, pady=20)

        self.result_label = tk.Label(root, text="")
        self.result_label.grid(row=4, column=0, columnspan=5, pady=30)

        self.timer_label = tk.Label(root, text="")
        self.timer_label.grid(row=5, column=0, columnspan=5, pady=30)

    def quit_game(self):
        self.play("Quit")
        self.root.destroy()

    def play(self, guess):
        if guess == self.target_number:
            self.result_label.config(text=f"Correct! The number was {guess}")
            self.disable_buttons()
        else:
            self.number_of_tries -= 1
            self.result_label.config(text=f"Incorrect! You have {self.number_of_tries} tries left")
            if self.number_of_tries < 1:
                self.result_label.config(text=f"You lost! The correct number was {self.target_number}")
                self.disable_buttons()
                self.timer_label.config(text="Game will automatically close in 5 seconds")
                self.timer(5)

    def disable_buttons(self):
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Button) and widget != self.quit_button:
                widget.config(state=tk.DISABLED)

    def timer(self, seconds):
        if seconds > 0:
            self.timer_label.config(text=f"Game will automatically close in {seconds} seconds")
            self.root.after(1000, self.timer, seconds - 1)
        else:
            self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    game = GuessingGame(root)
    root.mainloop()