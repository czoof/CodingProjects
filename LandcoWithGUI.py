# This program creates an interactive graphical user interface (GUI) using the tkinter library to allow users to create an account and access a selection of games.
# Users must enter a valid email address and create a strong password before they can play the games.
# The games available are Computer Color Game, Rock Paper Scissors, and Guessing Game.
# The program generates a strong password automatically or allows users to create their own password.

import random
import string
import tkinter as tk
import subprocess

class Landco:
   def __init__(self, root):
       self.root = root
       self.root.title('Landco')  # Set the title of the window
       self.needed_signs = ["@", "."]  # List of required characters in the email

       self.setup_ui()  # Initialize the user interface

       # Generate a strong password
       self.strong_password = string.ascii_letters + string.digits + "!@#$%^&*()-+="
       self.password = ''.join(random.choice(self.strong_password) for _ in range(1, 10))

   def setup_ui(self):
       # Create and place the labels and entry widgets in the window
       self.title_label = tk.Label(root, text="Welcome to Landco, create your account to access our games. Start by entering your email, then your password")
       self.title_label.grid(row=0, column=0, columnspan=3, pady=20, padx=20)

       self.email_and_password = tk.Label(root, text="Enter your email below")
       self.email_and_password.grid(row=1, column=0, columnspan=3, pady=20, padx=20)

       self.enter_email = tk.Entry(root, width=30)
       self.enter_email.grid(row=2, column=1, pady=20)
       self.enter_email.bind('<Return>', self.process_email)  # Bind Enter key to process_email method

       self.enter_password = tk.Entry(root, width=30)
       self.enter_password.grid(row=2, column=1, pady=20)
       self.enter_password.grid_remove()  # Initially hide the password entry widget

       self.enter_button = tk.Button(root, text="Enter", command=self.process_email)
       self.enter_button.grid(row=3, column=1, pady=20)

       self.strong_password_button = tk.Button(root, text="Strong Password?", command=self.generated_password)
       self.strong_password_button.grid(row=2, column=1, pady=20)
       self.strong_password_button.grid_remove()  # Initially hide the strong password button

       self.create_password_button = tk.Button(root, text="Create Own Password", command=self.create_own_password)
       self.create_password_button.grid(row=3, column=1, pady=20)
       self.create_password_button.grid_remove()  # Initially hide the create own password button

       self.computer_color_game_button = tk.Button(root, text="ComputerColorGame", command=self.computer_color_game)
       self.computer_color_game_button.grid(row=3, column=1, pady=20)
       self.computer_color_game_button.grid_remove()  # Initially hide the Computer Color Game button

       self.rock_paper_scissors_button = tk.Button(root, text="RockPaperScissors", command=self.rock_paper_scissors)
       self.rock_paper_scissors_button.grid(row=4, column=1, pady=20)
       self.rock_paper_scissors_button.grid_remove()  # Initially hide the Rock Paper Scissors button

       self.GuessingGameButton = tk.Button(root, text="GuessingGame", command=self.guessing_game)
       self.GuessingGameButton.grid(row=5, column=1, pady=20)
       self.GuessingGameButton.grid_remove()  # Initially hide the Guessing Game button

   def bind_enter_to_strong_password(self):
       # Unbind Enter key from the email entry and bind it to the strong password submission
       self.enter_email.unbind('<Return>')
       self.enter_password.bind('<Return>', self.submit_password)

   def bind_enter_to_user_password(self):
       # Unbind Enter key from the email entry and bind it to the user-defined password submission
       self.enter_email.unbind('<Return>')
       self.enter_password.bind('<Return>', self.submit_own_password)

   def process_email(self, event=None):
       email = self.enter_email.get()  # Get the email input
       if all(sign in email for sign in self.needed_signs):
           # Email is valid
           self.email_and_password.config(text=f"Email accepted. Use our strong password? Or Create your own password?")
           self.strong_password_button.grid()  # Show strong password button
           self.create_password_button.grid()  # Show create own password button
           self.enter_email.grid_remove()  # Hide email entry
           self.enter_button.config(command=self.generated_password)  # Set button command to generate password
       else:
           # Invalid email
           self.email_and_password.config(text="Please enter a valid email")

   def generated_password(self, event=None):
       # Set up the UI for strong password entry
       self.bind_enter_to_strong_password()
       self.enter_password.focus()  # Focus on password entry
       self.strong_password_button.grid_remove()  # Hide strong password button
       self.create_password_button.grid_remove()  # Hide create own password button
       self.enter_password.grid()  # Show password entry
       self.enter_button.config(command=self.submit_password)  # Set button command to submit password
       self.email_and_password.config(text=f"Enter your strong password: {self.password}")

   def submit_password(self, event=None):
       password = self.enter_password.get()  # Get the entered password
       if password == self.password:
           # Password is correct
           self.games_to_play()
       else:
           # Incorrect password
           self.email_and_password.config(text=f"Please enter the valid password {self.password}")

   def create_own_password(self, event=None):
       # Set up the UI for user-defined password entry
       self.bind_enter_to_user_password()
       self.strong_password_button.grid_remove()  # Hide strong password button
       self.create_password_button.grid_remove()  # Hide create own password button
       self.enter_password.grid()  # Show password entry
       self.enter_password.focus()  # Focus on password entry
       self.enter_button.config(command=self.submit_own_password)  # Set button command to submit own password
       self.email_and_password.config(text="Enter your password. Password must contain at least 7 characters, and at least one capital letter, number, and special character")

   def submit_own_password(self, event=None):
       own_password = self.enter_password.get()  # Get the entered own password
       if (any(char in own_password for char in '!@#$%^&*()_+-=') and
           any(char.isupper() for char in own_password) and
           any(char.isdigit() for char in own_password) and
           len(own_password) >= 7):
               # Password is valid
               self.games_to_play()
       else:
           # Invalid password
           self.email_and_password.config(text="Password must contain at least 7 characters, and at least one capital letter, number, and special character")

   def games_to_play(self):
       # Hide input widgets and show game selection buttons
       self.enter_button.grid_remove()
       self.enter_password.grid_remove()
       self.email_and_password.config(text="Which game would you like to play?")
       self.computer_color_game_button.grid()  # Show Computer Color Game button
       self.rock_paper_scissors_button.grid()  # Show Rock Paper Scissors button
       self.GuessingGameButton.grid()  # Show Guessing Game button

   def run_game(self, script_name):
       # Hide the main window
       self.root.withdraw()  # Hides the window

       # Run the external game script
       subprocess.run(["python", script_name])

       # Show the main window again
       self.root.deiconify()  # Shows the window

   def computer_color_game(self):
       self.run_game("ComputerGameUsingGUI.py")

   def rock_paper_scissors(self):
       self.run_game("RockPaperScissorsUsingGUI.py")

   def guessing_game(self):
       self.run_game("GuessingGameUsingGUI.py")

if __name__ == "__main__":
   root = tk.Tk()  # Create the main Tkinter window
   app = Landco(root)  # Instantiate the Landco class
   root.mainloop()  # Start the Tkinter event loop
