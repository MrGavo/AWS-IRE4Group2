import os
import jsonio
import time
from Product import Cake, Drink, Book
import customer as Customer

cakes = jsonio.read_cakes()
drinks = jsonio.read_drinks()
books = jsonio.read_books()

order = [] # MrGavo : This is just how i was adding to an order list - you can change

def employee(name):
    #display menu for employees
    print(f"Welcome {name}")

def customer_interface(name):
    #display menu for cakes
    cust = ''
    print(f"welcome {name}")
    while cust != "checkout":
        os.system('cls' if os.name == 'nt' else 'clear')
        cust = input("Are you interested in drinks, cakes or books? Or checkout to proceed\n")
        cust = cust.lower()
        if cust == "drinks":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Today's drink menu is")
            time.sleep(1)        
            menu_select(drinks)
            cust = ''
        elif cust == "cakes":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Today's cakes menu is")
            time.sleep(1)
            menu_select(cakes)
            cust = ''
        elif cust == "books":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("See what's in our book shelf")
            time.sleep(1) 
            menu_select(books)
            cust = ''
        else:
            print("sorry not available today")
            continue
    print(order) # MrGavo : just checking to see if all items are being addded
    time.sleep(1)

def menu_select(product):
    selection = 1
    while selection !=0:
        os.system('cls' if os.name == 'nt' else 'clear')
        # Iterating through the list of products - enumerate just puts a number beside each product
        for i, k in enumerate(product, start=1):
            print(i, k.ljust(40), product[k]['description'])
        print ('0 To Proceed')
        selection = int(input("Select Item to add to your Basket : "))
        if selection == 1:
            print("Adding ", list(product.keys())[0], " to your basket")
            order.append(list(product.keys())[0]) #MrGavo : This is just how i was adding to an order list - you can change
            # MrGavo : Another option is to create an instance of the class
            # MrGavo : You would need to pass another arg for instance type eg. Cake, Drink, Book
            # item = Cake(**cakes[list(product.keys())[0]])
        elif selection == 2:
            print("Adding ", list(product.keys())[1], " to your basket")
            order.append(list(product.keys())[1]) #MrGavo : This is just how i was adding to an order list - you can change
        elif selection == 3:
            print("Adding ", list(product.keys())[2], " to your basket")
            order.append(list(product.keys())[2]) #MrGavo : This is just how i was adding to an order list - you can change
        elif selection == 4:
            print("Adding ", list(product.keys())[3], " to your basket")
            order.append(list(product.keys())[3]) #MrGavo : This is just how i was adding to an order list - you can change
        elif selection == 5:
            print("Adding ", list(product.keys())[4], " to your basket")
            order.append(list(product.keys())[4]) #MrGavo : This is just how i was adding to an order list - you can change
        time.sleep(2)


def main():
    while True:
        #asks if it is the employee or the customer that will log in
        #os.system("cls")
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
            new_customer = Customer.Customer(name,1)
            # new_customer.add_cart("cake")
            # new_customer.add_cart("coffee")
            # new_customer.add_cart("coke")
            # new_customer.show_cart()
            # new_customer.rv_cart("coke")
            # new_customer.show_cart()
            customer_interface(name)
            
            #print ("customer")
        else:
            print("Invalid input, try again.")



main()