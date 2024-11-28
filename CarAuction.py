# Description:
# This program simulates an auction where three contestants (Joe, Mike, and Nick) bid on cars.
# Each car has a starting price, and the bidding continues for a set time until a winner is determined for each car.
# The highest bid wins the car, and the auction continues until all cars are sold.
# The contestants' bids are simulated randomly, and the auction timer runs for 5 seconds for each round of bidding.

import time
import random
import sys

# Car class: Defines the attributes of a car and includes a string representation for displaying the car details.
class Cars:
    def __init__(self, year, make, model, startingPrice, highestBid, numberOfBids, bidDecrease, winner):
        self.year = year
        self.make = make
        self.model = model
        self.startingPrice = startingPrice
        self.highestBid = highestBid
        self.numberOfBids = numberOfBids
        self.bidDecrease = bidDecrease
        self.winner = winner
        
    def __str__(self):
        return f"{self.year} {self.make} {self.model} starting at ${self.startingPrice}"

# Define cars
car1 = Cars(2010, "Toyota", "Camry", 10000, 0, 0, .05, "")
car2 = Cars(2015, "BMW", "M4", 20000, 0, 0, .05, "")
car3 = Cars(2020, "Mercedes", "GT", 30000, 0, 0, .05, "")
cars = [car1, car2, car3]

# Contestants class: Defines the contestants with their name, current bid, number of cars won, and which cars they won.
class Contestants:
    def __init__(self, name, bid, carsWon, whichCarWon):
        self.name = name
        self.bid = bid
        self.numberOfCarsWon = carsWon
        self.whichCarWon = whichCarWon
    
    def __str__(self):
        return f"{self.name}:"

# Contestant instances
Joe = Contestants("Joe", 0, 0, "")
Mike = Contestants("Mike", 0, 0, "")
Nick = Contestants("Nick", 0, 0, "")

# Timer function: Displays a countdown for the auction
def timer(seconds):
    while True:
        print(f"{seconds} Seconds Remaining")
        if seconds == 0:
            break
        else:
            seconds -= 1
            time.sleep(1)

# Bid logic function: Handles the bidding logic, including random bids from each contestant
def bidLogic(price, bid, startIndex, car):
    if price == False:
        Joe.bid = random.randrange(car.startingPrice, car.startingPrice + priceLogic(cappedPrice=True, car=car))
        Mike.bid = random.randrange(car.startingPrice, car.startingPrice + priceLogic(cappedPrice=True, car=car))
        Nick.bid = random.randrange(car.startingPrice, car.startingPrice + priceLogic(cappedPrice=True, car=car))
    else:
        chance = random.randrange(10, 100)
        if chance > startIndex:
            return bid
        else:
            winner(car)

# Price logic function: Calculates the price based on bid decrease and random price fluctuation
def priceLogic(cappedPrice, car):
    price2 = True
    if True:
        car.bidDecrease -= random.uniform(.001, .003)
        calculation = car.bidDecrease * 50000
        price = int(calculation)
        cappedPrice = car.highestBid + price
        if cappedPrice <= car.highestBid:
            print(car.winner)
            winner(car)
        return cappedPrice

# Winner function: Determines the winner of the auction for each car
def winner(car):
    if Joe.bid == car.highestBid:
        car.winner = f"Joe won the {car} for ${Joe.bid}"
        Joe.numberOfCarsWon += 1
        Joe.whichCarWon += f"{car.winner}: "
        print(f"Joe won the auction of the {car} for ${Joe.bid}.")
        cars.remove(car)
        if cars == []:
            print(f"\nAuction over! Results of the auction: \n{Joe.whichCarWon} \n{Mike.whichCarWon} \n{Nick.whichCarWon}")
            sys.exit()
        time.sleep(2)
        auction()
        
    if Mike.bid == car.highestBid:
        car.winner = f"Mike won the {car} for ${Mike.bid}"
        Mike.numberOfCarsWon += 1
        Mike.whichCarWon += f"{car.winner}: "
        print(f"Mike won the auction of the {car} for ${Mike.bid}.")
        cars.remove(car)
        if cars == []:
            print(f"\nAuction over! Results of the auction: \n{Joe.whichCarWon} \n{Mike.whichCarWon} \n{Nick.whichCarWon}")
            sys.exit()
        time.sleep(2)
        auction()

    if Nick.bid == car.highestBid:
        car.winner = f"Nick won the {car} for ${Nick.bid}"
        Nick.numberOfCarsWon += 1
        Nick.whichCarWon += f"{car.winner}: "
        print(f"Nick won the auction of the {car} for ${Nick.bid}.")
        cars.remove(car)
        if cars == []:
            print(f"\nAuction over! Results of the auction: \n{Joe.whichCarWon} \n{Mike.whichCarWon} \n{Nick.whichCarWon}")
            sys.exit()
        time.sleep(2)
        auction()

# Auction logic for each car: Simulates the auction process with multiple bids and a timer countdown
def carAuction(car):  # when the timer stops, start the first bid, then set the timer again
    bidLogic(price=False, startIndex=0, bid=random.randrange(car.highestBid, car.highestBid + 2000), car=car)
    
    while True:  # main loop for the auction to keep going

        if Joe.bid > Mike.bid and Joe.bid > Nick.bid:
            car.highestBid = Joe.bid
            car.numberOfBids += 1
            print(f"\nJoe has the highest bid of: ${car.highestBid}")
            timer(seconds=5)
            Mike.bid = bidLogic(price=True, startIndex=int(10) + car.numberOfBids, bid=random.randrange(car.highestBid, priceLogic(cappedPrice=True, car=car)), car=car)
            Nick.bid = bidLogic(price=True, startIndex=int(10) + car.numberOfBids, bid=random.randrange(car.highestBid, priceLogic(cappedPrice=True, car=car)), car=car)

        elif Mike.bid > Joe.bid and Mike.bid > Nick.bid:
            car.highestBid = Mike.bid
            car.numberOfBids += 1
            print(f"\nMike has the highest bid of: ${car.highestBid}")
            timer(seconds=5)
            Joe.bid = bidLogic(price=True, startIndex=int(10) + car.numberOfBids, bid=random.randrange(car.highestBid, priceLogic(cappedPrice=True, car=car)), car=car)
            Nick.bid = bidLogic(price=True, startIndex=int(10) + car.numberOfBids, bid=random.randrange(car.highestBid, priceLogic(cappedPrice=True, car=car)), car=car)

        elif Nick.bid > Joe.bid and Nick.bid > Mike.bid:
            car.highestBid = Nick.bid
            car.numberOfBids += 1
            print(f"\nNick has the highest bid of ${car.highestBid}")
            timer(seconds=5)
            Mike.bid = bidLogic(price=True, startIndex=int(10) + car.numberOfBids, bid=random.randrange(car.highestBid, priceLogic(cappedPrice=True, car=car)), car=car)
            Joe.bid = bidLogic(price=True, startIndex=int(10) + car.numberOfBids, bid=random.randrange(car.highestBid, priceLogic(cappedPrice=True, car=car)), car=car)

# Main auction loop: Starts the auction process for all cars
def auction():
    for car in cars:
        if cars != []:
            print(f"\nNow we will start the auction for {car} in 5 seconds...")
            time.sleep(5)
            carAuction(car)     

# Welcome message and starting the auction
print(f"\nWeclome to the auction. Today we have three participants {Joe} {Mike} {Nick}")
input("\nPress 'enter' to start...")
auction()
