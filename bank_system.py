class Banking:
    def __init__(self, user_name, initial_balance):
        self.name = user_name
        self.initial_balance = initial_balance  # Store initial balance separately
        self.balance = initial_balance  # Start with initial balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount  # Add deposit to balance
        return self.balance  # Return updated balance after deposit
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return amount  
        else:
            return "Insufficient Balance"
    
    def get_balance(self):
        return self.balance  # Method to get current balance

# Create an instance of Banking
ostad = Banking("Ostad", 10000)
print(f"Account Name: {ostad.name}")
print(f"Initial Balance is: {ostad.initial_balance}")  # Display the stored initial balance

# Deposit 1000 and store the updated balance
updated_balance = ostad.deposit(1000)

print(f"Deposit Amount: {1000}")  # Display the deposit amount
print(f"Deposit Balance is: {updated_balance}")  # Display updated balance after deposit
print(f"After deposit, Your Balance is: {ostad.get_balance()}")
print(f"Initial balance is: {ostad.initial_balance}")  # Display the stored initial balance again