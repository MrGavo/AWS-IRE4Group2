import os
import jsonio
from Product import Cake, Drink, Book
import customer as Customer


def employee(name):
    #display menu for employees
    print(f"Welcome {name}")

def customer_interface(name):
    #display menu for cakes
    print(f"Welcome {name}")
    # global order



def main():
    while True:
        #asks if it is the employee or the customer that will log in
        os.system("cls")
        person = input("Employee or Customer (E/C): ").lower()
        #if the person is Employee, call the definition of employee
        if person == "e":
            os.system("cls")
            emp = input("Please log in with your name: ")
            employee(emp)
            #print("employee")
        #If the person is customer, call definition of customer
        elif person == "c":
            os.system("cls")
            print("Welcome to The Coffee Stain")
            name = input("Please enter your name: ").title()
            customer_interface(name)
            
            #print ("customer")
        else:
            print("Invalid input, try again.")



main()