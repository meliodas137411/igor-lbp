class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password


users = {
    "admin": User("admin", "admin123"),
    "usuario1": User("usuario1", "senha123"),
}
