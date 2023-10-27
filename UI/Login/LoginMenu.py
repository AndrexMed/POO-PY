from Services.UserService import UserService
from Services.ProductService import ProductService
from Model.Product import Product

productSvc = ProductService()
userSvc = UserService()

class LoginMenu:
        def loginMenu(self, userName):
            print(f"\n<== Welcome {userName} ==>\n")
            while True:
                print("1. Register product")
                print("2. Delete product")
                print("3. List of products")
                print("4. Exit")

                try:
                    option = int(input("Select a option: "))

                    if option == 1:
                        self.registerProduct()
                    elif option == 2:
                        print("option 2")
                    elif option == 3:
                        self.listOfProducts()
                    elif option == 4:
                        print("\n<== Good bye ==>\n")
                        break
                    else:
                        print("\n<== Option no valid ==>\n")
                    
                except ValueError:
                        print("\n<== Enter a valid number ==>\n")

        def registerProduct(self):
            print("\n<== Register a product ==>\n")
            idProduct = input("Enter a id product: ")
            title = input("Enter name of product: ")
            price = float(input("Enter price of product: "))

            product = Product()
            product.idProduct = idProduct
            product.title = title
            product.price = price

            productSvc.registerProduct(product)

        def listOfProducts(self):
             productSvc.listProducts()

        def listOfUsers(self):
             userSvc.listUsers()





        
