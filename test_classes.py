'''
Test oject create and method call
'''

# Imports
import os
from Product import Cake, Drink, Book
from jsonio import read_cakes

# Clear the console
os.system('cls' if os.name == 'nt' else 'clear')

# Testing Cake Object creation
# --------------------------------------------------------------------------------------
print('\nCreate Cake Object and get data')
print('-'*30)
cake1 = Cake("Chocolate Cake", 20.43)

print(cake1.get_name())
print(cake1.get_price())
print(cake1.get_description())
print(cake1.get_stock())

print('\nModify Cake Object and get data')
print('-'*30)
cake1.set_price(199.99)
cake1.set_description('Im a Big Cake')
cake1.set_stock(999)



print(cake1.get_name())
print(cake1.get_price())
print(cake1.get_description())
print(cake1.get_stock())

# Testing Drink Object creation
# --------------------------------------------------------------------------------------
print('\nCreate Drink Object and get data')
print('-'*30)
drink1 = Drink("Latte", 3.59)

print(drink1.get_name())
print(drink1.get_price())
print(drink1.get_description())
print(drink1.get_stock())
print(drink1.get_size())

# Testing Book Object creation
# --------------------------------------------------------------------------------------
print('\nCreate Book Object and get data')
print('-'*30)
book1 = Book("Python For Dummies", 19.99, 'A beginner\'s guide to Python programming', 12, "Programming", "John Doe")

print(book1.get_name())
print(book1.get_price())
print(book1.get_description())
print(book1.get_stock())
print(book1.get_genre())
print(book1.get_author())



# Testing different ways to create objects from the dicts nested in a dict
# --------------------------------------------------------------------------------------
print('\nCreate dict from inside dict')
cakes = read_cakes()
ap = cakes['Apple Pie']
print(ap)
print('-' * 30)

print('\nCreate Cake Object from dict')
print('-' * 30)
applepie1 = Cake(ap['name'], ap['price'], ap['description'], ap['stock'])
print(applepie1.get_name())
print(applepie1.get_price())
print(applepie1.get_description())
print(applepie1.get_stock())

print('\nCreate Cake object from dict using ** unpack')
print('-' * 30)
applepie2 = Cake(**ap)
print(applepie2.get_name())
print(applepie2.get_price())
print(applepie2.get_description())
print(applepie2.get_stock())


print('\nCreate Cake Object from dict directly using ** unpack')
print('-' * 30)
choco1 = Cake(**cakes['Chocolate Cake'])
print(choco1.get_name())
print(choco1.get_price())
print(choco1.get_description())
print(choco1.get_stock())