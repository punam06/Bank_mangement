class Banking:
    def __init__(self, user_name, initial_balance):
        self.name = user_name
        self.balance = initial_balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
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
print(f"Initial Balance is: {ostad.balance}")
print(f"Deposit Balance is: {ostad.deposit(1000)}")  # Display updated balance after deposit
print(f"After deposit, Your Balance is: {ostad.get_balance()}")
print(f"Initial balance is: {ostad.balance}")