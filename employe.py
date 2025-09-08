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

    def add_product(self):

         


        