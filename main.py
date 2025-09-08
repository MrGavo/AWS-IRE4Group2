import os
from Product import Cake, Drink, Book


def employee(name):
    #display menu for employees
    print(f"welcome {name}")

def customer(name):
    #display menu for cakes
    print(f"welcome {name}")




def main():
    while True:
        #asks if it is the employee or the customer that will log in
        person = input("Employee or Customer (E/C): ").lower()
        #if the person is Employee, call the definition of employee
        if person == "e":
            print("employee")
        #If the person is customer, call definition of customer
        elif person == "c":
            print("Welcome to The Coffee Stain")
            name = input("Please enter your name: ")
            customer(name)
            
            #print ("customer")
        else:
            print("Invalid input, try again.")



main()
