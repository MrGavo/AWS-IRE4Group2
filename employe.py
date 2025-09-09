import jsonio
import pprint
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
            print("5. Logout")

            options = input("Enter your choice: ")

            if options == "1":
                self.add_product()
            elif options == "2":
                self.view_products()
            elif options == "3":
                self.remove_product()
            elif options == "4":
                self.check_stock()
            elif options == "5":
                print("Logging out...\n")
                break
            else:
                print("Invalid choice, try again.")
##Add a new product to cakes, drinks, or books.
    def add_product(self):
        product = input("Which category you want to add? (cakes/drinks/books): ").lower()
        name = input("Enter product name: ")
        price = float(input("Enter price: "))
        description = input("Please provide the description" )
        stock = int(input("Enter stock quantity: "))
        ## Created a dictionary to add new items 
        new_item = {
        name: {
            "name" : name,
            "description": description,
            "price": price,
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


    def view_products(self):
        print("\n--- Books ---")
        books = jsonio.read_books()
        # print json to screen with human-friendly formatting
        pprint.pprint(books, compact=True)
        print("\n--- Cakes ---")
        cakes = jsonio.read_cakes() 
        pprint.pprint(cakes, compact=True)
        print("\n--- Drinks ---")
        drinks = jsonio.read_drinks()  
        pprint.pprint(drinks, compact=True)


    def remove_product(self):
        product = input("Remove from which category? (cakes/drinks/books): ").lower()
        if product == "cakes":
            stock = jsonio.read_cakes()
        elif product == "drinks":
            stock = jsonio.read_drinks() 
        elif product == "books":
            stock = jsonio.read_books()
        else:
            print("Invalid category.")
            return

         


        
