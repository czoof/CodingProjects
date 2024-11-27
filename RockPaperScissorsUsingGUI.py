import random
import tkinter as tk

class RPSGame:
    def __init__(self, root):
        self.user_wins = 0
        self.computer_wins = 0
        self.options = ['rock', 'paper', 'scissors']

        self.root = root
        self.root.title("Rock-Paper-Scissors Game")

        self.label = tk.Label(root, text="Choose Rock, Paper, or Scissors")
        self.label.pack(side=tk.LEFT, padx=20)

        self.rock_button = tk.Button(root, text="Rock", command=lambda: self.play('rock'))
        self.rock_button.pack(side=tk.LEFT, padx=20)

        self.paper_button = tk.Button(root, text="Paper", command=lambda: self.play('paper'))
        self.paper_button.pack(side=tk.LEFT, padx=20)

        self.scissors_button = tk.Button(root, text="Scissors", command=lambda: self.play('scissors'))
        self.scissors_button.pack(side=tk.LEFT, padx=20)

        self.result_label = tk.Label(root, text="")
        self.result_label.pack(pady=20)

        self.score_label = tk.Label(root, text=f"User Wins: {self.user_wins} | Computer Wins: {self.computer_wins}")
        self.score_label.pack(pady=10)

        self.quit_button = tk.Button(root, text="Quit", command=root.quit)
        self.quit_button.pack(pady=10)

    def play(self, user_choice):
        computer_choice = random.choice(self.options)
        result = ""

        if user_choice == computer_choice:
            result = "It's a tie!"
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            result = "You Win!"
            self.user_wins += 1

        else:
            result = "Computer Wins"
            self.computer_wins += 1

        self.result_label.config(text=f"You chose {user_choice}, computer chose {computer_choice}. {result}")
        self.score_label.config(text=f"User wins: {self.user_wins} | Computer wins: {self.computer_wins}")

if __name__ == "__main__":
    root = tk.Tk()
    game = RPSGame(root)
    root.mainloop()



