from blockchain import Blockchain
from car_sharing import Owner, Car, Customer, Car_Info

starting_money = 50
running = True
balances = {"Oshanik" : 50}
cars = [{'car_id' : 1, 'Name' : "Honda City", 'Year' : 2015, "Owner" : "Oshanik", 'reg_no' : "DL3CCK1791", 'daily_price' : 10}]

def customerHome():
    print(" ")
    print(" ")
    print("###################################################")
    print("###################################################")
    print(" ")
    print(" ")
    
    #Function that makes up the customer homepage
    print("Hello customer")
    name = input("Please Enter your Name : ")
    print(" ")
    print("###################################################")
    print(" ")
    balance = 0

    #starting off every new user with 500 rupees
    if name in balances.keys():
        print("Welcome back " + str(name))
        balance = balances[name]
        
    else:
        balance = starting_money
        balances[name] = balance
        print("Hi " + name)
        print("You have been started off with"+str(balance)+" Rs credit in your account! ")

    print("Current balance is : " + str(balance))

    print(" ")
    print("###################################################")
    print(" ")
    print("The following cars are currently available to rent")
    showListOfCars()
    print(" ")
    print(" ")
    print("Please Enter the car_id of the car you want to rent")
    print("Or enter 000 to go back to the main menu")
    print("")

    sno = int(input(""))
    
    if sno == 000:
        start2()
    else:
        days = int(input("How many days do you want to rent the car for? : "))
        selectedCar = {}
        for car in cars:
            if car['car_id']==sno:
                selectedCar = car
        
        costOfRenting = int(selectedCar['daily_price']*days)

        #checking of the user has enough balace for the transaction
        if balance < costOfRenting:
            
            print("")
            print("Insufficient Balance")
            print("Cost of renting : " + str(costOfRenting) + " ")
            print("Balance : " + str(balance))
            print("")
            input("press any key to go back")
            customerHome()
        
        newBalance = balance - costOfRenting
        balances[name] = newBalance
        carOwnerName = selectedCar["Owner"]

        balances[carOwnerName] = balances[carOwnerName] + costOfRenting
        print("")
        print("Creating a request to rent the selected car ...")
        print(".")
        print(".")
        print(".")
        print(".")
        input("Car rental sucessful, press any key to go back to the main menu")


        

def showListOfCars():
    print(" ")
    for car in cars:
        print(car)



def ownerHome():
    print(" ")
    print(" ")
    print("###################################################")
    print("###################################################")
    print(" ")
    print(" ")
    #Function that makes up the owner homepage
    print("Hello Owner")
    ownerName = input("Please Enter your Name : ")
    print("###################################################")
    print(" ")  

    balance = 0

    if ownerName in balances.keys():
        print(" Welcome back " + str(ownerName))
        balance = balances[ownerName]
    else:
        print(" Hi " + str(ownerName))
        balance = starting_money
        balances[ownerName] = balance

    print(" You have " + str(balance) + " Rs. credit in your account! ")
    

    while True:
        printCarsOwned(ownerName)
        print("Enter 0 if you want to add a new car")
        print("Enter 1 if you want to go back to the main menu")
        print(" ")

        input2 = int(input(""))

        if input2 == 0:
            addNewCar(ownerName)
        else:
            start2()

#cars = [{'car_id' : 1, 'Name' : "Honda City", 'Year' : 2015, "Owner" : "Oshanik", 'reg_no' : "DL3CCK1791", 'daily_price' : "10"}]
    
def addNewCar(ownerName):
    print(" ")
    car = {}
    car['car_id'] = int(input("Please Enter car-id : "))
    car['Name'] = input("Please Enter Car Name : ")
    car['Year'] = input("Please Enter car manufacturing year : ")
    car["Owner"] = ownerName
    car['reg_no'] = input("Please Enter car's registration number : ")
    car['daily_price'] = int(input("Please Enter the per-day price of the car : "))

    cars.append(car)


def printCarsOwned(ownerName):
    print(" ")
    print("You own the following cars : ")
    print(" ")
    for car in cars:
        if car["Owner"] == ownerName:
            print(car)
    print(" ")

def start2():
    while running:
        #Printing main menu
        print(" ")
        print(" ")
        print("###################################################")
        print("### Welcome to Decentralised Car Rental Service ###")
        print("###################################################")
        print("  Made by Oshanik, Rishab and Jatin for 8th sem BTP")
        print(" ")
        print(" ")
        print("Are you a")
        print("(1) Car Owner")
        print("(2) Customer")

        custOrOwner = int(input("Enter a value from 1-2 "))

        if custOrOwner == 2:
            customerHome()
        else:
            ownerHome()
        


"""
Requirements - 
0. Ask if youre a car owner or a customer
1. Add car for rent
2. Show available cars
3. Select a car for renting, provide the number of days and rent the car
4. balance deduction
"""