# AWS-IRE4Group2
The Coffee Stain
================
    Program to model a Bookshop and Cafe

Modules
-
    \---AWS-IRE4Group2
        |   books.json              - Books Data
        |   cakes.json              - Cakes Data
        |   drinks.json             - Drinks Data
        |   jsonio.py               - Json IO Module
        |   main.py                 - Main Program
        |   customer.py             - Customer Actions
        |   memploye.py             - Employee Actions
        |   Product.py              - Product Classes
        |   README.md
        |   test_classes.py         - Test Module for Classes
        |   test_jsonio.py          - Test module for Json IO


Classes
-

    Product
    * name
    * price
    * stock

    Cake (Inherits from Product)


    Drink (Inherits from Product)
    * size

    Book (Inherits from Product)
    * genre
    * author

Json Storage
-
    3 json files to store product data
    cakes.json
    drinks.json
    books.json



Customer
-
    CUSTOMER SIDE
    Shop counter
         Menu food drink and cakes
            display menu
                ask to see alergens for x food
            add or remove extra stuff
            add to cart, ask if he wants anything else y/n
                enter code to add cart
            update stock
         Menu books
            display menu
            add to cart ask if he wants anything else y/n
                enter code to add cart
            update stock
    show cart in counter with full price
        Ask employee to add discount y/n
            How much

Employee
-
    Menu food
        stock level each food
        change price
        add or remove food
    Menu book
        stock level of books
        change price
        add or remove books
    see Order


