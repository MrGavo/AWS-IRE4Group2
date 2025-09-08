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
    
    while cust != "o":
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Welcome {name} !\n")
        print("Can we interest you in some...")
        print("(D)rinks")
        print("(C)akes")
        print("(B)ooks")
        print("Or are you ready to Check(O)ut ?")
        cust = input("Please make your selection : ")
        cust = cust.lower()
        if cust == "d":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Today's drink menu is")
            time.sleep(1)        
            menu_select(drinks)
            cust = ''
        elif cust == "c":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Today's cakes menu is")
            time.sleep(1)
            menu_select(cakes)
            cust = ''
        elif cust == "b":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("See what's in our book shelf")
            time.sleep(1) 
            menu_select(books)
            cust = ''
        # else:
        #     print("sorry not available today")
        #     continue
    # print(order) # MrGavo : just checking to see if all items are being addded
    time.sleep(1)

# Menu length should be dynamic now based on the number of Products
def menu_select(product):
    selection = -1
    product_keys = list(product.keys())
    num_products = len(product_keys)

    while selection != 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        
        # Iterating through the list of products - enumerate just puts a number beside each product
        for i, k in enumerate(product, start=1):
            print(f"{i}. {k.ljust(40)} {product[k]['description']}")
        print('0. To Proceed')
        
        try:
            selection = int(input("Select item to add to your basket: "))

            if selection >= 1 and selection <= num_products:
                item_to_add = product_keys[selection - 1]
                print(f"Adding {item_to_add} to your basket")
                order.append(item_to_add) #MrGavo : This is just how i was adding to an order list - you can change
                # MrGavo : Another option is to create an instance of the class
                # MrGavo : You would need to pass another arg for instance type eg. Cake, Drink, Book
                # item = Cake(**cakes[item_to_add])
            elif selection == 0:
                print("Proceeding to checkout...")
            else:
                print("Invalid selection. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

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