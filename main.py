from itertools import chain
from blockchain import Blockchain
from car_sharing import Owner, Car, Customer, Car_Info
from extras import start2


def show_balance(cust_balance, owner_balance):
    #A function to show balance of customer and owner
    print("Customer balance: %s" % (cust_balance,))
    print("Owner balance: %s" % (owner_balance,))

def show_rental_cost(cost):
    print("Rental cost: ", cost)

def start():
    print("  ")
    print("######## Creating a new blockchain ##########")
    print("  ")
    blockchain = Blockchain()
    
    customer = Customer(500)
    owner = Owner(500)

    eth = 50

    #show balance of customer and owner
    show_balance(customer.balance, owner.balance)

    #1
    #Deploy owner on the blockchain
    owner.deploy(eth, blockchain)

    #2
    customer.request_book(eth, blockchain)

    #3
    car = "Honda Civic"
    year = 2005
    owner_name = "Oshanik"
    reg_no = "DL3CCK1791"
    daily_price = 10
    days_no = 3

    car_info1 = Car_Info(1,car, year, owner_name, reg_no, daily_price)

    #method to add car for rent
    owner.add_car_to_rent(car_info1)
    customer.pass_number_of_days(days_no)

    #4
    owner.encrypt_and_store_details(blockchain)
    owner.allow_car_usage()

    #5
    customer.access_car()

    #6
    customer.end_car_rental()

    #7
    owner.withdraw_earnings()
    customer.retrieve_balance()

    show_rental_cost(daily_price*days_no)
    show_balance(customer.balance, owner.balance)
    
    for i in blockchain.chain:
        print(i.transactions)



if __name__ == '__main__':
    start2()
