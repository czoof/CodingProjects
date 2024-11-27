import tkinter as tk

# Identifying the calculator class to make this an OOP
class calculatorGui:
    
    def __init__(self, root):
        # Create GUI interface with self.root = root, set the title to calculator
        self.root = root
        self.root.title("Calculator")
        
        # Welcome label
        self.welcomeLabel = tk.Label(self.root, text="Add/Subtract/Multiply/Divide?")
        self.welcomeLabel.grid(row=0, column=0, columnspan=3, pady=10, padx=10)
        
        # Entry widget for input (initially visible)
        self.enterEquation = tk.Entry(self.root)
        self.enterEquation.grid(row=1, column=0, columnspan=3, pady=10, padx=10)

        # Button layout
        button_padding = {'padx': 10, 'pady': 10}
        
        # Number buttons (arranged in a grid)
        for i in range(1, 10):
            button = tk.Button(self.root, text=str(i), command=lambda num=i: self.number_click(num))
            row = (i - 1) // 3 + 2
            col = (i - 1) % 3
            button.grid(row=row, column=col, **button_padding)

        # Zero button
        button_zero = tk.Button(self.root, text="0", command=lambda: self.number_click(0))
        button_zero.grid(row=5, column=1, **button_padding)

        # Operation buttons
        self.addButton = tk.Button(self.root, text="+", command=self.add)
        self.addButton.grid(row=2, column=3, **button_padding)

        #subtract buttton
        self.subtractButton = tk.Button(self.root, text="-", command=self.subtract)
        self.subtractButton.grid(row=3, column=3, **button_padding)

        #multiply button
        self.multiplyButton = tk.Button(self.root, text="X", command=self.multiply)
        self.multiplyButton.grid(row=4, column=3, **button_padding)

        #divide button
        self.divideButton = tk.Button(self.root, text="/", command=self.divide)
        self.divideButton.grid(row=5, column=3, **button_padding)
        
        #equals button
        self.equalsButton = tk.Button(self.root, text="=", command=self.equal)
        self.equalsButton.grid(row=5, column=3, **button_padding)
        
        #clear equation
        self.clearButton = tk.Button(self.root, text="Clear", command=self.clear)
        self.clearButton.grid(row=6, column=1, **button_padding)
        
        #decimal button
        self.decimalButton = tk.Button(self.root, text=".", command=self.add_decimal)
        self.decimalButton.grid(row=5, column=0, **button_padding)

        #negative to positive and vice versa button
        self.negativeButton = tk.Button(self.root, text="+/-", command=self.toggle_negative)
        self.negativeButton.grid(row=6, column=0, **button_padding)
        
    # Define when the number is clicked 
    def number_click(self, num):
        current = self.enterEquation.get()
        self.enterEquation.delete(0, tk.END)  
        self.enterEquation.insert(0, current + str(num))  
    
    #decimal method
    def add_decimal(self):
        current = self.enterEquation.get()
        if "." not in current:
            self.enterEquation.insert(tk.END, ".")
    
    # negative method  
    def toggle_negative(self):
        current = self.enterEquation.get()
        if current and current[0] == "-":
            self.enterEquation.delete(0)
        else:
            self.enterEquation.insert(0, "-")

    #add method
    def add(self):
        self.first_number = float(self.enterEquation.get())  
        self.operation = "+"  
        self.enterEquation.delete(0, tk.END)
    
    #subtract method 
    def subtract(self):
        self.first_number = float(self.enterEquation.get())
        self.operation = "-"
        self.enterEquation.delete(0, tk.END)
    
    #multiply method
    def multiply(self):
        self.first_number = float(self.enterEquation.get())
        self.operation = "X"
        self.enterEquation.delete(0, tk.END)
    
    # divide method
    def divide(self):
        self.first_number = float(self.enterEquation.get())
        self.operation = "/"
        self.enterEquation.delete(0, tk.END)
    
    #equals method
    def equal(self):
        self.second_number = float(self.enterEquation.get()) 
        self.enterEquation.delete(0, tk.END)  
        if self.operation == "+":
            result = self.first_number + self.second_number
            self.enterEquation.insert(0, str(result))
            
        elif self.operation == "-":
            result = self.first_number - self.second_number
            self.enterEquation.insert(0, str(result))
            
        elif self.operation == "X":
            result = self.first_number * self.second_number
            self.enterEquation.insert(0, str(result))
            
        elif self.operation == "/":
            result = self.first_number / self.second_number
            self.enterEquation.insert(0, str(result))
    
    #clear button to clear the equations
    def clear(self):
        self.enterEquation.delete(0, tk.END)
    
# Main code to run the GUI
if __name__ == "__main__":
    root = tk.Tk()
    calc = calculatorGui(root)
    root.mainloop()
