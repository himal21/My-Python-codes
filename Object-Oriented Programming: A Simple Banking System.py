class Account:
    def __init__(self, account_number, account_holder, balance=0):
        self.account_number = account_number
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: ${amount}. New balance: ${self.balance}.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: ${amount}. New balance: ${self.balance}.")
        else:
            print("Invalid withdrawal amount.")

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"Account({self.account_number}, {self.account_holder}, Balance: ${self.balance})"


# Example usage
if __name__ == "__main__":
    account1 = Account("123456", "Alice", 1000)
    print(account1)
    account1.deposit(500)
    account1.withdraw(200)
    print(account1)
