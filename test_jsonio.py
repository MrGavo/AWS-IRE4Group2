'''
This is just a test file to test the functions in jsonio.py

I have already written some sample data to the json files
but if you want to try yourself then delete the existing json files and uncomment
the write lines below.

'''


import os
import time
from select import select
from jsonio import read_books, read_cakes, read_drinks, write_books, write_cakes, write_drinks
from Product import Cake, Drink, Book

os.system('cls' if os.name == 'nt' else 'clear')

# Sample Cake Data
cake1 = {
    "Apple Pie": {
        "name": "Apple Pie",
        "price": 12.99,
        "description": "Delicious apple pie with a flaky crust",
        "stock": 4
    }
}
cake2 = {
    "Chocolate Cake": {
        "name": "Chocolate Cake",
        "price": 15.49,
        "description": "Rich chocolate cake with creamy frosting",
        "stock": 5
    }
}
cake3 = {
    "Cinnamon Roll": {
        "name": "Cinnamon Roll",
        "price": 3.99,
        "description": "Warm cinnamon roll with icing",
        "stock": 11
    }
}
cake4 = {
    "Lemon Slice": {
        "name": "Lemon Slice",
        "price": 4.99,
        "description": "Tangy lemon slice with a sweet glaze",
        "stock": 7
    }
}
cake5 = {
    "Raspberry Muffin": {
        "name": "Raspberry Muffin",
        "price": 2.99,
        "description": "Moist muffin filled with fresh raspberries",
        "stock": 12
    }
}

# Sample Drink Data
drink1 = {
    "Latte": {
        "name": "Latte",
        "price": 12.99,
        "description": "Creamy latte with steamed milk",
        "stock": 7
    }
}
drink2 = {
    "Cappuccino": {
        "name": "Cappuccino",
        "price": 14.99,
        "description": "Espresso with frothy milk",
        "stock": 4
    }
}
drink3 = {
    "Americano": {
        "name": "Americano",
        "price": 11.99,
        "description": "Espresso with hot water",
        "stock": 12
    }
}
drink4 = {
    "Espresso": {
        "name": "Espresso",
        "price": 12.99,
        "description": "Strong and bold espresso shot",
        "stock": 22
    }
}
drink5 = {
    "Breakfast Tea": {
        "name": "Breakfast Tea",
        "price": 12.99,
        "description": "Classic black tea blend",
        "stock": 6
    }
}

# Sample Book Data
book1 = {
    "Python For Dummies": {
        "name": "Python For Dummies",
        "price": 19.99,
        "description": "A beginner's guide to Python programming",
        "stock": 12,
        "genre": "Programming",
        "author": "John Doe"
    }
}
book2 = {
    "Matter": {
        "name": "Matter",
        "price": 29.99,
        "description": "A science fiction novel exploring the nature of reality",
        "stock": 4,
        "genre": "Science Fiction",
        "author": "Iain M. Banks"
    }
}
book3 = {
    "The Life and Cuisine of Elvis Presley": {
        "name": "The Life and Cuisine of Elvis Presley",
        "price": 99.99,
        "description": "A biography and cookbook about the King of Rock and Roll... Mmmmmm Cheese Burger",
        "stock": 99,
        "genre": "Cookbook",
        "author": "Elvis Presley"
    }
}
book4 = {
    "Book": {
        "name": "Book",
        "price": 59.99,
        "description": "A fascinating biography of a remarkable individual.",
        "stock": 7,
        "genre": "Biography",
        "author": "Whoppi Goldberg"
    }
}
book5 = {
    "Twilight": {
        "name": "Twilight",
        "price": 39.99,
        "description": "A captivating novel about love and vampires.",
        "stock": 76,
        "genre": "Fantasy",
        "author": "Stephenie Meyer"
    }
}

# Write sample data to JSON files
# If you want to use this then first delete existing json files and uncomment these lines
# If you change any of the indiviual values - eg the price of Apple Pie then write will update the json
def reset_json():
    write_cakes(cake1)
    write_cakes(cake2)
    write_cakes(cake3)
    write_cakes(cake4)
    write_cakes(cake5)
    write_drinks(drink1)
    write_drinks(drink2)
    write_drinks(drink3)
    write_drinks(drink4)
    write_drinks(drink5)
    write_books(book1)
    write_books(book2)
    write_books(book3)
    write_books(book4)
    write_books(book5)

# reset_json()

# Read and print data from JSON files
# print("\nCAKES")
# print(read_cakes())
# print(type(read_cakes()))
# print("\nDRINKS")
# print(read_drinks())
# print(type(read_drinks()))
# print("\nBOOKS")
# print(read_books())
# print(type(read_books()))

cakes = read_cakes()
drinks = read_drinks()
books = read_books()


# --------------------------------------------------------------------------
# Below is Menu System for adding products to basket
# --------------------------------------------------------------------------
# def menu_select(product):
#     selection = -1
#     product_keys = list(product.keys())
#     num_products = len(product_keys)

#     while selection != 0:
#         os.system('cls' if os.name == 'nt' else 'clear')
        
#         # Iterating through the list of products - enumerate just puts a number beside each product
#         for i, k in enumerate(product, start=1):
#             print(f"{i}. {k.ljust(40)} {product[k]['description']}")
#         print('0. To Proceed')
        
#         try:
#             selection = int(input("Select item to add to your basket: "))

#             #if 1 <= selection <= num_products:
#             if selection >= 1 and selection <= num_products:
#                 item_to_add = product_keys[selection - 1]
#                 print(f"Adding {item_to_add} to your basket")
#                 order.append(item_to_add) #MrGavo : This is just how i was adding to an order list - you can change
#                 # MrGavo : Another option is to create an instance of the class
#                 # MrGavo : You would need to pass another arg for instance type eg. Cake, Drink, Book
#                 # item = Cake(**cakes[item_to_add])
#             elif selection == 0:
#                 print("Proceeding to checkout...")
#             else:
#                 print("Invalid selection. Please try again.")
#         except ValueError:
#             print("Invalid input. Please enter a number.")

#         time.sleep(2)


# menu_select(cakes)
# menu_select(drinks)
# menu_select(books)

# --------------------------------------------------------------------------
# Testing dict updates
# --------------------------------------------------------------------------
# print(cakes.values())
# print(cakes['Apple Pie'])
# print(cakes['Apple Pie']['price'])
# print (order)

# Read cakes.json into a dictionary of dictionaries
# Update price of Apple Pie
# Write back to json
# cakes = read_cakes()
# cakes['Apple Pie']['price'] = 33.44
# write_cakes(cakes)





# --------------------------------------------------------------------------
# Below is Menu System for adding new Products
# --------------------------------------------------------------------------
# name = ""
# price = 0
# desc = ""
# stock = 0
# genre = ""
# author = ""

# def add_new_prod(item):
#     while True:
#         os.system('cls' if os.name == 'nt' else 'clear')
#         print(f"Adding New {item}\n")
#         try:
#             name = input("Name".ljust(20) + ": ")
#             price = float(input("Price".ljust(20) + ": "))
#             desc = input("Description".ljust(20) + ": ")
#             stock = int(input("Stock".ljust(20) + ": "))
#             break
#         except ValueError:
#             print("Invalid input. Please enter a number.")
#             time.sleep(1)
#     return name.title(), price, desc.title(), stock

# def add_new_cake():
#     name, price, desc, stock = add_new_prod("Cake")
#     new_cake = {
#         name: {
#             "name": name,
#             "price": price,
#             "description": desc,
#             "stock": stock
#         }
#     }
#     print("Cake Added")
#     time.sleep(1)
#     write_cakes(new_cake)


# def add_new_drink():
#     name, price, desc, stock = add_new_prod("Drink")
#     new_drink = {
#         name: {
#             "name": name,
#             "price": price,
#             "description": desc,
#             "stock": stock
#         }
#     }
#     print("Drink Added")
#     time.sleep(1)
#     write_drinks(new_drink)


# def add_new_book():
#     name, price, desc, stock = add_new_prod("Book")
#     genre = input("Genre".ljust(20) + ": ").title()
#     author = input("Author".ljust(20) + ": ").title()
#     new_book = {
#         name: {
#             "name": name,
#             "price": price,
#             "description": desc,
#             "stock": stock,
#             "genre": genre,
#             "author": author
#         }
#     }
#     print("Book Added")
#     time.sleep(1)
#     write_books(new_book)


# add_new_cake()
# add_new_drink()
# add_new_book()



