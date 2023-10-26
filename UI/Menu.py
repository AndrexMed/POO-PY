from Model.User import User
from Services.UserService import UserService
from UI.Login.LoginMenu import LoginMenu

userService = UserService()

class Menu:
    def __init__(self):
        self.options = [
            {
                "number": 1,
                "text": "Login"
            },
            {
                "number": 2,
                "text": "Register"
            },
            {
                "number": 3,
                "text": "Exit"
            }
        ]

    def showMenu(self):
        while True:
            print("\n<== Menu ==>\n")
            for option in self.options:
                print(f"{option['number']}. {option['text']}")

            try:
                    
              choice = int(input("Select an option: "))

              if choice == 1:
                self.login()
              elif choice == 2:
                self.register()
              elif choice == 3:
                print("\n<== Good bye ==>\n")
                break
              else:
                print("\n<== Option no valid! ==>\n")

            except ValueError:
                 print("\n <== Enter a valid number (1 - 3) ==>\n")

    def login(self):
       userName = input("Enter your userName: ")
       password = input("Enter your password: ")

       isUserValid = userService.isUserValid(userName, password)

       if isUserValid:
          loginMenu = LoginMenu()
          loginMenu.loginMenu(userName)
       else:
          print("\n<== Credentials are no valid ==>\n")
    
    def register(self):
       fullName = input("Enter your full name: ")
       userName = input("Enter your userName: ")
       password = input("Enter your password: ")

       user = User()
       user.fullname = fullName
       user.username = userName
       user.password = password

       userService.registerUser(user)


