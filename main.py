import os
import jsonio
import time
from Product import Cake, Drink, Book
import customer as Customer
import employe

cakes = jsonio.read_cakes()
drinks = jsonio.read_drinks()
books = jsonio.read_books()

order = [] # MrGavo : This is just how i was adding to an order list - you can change
price = []


def employee(name):
    #display menu for employees
    print(f"Welcome {name}")

def customer_interface(name):
    #display menu for cakes
    cust = ''
    
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print(f"Welcome {name} !\n")
        print("!! 3 or more items + our monthly discount code gets you big savings!!\n")
        print("Can we interest you in some...")
        print("(D)rinks")
        print("(C)akes")
        print("(B)ooks")
        print("Do you want to see the (A)llergens ?")
        print("Or are you ready to Check(O)ut ?\n")
        cust = input("Please make your selection : ").lower()
        if cust == "d":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Today's drink menu is")
            time.sleep(0.5)        
            menu_select(drinks)
            cust = ''
        elif cust == "c":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Today's cakes menu is")
            time.sleep(0.5)
            menu_select(cakes)
            cust = ''
        elif cust == "b":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("See what's in our book shelf")
            time.sleep(0.5) 
            menu_select(books)
            cust = ''
        elif cust== "o":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Your basket is: \n")
            length = len(order)
            #Checks if the basket is empty and sends the customer back to the main screen
            if length == 0:
                print("The basket is empty")
                time.sleep(2)
                continue
            #display the list of the basket and the total
            for i in range(0, length):
                print(f"{i+1}. "+ str(order[i]).ljust(20) + str(price[i]))
            print(f"Total:  {sum(price)}€\n")
            #Asks what to remove of the basket
            remove = input("Do you want to (A)dd, (R)emove more items or (C)ontinue?: ").lower()
            #goes back to the main screen
            if remove == "a":
                continue
            #goes to the remove screen
            elif remove == "r":
                menu_remove()
                continue
            elif remove == "c":
                #employee asked to add discount here
                total = {sum(price)}
                if len(order) >= 3:
                    print(f"\nLooks like you have {len(order)} items in your basket")
                    print("If you have a valid coupon you get a 50% discount")
                    code = input("Enter your code : ")
                    if code.lower() == "discount":
                        total = round((sum(price) / 2), 2)
                        print("\nCongratulations - You get half off !")
                    else:
                        print("Sorry - Not a valid code !")
                print(f"Please pay: {total}€")
                time.sleep(5)
                #Removes the items of the lists
                for i in range(0,length):
                    order.pop()
                    price.pop()
                break
                #print(order, price)
            else:
                print("invalid selection")
                time.sleep(1)
                continue
            
        elif cust == "a":
            Chocolate_cake_allergens = "gluten, eggs, milk, butter, cocoa powder"
            Apple_pie_allergens = "gluten, eggs, milk, butter"
            Cinnamon_roll_allergens = "gluten, eggs, milk, butter,cinnamon"
            Lemon_slice_allergens = "gluten, eggs, milk, butter"
            Raspberry_muffin_allergens = "gluten, eggs, milk, butter"
            Gooseberry_tart_allergens = "gluten, eggs, milk, butter"

            cakes = {
                "Chocolate Cake": Chocolate_cake_allergens,
                "Apple Pie": Apple_pie_allergens,
                "Cinnamon Roll": Cinnamon_roll_allergens,
                "Lemon Slice": Lemon_slice_allergens,
                "Raspberry Muffin": Raspberry_muffin_allergens,
                "Gooseberry Tart" : Gooseberry_tart_allergens
            }
            #selected_cake = input("which cake \n").title()
            for cake, allergens in cakes.items():
                if cake == selected_cake.title():
                    print(f"{cake} contains the following allergens: {allergens}")


            Latte_allergens = "milk"
            Cappuccino_allergens = "milk"
            Americano_allergens = "No allergens"
            Espresso_allergens = "No allergens"
            Breakfast_tea_allergens = "milk"

            drinks = {
                "Latte": Latte_allergens,
                "Cappuccino": Cappuccino_allergens,
                "Americano": Americano_allergens,
                "Espresso": Espresso_allergens,
                "Breakfast Tea": Breakfast_tea_allergens
            }
            #selected_drink = input("which drink \n").title()
            for drink, allergens in drinks.items():
                if drink == selected_drink.title():
                    print(f"{drink} contains the following allergens: {allergens}")

            time.sleep(3)


            continue
        else:
            print("Sorry not available today")
            continue
    # print(order) # MrGavo : just checking to see if all items are being addded
    time.sleep(1)

#Shows the list of the order that the customer placed with the price
def menu_remove():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        length = len(order)
        #display a list of the items in the cart and the total price
        for i in range(0, length):
            print(f"{i+1}. "+ str(order[i]).ljust(20) + str(price[i]))
        print(f"Total:  {sum(price)}€")
        print('0. To Proceed')

        try:
            select = int(input("Select the item you want to remove: "))
            
            if select >= 1 and select <= length:
                print(f"Removed {order[select-1]} -- {price[select-1]}")
                #Removes the selected item and the price of the list
                order.pop(select-1)
                price.pop(select-1)
                time.sleep(1)
            elif select == 0:
                print("Proceeding to checkout...")

                break
            else:
                print("Invalid selection. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")



# Menu length should be dynamic now based on the number of Products
def menu_select(product):
    selection = -1
    product_keys = list(product.keys())
    num_products = len(product_keys)
    

    while selection != 0:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("------- MENU -------\n")
        # Iterating through the list of products - enumerate just puts a number beside each product
        for i, k in enumerate(product, start=1):
            print(f"{i}. {k.ljust(20)}" +  str(product[k]['price']).ljust(20) + f"{product[k]['description']}")
        print('\n0. To Proceed\n')
        
        try:
            selection = int(input("Select item to add to your basket: "))

            if selection >= 1 and selection <= num_products:
                item_to_add = product_keys[selection - 1]
                #access the value of price in the dictionary
                price_to_add = product[item_to_add]["price"]
                # print(f"Adding {price_to_add}")
                print(f"Adding {item_to_add} to your basket")
                order.append(item_to_add) #MrGavo : This is just how i was adding to an order list - you can change
                price.append(price_to_add) #adds the price to the table

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
    os.system('cls' if os.name == 'nt' else 'clear')
    while True:
        #asks if it is the employee or the customer that will log in
        #os.system("cls")
        
        person = input("Employee or Customer (E/C): ").lower()
        #if the person is Employee, call the definition of employee
        if person == "e":
            os.system('cls' if os.name == 'nt' else 'clear')
            emp = input("Please log in with your name: ")
            employee(emp)
            new_emp = employe.Employee(emp) ## Added
            new_emp.menu()
            #print("employee")
        #If the person is customer, call definition of customer
        elif person == "c":
            os.system('cls' if os.name == 'nt' else 'clear')
            #clear the list

            print("WELCOME to The Coffee Stain\n")
            name = input("Please enter your name: ").title()
            # new_customer = Customer.Customer(name)
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
