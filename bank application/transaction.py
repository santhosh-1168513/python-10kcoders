class Transaction:

    def deposit(self, amount, account):
        if amount > 0:
            account.balance += amount
            print(f"Amount Deposited : ₹{amount}")
            print(f"Total Balance : ₹{account.balance}")
        else:
            print("Invalid Amount")

    def withdraw(self, amount, account):
        if amount > 0 and amount <= account.balance:
            account.balance -= amount
            print(f"Amount Withdrawn : ₹{amount}")
            print(f"Total Balance : ₹{account.balance}")
        else:
            print("Invalid Amount or Insufficient Balance")