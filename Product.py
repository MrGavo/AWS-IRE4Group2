'''
Product Parent Class
Has child classes for Cake Drink Book
'''

class Product:
    def __init__(self, name, price, description='', stock=0):
        self.name = name.title()
        self.price = price
        self.description = description
        self.stock = stock

    def get_name(self):
        return self.name

    def get_price(self):
        return self.price

    def get_description(self):
        return self.description

    def get_stock(self):
        return self.stock

    def set_stock(self, new_stock):
        self.stock = new_stock
    
    def set_description(self, new_description):
        self.description = new_description  

    def set_price(self, new_price):
        self.price = new_price
    
class Cake(Product):
    def __init__(self, name, price, description='', stock=0):
        super().__init__(name, price, description, stock)


class Drink(Product):
    def __init__(self, name, price, description='', stock=0):
        super().__init__(name, price, description, stock)
        self.size = size = 'S'

    def get_size(self):
        return self.size
    
    def set_size(self, new_size):
        self.size = new_size

class Book(Product):
    def __init__(self, name, price, description='', stock=0, genre='', author=''):
        super().__init__(name, price, description, stock)
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
