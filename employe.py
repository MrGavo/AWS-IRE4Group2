import jsonio
# Created a class for employee 
class Employee:
    def __init__(self, name):
        self.name = name

    def menu(self):

        
        print(f"\nWelcome {self.name} back")
        while True:
            print("\n--- Employee Menu ---")
            print("1. Add Product")
            print("2. View Products")
            print("3. Remove Product")
            print("4. Check Stock")
            print("5. Add Discount")
            print("6. Logging Out")

            options = input("Enter your choice: ")

            if options   == "1":
                self.add_product()
            elif options == "2":
                self.view_product()
            elif options == "3":
                self.remove_product()
            elif options == "4":
                self.check_stock()
            elif options == "5" :
                self.add_discount()   
            elif options == "6":
                print("Logging out...\n")
                break
            else:
                print("Invalid choice, try again.")

##Add a new product to cakes, drinks, or books.

    def add_product(self):      
        product = input("Which category you want to add? (cakes/drinks/books): ").lower()
        if product == "books":
            name = input("Enter product name: ")
            price = float(input("Enter price: "))
            description = input("Please provide the description" )
            stock = int(input("Enter stock quantity: ")) 
            genre = input("Enter genre:")
            author = input("Enter the author of the book: ")
### Created a dictionary to add new items           
            new_item = {
               name: {
                "name" : name,
                "price": price,
                "description": description,
                "stock": stock,
                "genre": genre,
                "author":author
                }
            }
        else:
         name = input("Enter product name: ")
         price = float(input("Enter price: "))
         description = input("Please provide the description: ")
         stock = int(input("Enter stock quantity: "))

        # Dictionary for cakes/drinks
        new_item = {
         name: {
                "name": name,
                "price": price,
                "description": description,
                "stock": stock
              }
        }

        if product == "cakes":
            jsonio.write_cakes(new_item)
        elif product == "drinks":
            jsonio.write_drinks(new_item)
        elif product == "books":
            jsonio.write_books(new_item)
        else:
            print("Invalid category.")


    def view_product(self):
        print("\n--- Cakes ---")
        cakes = jsonio.read_cakes() 
        print(cakes)

        print("\n--- Drinks ---")  
        drinks = jsonio.read_drinks()
        print(drinks)  

        print("\n--- Books ---")
        books = jsonio.read_books()
        print(books)


        
 
    def remove_product(self):
        product = input("Remove from which category? (cakes/drinks/books): ").lower()
        stock = {}   
        if product == "cakes":
            cakes = jsonio.read_cakes()
            stock = list(cakes.keys())
            print(stock)
        elif product == "drinks":
            stock = jsonio.read_drinks() 
        elif product == "books":
            stock = jsonio.read_books()
        else:
            print("Invalid category.")
            return


        item_to_remove = input("Enter the name of the item you want to remove: ")
### Removing the item and wiriting back to the json 
        if item_to_remove in stock:
            del stock[item_to_remove] 
            if product == "cakes":
                jsonio.write_cakes(stock)
            elif product == "drinks":
                jsonio.write_drinks(stock)
            elif product == "books":
                jsonio.write_books(stock)

            print(f"{item_to_remove} has been removed from {product}.")
        else:
            print(f"{item_to_remove} not found in {product}.")

one=Employee ("name")    
one.remove_product()   
    
   ## def check_stock(self):


    ## def add_discount(self):   
        




        