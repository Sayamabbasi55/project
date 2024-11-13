class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role  # Either 'Admin' or 'User'

class AuthSystem:
    def __init__(self):
        self.users = {
            "admin": User("admin", "admin123", "Admin"),
            "user": User("user", "user123", "User")
        }

    def login(self, username, password):
        user = self.users.get(username)
        if user and user.password == password:
            print(f"Welcome, {username}!")
            return user
        else:
            print("Invalid username or password.")
            return None
