class Customer():
    def __init__(self,name, order):
        self.name = name
        self.order = order
        self.cart = []

    def add_cart(self,item):
        self.cart.append(item)
    
    def rv_cart(self, item):
        self.cart.remove(item)
    
    def show_cart(self):
        print(self.cart)

newcust = Customer("gerardo", 1)

newcust.add_cart("cakes")
newcust.show_cart()
