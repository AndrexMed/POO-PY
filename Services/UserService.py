from Model.User import User

class UserService:
    def __init__(self) -> None:
        self.users = []

    def registerUser(self, user):
        if isinstance(user, User):
          self.users.append(user)
          print("\n<== Usuario registrado con éxito. ==>\n")
        else:
          print("Error: Se esperaba un objeto de tipo User.")

    def listUsers(self):
        if not self.users:
            print("No hay usuarios registrados.")
        else:
            print("\n<== Lista de Usuarios ==>\n")
            for user in self.users:
                print(f"Nombre completo: {user.fullname}")
                print(f"Nombre de usuario: {user.username}")
                print(f"Contraseña: {user.password}")
                print("-" * 20)

    def isUserValid(self, userName, password):
        for user in self.users:
            if user.username == userName and user.password == password:
                return True
            return False