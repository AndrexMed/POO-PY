from Services.UserService import UserService

class LoginMenu:
        def loginMenu(self, userName):
            print(f"\n<== Welcome {userName} ==>\n")
            while True:
                print("1. Register product")
                print("2. Delete product")
                print("3. List of users")
                print("4. Exit")

                try:
                    option = int(input("Select a option: "))

                    if option == 1:
                        print("option 1")
                    elif option == 2:
                        print("option 2")
                    elif option == 3:
                        userSvc = UserService()
                        userSvc.listUsers()
                    elif option == 4:
                        print("\n<== Good bye ==>\n")
                        break
                    else:
                        print("\n<== Option no valid ==>\n")
                    
                except ValueError:
                        print("\n<== Enter a valid number ==>\n")

        
