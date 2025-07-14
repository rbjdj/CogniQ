class User:
    def __init__(self, email, password, user_type):
        self.email = email
        self.password = password
        self.user_type = user_type
    
    def __str__(self):
        return f"User(email='{self.email}', type='{self.user_type}')"


class AuthSystem:
    def __init__(self):
        self.users = []
    
    def determine_user_type(self, email):
        if email.endswith('@admin.ph'):
            return 'admin'
        elif email.endswith('@gmail.com'):
            return 'user'
        else:
            raise ValueError("Invalid email domain. Only @admin.ph or @gmail.com allowed")
    
    def signup(self, email, password):
        try:
            if any(user.email == email for user in self.users):
                raise ValueError("Email already registered")
            
            user_type = self.determine_user_type(email)
            
            new_user = User(email, password, user_type)
            self.users.append(new_user)
            
            print(f"Successfully registered {user_type}: {email}")
            return new_user
            
        except ValueError as e:
            print(f"Signup failed: {e}")
            return None
    
    def login(self, email, password):

        user = next((u for u in self.users if u.email == email), None)
        
        if user and user.password == password:
            print(f"Login successful as {user.user_type}: {email}")
            return user
        else:
            print("Login failed: Invalid email or password")
            return None

if __name__ == "__main__":
    auth = AuthSystem()
    
    print("==== Mental Health Tracker Authentication ====")
    print("1. Signup")
    print("2. Login")
    print("3. Exit")
    
    while True:
        choice = input("\nEnter choice (1-3): ").strip()
        
        if choice == "1":
            email = input("Enter email: ").strip()
            password = input("Enter password: ").strip()
            auth.signup(email, password)
        
        elif choice == "2":
            email = input("Enter email: ").strip()
            password = input("Enter password: ").strip()
            user = auth.login(email, password)
            if user:
                if user.user_type == 'admin':
                    print("Redirecting to admin dashboard...")
                else:
                    print("Redirecting to user dashboard...")
        
        elif choice == "3":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter 1, 2 or 3.")
