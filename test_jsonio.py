'''
This is just a test file to test the functions in jsonio.py

I have already written some sample data to the json files
but if you want to try yourself then delete the existing json files and uncomment
the write lines below.

'''


import os
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
# write_cakes(cake1)
# write_cakes(cake2)
# write_cakes(cake3)
# write_cakes(cake4)
# write_cakes(cake5)
# write_drinks(drink1)
# write_drinks(drink2)
# write_drinks(drink3)
# write_drinks(drink4)
# write_drinks(drink5)
# write_books(book1)
# write_books(book2)
# write_books(book3)
# write_books(book4)
# write_books(book5)

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


# Access individual Dicts
# cakes = read_cakes()
# print(cakes.keys())
# for k in cakes:
#     print(k)
# print(cakes.values())
# print(cakes['Apple Pie'])
# print(cakes['Apple Pie']['price'])


# Read cakes.json into a dictionary of dictionaries
# Update price of Apple Pie
# Write back to json
# cakes = read_cakes()
# cakes['Apple Pie']['price'] = 33.44
# write_cakes(cakes)




