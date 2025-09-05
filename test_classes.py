'''
Test oject create and method call
'''

# Imports
import os
from Product import Cake, Drink, Book

# Clear the console
os.system('cls' if os.name == 'nt' else 'clear')

# Sample Cake Data
print('\nCreate Cake Object and get data')
print('-'*30)
cake1 = Cake("Chocolate Cake", 20.43, 5)

print(cake1.get_name())
print(cake1.get_price())
print(cake1.get_stock())

print('\nModify Cake Object and get data')
print('-'*30)
cake1.set_stock(1999)
cake1.set_price(199.99)

print(cake1.get_name())
print(cake1.get_price())
print(cake1.get_stock())

# Sample Drink Data
print('\nCreate Drink Object and get data')
print('-'*30)
drink1 = Drink("Latte", 3.59, 10)

print(drink1.get_name())
print(drink1.get_price())
print(drink1.get_stock())
print(drink1.get_size())

# Sample Book Data
print('\nCraete Book Object and get data')
print('-'*30)
book1 = Book("The Great Gatsby", 10.99, "Fiction", "F. Scott Fitzgerald", 3)

print(book1.get_name())
print(book1.get_price())
print(book1.get_genre())
print(book1.get_author())
print(book1.get_stock())

