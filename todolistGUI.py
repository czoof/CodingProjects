
import tkinter as tk

class toDoList:
    def __init__(self, root):
        
        self.root = root
        self.root.title("Landco 'To-Do-List'") 
        self.tasks = []
        self.finishedTasks = []
        #root.bind('<Return>', self.onEnterKey)
        #root.bind('<Escape>', self.onEscapeKey)
        
        self.entry = tk.Entry(root)
        self.entry.grid(row=1, column=1, pady=20, padx=20)
        self.entry.grid_remove()
        
        self.welcomeButton = tk.Label(root, text="Welcome to your personal To-Do-List at Landco. select an option below")
        self.welcomeButton.grid(row=0, column=1, pady=20, padx=20)
        
        self.enterButton = tk.Button(root, text="Enter", command=None)
        self.enterButton.grid(row=2, column=1, pady=20, padx=20)
        self.enterButton.grid_remove()
        
        self.back = tk.Button(root, text="Back", command=self.backButtonLogic)
        self.back.grid(row=3, column=1, pady=20, padx=20)
        self.back.grid_remove()

        self.addTaskButton = tk.Button(root, text="AddTask", command=self.addTask)
        self.addTaskButton.grid(row=1, column=1, pady=20, padx=20)
        
        self.yesButton = tk.Button(root, text="Yes", command=None)
        self.yesButton.grid(row=2, column=1, pady=20, padx=20)
        self.yesButton.grid_remove()
        
        self.removeTaskButton = tk.Button(root, text="RemoveTask", command=self.removeTask)
        self.removeTaskButton.grid(row=2, column=1, pady=20, padx=20)
        
        self.viewTaskButton = tk.Button(root, text="ViewTasks/Change/MarkCompleted", command=self.viewTasks)
        self.viewTaskButton.grid(row=3, column=1, pady=20, padx=20)
        
        self.changeTaskButton = tk.Button(root, text="ChangeTask", command=self.changeTasks)
        self.changeTaskButton.grid(row=2, column=1, pady=20, padx=20)
        self.changeTaskButton.grid_remove()
        
        self.markCompletedButton = tk.Button(root, text="MarkTaskComplete", command=self.markTaskComplete)
        self.markCompletedButton.grid(row=3, column=1, pady=20, padx=20)
        self.markCompletedButton.grid_remove()
        
        self.viewCompletedTask = tk.Button(root, text="CompletedTask", command=self.completedTasks)
        self.viewCompletedTask.grid(row=4, column=1, pady=20, padx=20)

        
    def buttonRemover(self):
        self.addTaskButton.grid_remove()
        self.removeTaskButton.grid_remove()
        self.viewTaskButton.grid_remove()
        self.viewCompletedTask.grid_remove()
        self.changeTaskButton.grid_remove()
        self.markCompletedButton.grid_remove()
        self.enterButton.grid_remove()
        
    def backButtonLogic(self):
        self.changeTaskButton.grid_remove()
        self.markCompletedButton.grid_remove()
        self.addTaskButton.grid()
        self.removeTaskButton.grid()
        self.viewTaskButton.grid()
        self.viewCompletedTask.grid()
        self.welcomeButton.config(text="Welcome to your personal To-Do-List at Landco, select an option below")
        self.entry.grid_remove()        
        
    def addTask(self):
        self.enterButton.config(command=self.addTask)
        self.addTaskButton.grid_remove()
        self.removeTaskButton.grid_remove()
        self.viewTaskButton.grid_remove()
        self.viewCompletedTask.grid_remove()
        self.welcomeButton.config(text="Type a task that you want to add")
        self.yesButton.grid_remove()
        self.entry.grid()
        self.back.grid() 
        self.enterButton.grid()
        self.text = self.entry.get()
        self.currentTasks = self.text
        if self.text:
            self.tasks.append(self.text)
            self.entry.delete(0, tk.END)
            self.welcomeButton.config(text=f"Added task: ({self.text}). Add another task? Or press back to go back")
            self.enterButton.grid_remove()
            self.entry.grid_remove()
            self.yesButton.config(command=self.addAnotherTask)
            self.yesButton.grid()
            
    def addAnotherTask(self):
        if self.yesButton:
            self.entry.grid()
            self.enterButton.grid()
            self.yesButton.grid_remove()
            self.welcomeButton.config(text="Add another task")
            
    
    def removeTask(self):
        self.enterButton.config(command=self.removeTask)
        self.enterButton.grid_remove()
        self.back.grid()
        self.buttonRemover()
        if self.tasks == []:
            self.welcomeButton.config(text="No current tasks")
            self.entry.grid_remove()
        else:
            self.yesButton.grid_remove()
            self.enterButton.grid()
            self.welcomeButton.config(text=f"Type the task you want to delete: {self.tasks}")        
            self.entry.grid()
            remove = self.entry.get()
            for task in self.tasks:
                if remove == task:
                    self.tasks.remove(task)
                    self.entry.delete(0, tk.END)
                    if self.tasks == []:
                        self.welcomeButton.config(text=f"Task ({task}) has been deleted. No current tasks left")
                        self.enterButton.grid_remove()
                        self.entry.grid_remove()
                    else:
                        self.welcomeButton.config(text=f"Task ({task}) has been removed. Remove another task? Or go back?")
                        self.entry.grid_remove()
                        self.yesButton.grid()
                        self.yesButton.config(command=self.removeAnotherTask)
                        self.enterButton.grid_remove()
                        
    def removeAnotherTask(self):
        self.removeTask()
        
            
    def viewTasks(self):
        self.yesButton.grid_remove()
        self.buttonRemover()
        self.enterButton.grid_remove()
        self.back.grid()
        if self.tasks == []:
            self.welcomeButton.config(text="No current tasks")
        else:
            self.welcomeButton.config(text=f"Here are your current tasks: {self.tasks}")
            self.changeTaskButton.grid()
            self.markCompletedButton.grid()
            self.back.grid(row=4, column=1, pady=20, padx=20)
            self.back.grid()
            
    def changeTasks(self):
        self.enterButton.config(command=self.changeTasks)
        self.buttonRemover()
        self.welcomeButton.config(text=f"Enter the task that you want to change {self.tasks}")
        self.entry.grid()
        self.enterButton.grid()
        self.change = self.entry.get()
        for task in self.tasks:
            if self.change == task:
                self.tasks.remove(task)
                self.entry.delete(0, tk.END)
                self.welcomeButton.config(text="Type the new task:")
                self.enterButton.config(command=self.newTaskToEnter)
                self.newTaskToEnter()
            
    def newTaskToEnter(self):
        self.newTask = self.entry.get()
        if self.newTask:
            self.entry.delete(0, tk.END)
            self.tasks.append(self.newTask)
            self.entry.grid_remove()
            self.enterButton.grid_remove()
            self.welcomeButton.config(text=f"Task has been changed to ({self.newTask}) Do you want to change another task?")
            self.yesButton.grid()
            self.yesButton.config(command=self.changeAnotherTask)
            
            
    def changeAnotherTask(self):
        self.yesButton.grid_remove()
        self.changeTasks()
        

    def markTaskComplete(self):
        self.buttonRemover()
        self.enterButton.grid()
        self.enterButton.config(command=self.markTaskComplete)
        self.entry.grid()
        self.markTask = self.entry.get()
        for task in self.tasks:
            if self.markTask == task:
                self.finishedTasks.append(task)
                self.entry.delete(0, tk.END)
                self.tasks.remove(task)
                self.welcomeButton.config(text=f"Task: ({task}) has been completed. Complete another task?")
                if self.tasks == []:
                    self.welcomeButton.config(text=f"Task ({task}) has been completed. No tasks available")
                    self.buttonRemover()
                    self.entry.grid_remove()
                    self.back.grid()
                else:
                    self.enterButton.grid_remove()
                    self.entry.grid_remove()
                    self.yesButton.grid()
                    self.yesButton.config(command=self.markAnotherTaskCompleted)
            else:
                self.welcomeButton.config(text=f"Please type a proper task: ({self.tasks})")
            
    def markAnotherTaskCompleted(self):
        self.markTaskComplete()
        
        
        
    def completedTasks(self):
        self.buttonRemover()
        self.back.grid()
        self.welcomeButton.config(text=f"Completed Tasks: {self.finishedTasks}")
    
                 
if __name__ == "__main__":
    root = tk.Tk()
    calc = toDoList(root)
    root.mainloop() 
        
            
    
        











