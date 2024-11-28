# Program Description:
# This program creates a basic calculator GUI using the Tkinter library. The calculator
# supports addition, subtraction, multiplication, and division. It allows users to input 
# numbers and operations interactively and displays the result on a screen. Additional 
# features include clearing the display, toggling between positive and negative numbers, 
# and adding decimal points.

import tkinter as tk  # Importing the Tkinter library for GUI development

# Defining the calculator class to make this an OOP implementation
class calculatorGui:
    
    def __init__(self, root):
        # Initialize the GUI interface and set the title to "Calculator"
        self.root = root
        self.root.title("Calculator")
        
        # Label to display a welcome message
        self.welcomeLabel = tk.Label(self.root, text="Add/Subtract/Multiply/Divide?")
        self.welcomeLabel.grid(row=0, column=0, columnspan=3, pady=10, padx=10)
        
        # Entry widget for input (initially visible)
        self.enterEquation = tk.Entry(self.root)
        self.enterEquation.grid(row=1, column=0, columnspan=3, pady=10, padx=10)

        # Button layout with padding configuration
        button_padding = {'padx': 10, 'pady': 10}
        
        # Creating number buttons (1-9) and arranging them in a grid
        for i in range(1, 10):
            button = tk.Button(self.root, text=str(i), command=lambda num=i: self.number_click(num))
            row = (i - 1) // 3 + 2  # Determine row for the button
            col = (i - 1) % 3       # Determine column for the button
            button.grid(row=row, column=col, **button_padding)

        # Button for the number 0
        button_zero = tk.Button(self.root, text="0", command=lambda: self.number_click(0))
        button_zero.grid(row=5, column=1, **button_padding)

        # Operation buttons
        self.addButton = tk.Button(self.root, text="+", command=self.add)
        self.addButton.grid(row=2, column=3, **button_padding)

        self.subtractButton = tk.Button(self.root, text="-", command=self.subtract)
        self.subtractButton.grid(row=3, column=3, **button_padding)

        self.multiplyButton = tk.Button(self.root, text="X", command=self.multiply)
        self.multiplyButton.grid(row=4, column=3, **button_padding)

        self.divideButton = tk.Button(self.root, text="/", command=self.divide)
        self.divideButton.grid(row=5, column=3, **button_padding)
        
        # Equals button to calculate the result
        self.equalsButton = tk.Button(self.root, text="=", command=self.equal)
        self.equalsButton.grid(row=5, column=3, **button_padding)
        
        # Clear button to reset the input
        self.clearButton = tk.Button(self.root, text="Clear", command=self.clear)
        self.clearButton.grid(row=6, column=1, **button_padding)
        
        # Decimal button for decimal inputs
        self.decimalButton = tk.Button(self.root, text=".", command=self.add_decimal)
        self.decimalButton.grid(row=5, column=0, **button_padding)

        # Button to toggle between positive and negative numbers
        self.negativeButton = tk.Button(self.root, text="+/-", command=self.toggle_negative)
        self.negativeButton.grid(row=6, column=0, **button_padding)
        
    # Method to handle number button clicks
    def number_click(self, num):
        current = self.enterEquation.get()  # Get the current input
        self.enterEquation.delete(0, tk.END)  # Clear the input field
        self.enterEquation.insert(0, current + str(num))  # Append the clicked number to the input field
    
    # Method to add a decimal point to the input
    def add_decimal(self):
        current = self.enterEquation.get()
        if "." not in current:  # Add a decimal point only if not already present
            self.enterEquation.insert(tk.END, ".")
    
    # Method to toggle the sign of the input
    def toggle_negative(self):
        current = self.enterEquation.get()
        if current and current[0] == "-":  # If negative, make it positive
            self.enterEquation.delete(0)
        else:  # If positive, make it negative
            self.enterEquation.insert(0, "-")

    # Method to handle addition
    def add(self):
        self.first_number = float(self.enterEquation.get())  # Store the first number
        self.operation = "+"  # Set the operation
        self.enterEquation.delete(0, tk.END)  # Clear the input field
    
    # Method to handle subtraction
    def subtract(self):
        self.first_number = float(self.enterEquation.get())
        self.operation = "-"
        self.enterEquation.delete(0, tk.END)
    
    # Method to handle multiplication
    def multiply(self):
        self.first_number = float(self.enterEquation.get())
        self.operation = "X"
        self.enterEquation.delete(0, tk.END)
    
    # Method to handle division
    def divide(self):
        self.first_number = float(self.enterEquation.get())
        self.operation = "/"
        self.enterEquation.delete(0, tk.END)
    
    # Method to calculate the result when the equals button is pressed
    def equal(self):
        self.second_number = float(self.enterEquation.get())  # Store the second number
        self.enterEquation.delete(0, tk.END)  # Clear the input field
        if self.operation == "+":  # Perform addition
            result = self.first_number + self.second_number
            self.enterEquation.insert(0, str(result))
        elif self.operation == "-":  # Perform subtraction
            result = self.first_number - self.second_number
            self.enterEquation.insert(0, str(result))
        elif self.operation == "X":  # Perform multiplication
            result = self.first_number * self.second_number
            self.enterEquation.insert(0, str(result))
        elif self.operation == "/":  # Perform division
            result = self.first_number / self.second_number
            self.enterEquation.insert(0, str(result))
    
    # Method to clear the input field
    def clear(self):
        self.enterEquation.delete(0, tk.END)

# Main code to run the GUI
if __name__ == "__main__":
    root = tk.Tk()  # Create the main application window
    calc = calculatorGui(root)  # Initialize the calculator GUI
    root.mainloop()  # Run the Tkinter event loop
