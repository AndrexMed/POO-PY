from Model.User import User

class UserService:
    def __init__(self) -> None:
        self.users = []

    def registerUser(self, user):
        if isinstance(user, User):
          self.users.append(user)
          print("\n<== User registered successfully. ==>")
        else:
          print("Error: An object of type User was expected.")

    def listUsers(self):
        if not self.users:
            print("\n <== No users founded. ==>")
        else:
            print("\n<== List of Users ==>\n")
            for user in self.users:
                print(f"Id Persona: {user.idPerson}")
                print(f"Nacionalidad: {user.nationality}")
                print(f"Nombre completo: {user.fullname}")
                print(f"Nombre de usuario: {user.username}")
                print(f"Contraseña: {user.password}")
                print("-" * 20)

    def isUserValid(self, userName, password):
        for user in self.users:
            if user.username == userName and user.password == password:
                return True
            return False