# Description: This program is the same as CarAuction.py but now has a GUI
# This program simulates an auction where three contestants (Joe, Mike, and Nick) bid on cars.
# Each car has a starting price, and the bidding continues for a set time until a winner is determined for each car.
# The highest bid wins the car, and the auction continues until all cars are sold.
# The contestants' bids are simulated randomly, and the auction timer runs for 5 seconds for each round of bidding.

import tkinter as tk
import random

# Class representing each car in the auction
class Cars:
    def __init__(self, year, make, model, startingPrice, highestBid, numberOfBids, bidDecrease, winner):
        # Initialize car attributes
        self.year = year
        self.make = make
        self.model = model
        self.startingPrice = startingPrice
        self.highestBid = highestBid
        self.numberOfBids = numberOfBids
        self.bidDecrease = bidDecrease
        self.winner = winner
        
    # String representation of a car
    def __str__(self):
        return f"{self.year} {self.make} {self.model} starting at ${self.startingPrice}"

# Define the cars available for auction
car1 = Cars(2010, "Toyota", "Camry", 10000, 0, 0, .05, "")
car2 = Cars(2015, "BMW", "M4", 20000, 0, 0, .05, "")
car3 = Cars(2020, "Mercedes", "GT", 30000, 0, 0, .05, "")

# Class representing the contestants in the auction
class Contestants:
    def __init__(self, name, bid, carsWon, whichCarWon):
        # Initialize contestant attributes
        self.name = name
        self.bid = bid
        self.numberOfCarsWon = carsWon
        self.whichCarWon = whichCarWon
    
    # String representation of a contestant
    def __str__(self):
        return f"{self.name}:"

# Contestants in the auction
Joe = Contestants("Joe", 0, 0, "")
Mike = Contestants("Mike", 0, 0, "")
Nick = Contestants("Nick", 0, 0, "")

# Main class for managing the auction logic
class Auction:
    def __init__(self, root):
        self.root = root
        self.root.title("Car Auction")  # Set the title of the window

        self.timerId = None  # To store the timer ID for managing delays
        self.car = None  # To store the currently selected car
        self.end = False  # Flag to indicate the end of an auction

        self.auctionStart = False  # To track if the auction has started
        self.bids = [Joe.bid, Mike.bid, Nick.bid]  # List of bids by the contestants

        # Create and place the main label
        self.label = tk.Label(text=f"\nWeclome to the auction. Today we have three participants. ({Joe} {Mike} {Nick}) \nClick on the car that you want to start with.")
        self.label.grid(row=0, column=0, padx=20, pady=20)

        # Create and place the timer label
        self.timerLabel = tk.Label(text="")
        self.timerLabel.grid(row=1, column=0, padx=20, pady=20)

        # Create and place the auction result label
        self.auctionLabel = tk.Label(text="")
        self.auctionLabel.grid(row=2, column=0, padx=20, pady=20)

        # Create and place buttons for the available cars
        self.ToyotaButton = tk.Button(text="2010 Toyota Camry")
        self.ToyotaButton.grid(row=1, column=0, padx=20, pady=20)
        self.ToyotaButton.config(command=self.ToyotaAuction)

        self.BMWButton = tk.Button(text="2015 BMW M4")
        self.BMWButton.grid(row=2, column=0, padx=20, pady=20)
        self.BMWButton.config(command=self.BMWAuction)

        self.MercedesButton = tk.Button(text="2020 Mercedes GT")
        self.MercedesButton.grid(row=3, column=0, padx=20, pady=20)
        self.MercedesButton.config(command=self.MercedesAuction)

        # Create the Back button to return to the car selection
        self.backButton = tk.Button(text="Back", command=self.back)
        self.backButton.grid(row=4, column=0, padx=20, pady=20)
        self.backButton.grid_forget()  # Hide it initially

        # Button to view the auction winners
        self.viewAuctionWinnersButton = tk.Button(text="Auction Winners", command=self.auctionWinners, state=tk.DISABLED)
        self.viewAuctionWinnersButton.grid(row=4, column=0, padx=20, pady=20)
        

    def back(self):  # Method to handle going back to car selection
        self.viewAuctionWinnersButton.grid()  # Show the "View Winners" button
        self.viewAuctionWinnersButton.config(state=tk.ACTIVE)  # Activate the button
        self.disableCars()  # Disable car buttons after auction
        self.label.grid()  # Show the main label again
        self.backButton.grid_remove()  # Hide the back button
        self.car.winner = ""  # Clear winner information
        # Reset the main label text
        self.label.config(text=f"\nWeclome to the auction. Today we have three participants. ({Joe} {Mike} {Nick}) \nClick on the car that you want to start with.")
        self.ToyotaButton.grid()  # Show the car buttons again
        self.BMWButton.grid()
        self.MercedesButton.grid()
        self.timerLabel.grid_remove()  # Hide the timer label
        self.auctionLabel.grid_remove()  # Hide the auction label

    def buttonRemover(self):  # Remove car selection buttons
        self.ToyotaButton.grid_remove()
        self.BMWButton.grid_remove()
        self.MercedesButton.grid_remove()

    def timer(self, seconds, callback):  # Method to handle countdown timer
        if seconds >= 0:
            self.timerLabel.config(text=f"{seconds} seconds remaining")  # Update the timer label
            self.timerId = self.root.after(1000, self.timer, seconds - 1, callback)  # Continue countdown
        else:
            callback()  # Trigger the callback when timer ends

    def priceLogic(self, cappedPrice):  # Calculate price changes during the auction
        self.car.bidDecrease -= random.uniform(.001, .003)  # Decrease the bid price by a random amount
        calculation = self.car.bidDecrease * 50000  # Calculate new price based on bid decrease
        price = int(calculation)
        cappedPrice = self.car.highestBid + price  # Ensure price does not exceed the highest bid
        if cappedPrice <= self.car.highestBid:  # If price drops too low, auction ends
            self.end = True
            self.winner()  # Call the winner method
        return cappedPrice

    def bidLogic(self, price, bid, startIndex):  # Logic to handle bidding process
        if price == False:  # If it's the first bid
            for i in range(len(self.bids)):
                self.bids[i] = random.randrange(self.car.startingPrice, self.car.startingPrice + self.priceLogic(cappedPrice=True))
            Joe.bid, Mike.bid, Nick.bid = self.bids  # Set the bids for the contestants
        else:
            chance = random.randrange(10, 100)
            if chance > startIndex:
                return bid  # Return bid if within range
            else:
                self.end = True
                self.winner()  # Call the winner method

    def updateAuction(self):  # Method to update auction results after each bid round
        if self.end == False:
            if Joe.bid > Mike.bid and Joe.bid > Nick.bid:
                self.car.highestBid = Joe.bid
                self.car.numberOfBids += 1
                self.auctionLabel.config(text=f"Joe had the highest bid of ${Joe.bid} \nTotal # of bids = {self.car.numberOfBids}")
                Mike.bid = self.bidLogic(price=True, startIndex=int(10) + self.car.numberOfBids, bid=random.randrange(self.car.highestBid, self.priceLogic(cappedPrice=True)))
                Nick.bid = self.bidLogic(price=True, startIndex=int(10) + self.car.numberOfBids, bid=random.randrange(self.car.highestBid, self.priceLogic(cappedPrice=True)))
            elif Mike.bid > Joe.bid and Mike.bid > Nick.bid:
                self.car.highestBid = Mike.bid
                self.car.numberOfBids += 1
                self.auctionLabel.config(text=f"Mike had the highest bid of ${Mike.bid} \nTotal # of bids = {self.car.numberOfBids}")
                Nick.bid = self.bidLogic(price=True, startIndex=int(10) + self.car.numberOfBids, bid=random.randrange(self.car.highestBid, self.priceLogic(cappedPrice=True)))
                Joe.bid = self.bidLogic(price=True, startIndex=int(10) + self.car.numberOfBids, bid=random.randrange(self.car.highestBid, self.priceLogic(cappedPrice=True)))
            elif Nick.bid > Joe.bid and Nick.bid > Mike.bid:
                self.car.highestBid = Nick.bid
                self.car.numberOfBids += 1
                self.auctionLabel.config(text=f"Nick had the highest bid of ${Nick.bid} \nTotal # of bids = {self.car.numberOfBids}")
                Joe.bid = self.bidLogic(price=True, startIndex=int(10) + self.car.numberOfBids, bid=random.randrange(self.car.highestBid, self.priceLogic(cappedPrice=True)))
                Mike.bid = self.bidLogic(price=True, startIndex=int(10) + self.car.numberOfBids, bid=random.randrange(self.car.highestBid, self.priceLogic(cappedPrice=True)))

            # Continue to the next round after 2 seconds
            self.timer(3, self.updateAuction)

    def startAuction(self):  # Method to start the auction
        self.auctionLabel.config(text="")  # Clear the winner message immediately
        self.end = False  # Reset the end flag
        Joe.bid = Mike.bid = Nick.bid = 0  # Reset contestant bids
        self.car.highestBid = 0  # Reset the highest bid for the car
        self.car.numberOfBids = 0  # Reset the number of bids
        self.timerLabel.config(text="")  # Clear previous timer messages
        self.bidLogic(price=False, startIndex=0, bid=random.randrange(self.car.startingPrice, self.car.startingPrice + 2000))  # Start fresh bid logic
        self.updateAuction()  # Start auction process

    def theAuction(self):  # Wrapper for starting auction
        self.startAuction()

    def winner(self):  # Handle declaring the winner
        self.label.grid_remove()

        if Joe.bid == self.car.highestBid:
            self.car.winner = f"Joe won the {self.car} for ${Joe.bid}"
            Joe.whichCarWon += f"{self.car.winner}\n"  # Add the win to Joe's record
            self.auctionLabel.config(text=self.car.winner)
        elif Mike.bid == self.car.highestBid:
            self.car.winner = f"Mike won the {self.car} for ${Mike.bid}"
            Mike.whichCarWon += f"{self.car.winner}\n"  # Add the win to Mike's record
            self.auctionLabel.config(text=self.car.winner)
        elif Nick.bid == self.car.highestBid:
            self.car.winner = f"Nick won the {self.car} for ${Nick.bid}"
            Nick.whichCarWon += f"{self.car.winner}\n"  # Add the win to Nick's record
            self.auctionLabel.config(text=self.car.winner)
        
        self.timerLabel.grid_remove()
        self.backButton.grid()  # Show back button after auction ends

    def disableCars(self):  # Disable car selection buttons after auction starts
        if self.car == car1:
            self.ToyotaButton.config(state=tk.DISABLED)
        if self.car == car2:
            self.BMWButton.config(state=tk.DISABLED)
        if self.car == car3:
            self.MercedesButton.config(state=tk.DISABLED)

    def auctionWinners(self):  # Display the auction winners
        self.viewAuctionWinnersButton.grid_remove()
        self.backButton.grid()
        self.buttonRemover()
        # Display winners for each contestant
        self.label.config(text=f"Current winner's \n{Joe.whichCarWon} \n{Mike.whichCarWon} \n{Nick.whichCarWon}")

    def ToyotaAuction(self):  # Start auction for Toyota
        self.car = car1
        self.viewAuctionWinnersButton.grid_remove()
        self.auctionLabel.grid()
        self.auctionLabel.config(text="")
        self.timerLabel.grid()
        self.buttonRemover()
        self.label.config(text=f"This is the auction for the {self.car}.")
        self.timer(5, self.theAuction)  # Start auction after 5 seconds

    def BMWAuction(self):  # Start auction for BMW
        self.car = car2
        self.viewAuctionWinnersButton.grid_remove()
        self.auctionLabel.grid()
        self.auctionLabel.config(text="")
        self.timerLabel.grid()
        self.buttonRemover()
        self.label.config(text=f"This is the auction for the {self.car}.")
        self.timer(5, self.theAuction)  # Start auction after 5 seconds

    def MercedesAuction(self):  # Start auction for Mercedes
        self.car = car3
        self.viewAuctionWinnersButton.grid_remove()
        self.auctionLabel.grid()
        self.auctionLabel.config(text="")
        self.timerLabel.grid()
        self.buttonRemover()
        self.label.config(text=f"This is the auction for the {self.car}.")
        self.timer(5, self.theAuction)  # Start auction after 5 seconds

# Initialize and run the Tkinter window
root = tk.Tk()
app = Auction(root)
root.mainloop()
