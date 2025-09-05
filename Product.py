'''
Product Parent Class
Has child classes for Cake Drink Book
'''

class Product:
    def __init__(self, name, price, stock=0):
        self.name = name.title()
        self.price = price
        self.stock = stock

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_stock(self):
        return self.stock

    def set_stock(self, new_stock):
        self.stock = new_stock
    
    def set_price(self, new_price):
        self.price = new_price
    
class Cake(Product):
    def __init__(self, name, price, stock=0):
        super().__init__(name, price, stock)


class Drink(Product):
    def __init__(self, name, price, stock=0):
        super().__init__(name, price, stock)
        self.size = size = 'S'

    def get_size(self):
        return self.size
    
    def set_size(self, new_size):
        self.size = new_size

class Book(Product):
    def __init__(self, name, price, genre, author, stock=0):
        super().__init__(name, price, stock)
        self.genre = genre
        self.author = author

    def get_genre(self):
        return self.genre

    def get_author(self):
        return self.author
    
    def set_genre(self, new_genre):
        self.genre = new_genre.title()

    def set_author(self, new_author):
        self.author = new_author.title()
