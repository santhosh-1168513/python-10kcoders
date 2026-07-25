from bank import bank
from customer import customer
from account import account
from transaction import Transaction
from mini_statement import Statement

bank = bank(
    101,
    "union bank",
    "siva",
    "ubin0001234",
    "anantapur",
    1234567890,
)

customer = customer(
    1,
    "santhosh",
    22,
    "male",
    "anantapur",
    "9581927787",
    "santhosh@gmail.com"
)

account = account(
    1001,
    "santhosh",
    "savings",
    10000,
    "ananta",
    "ubi0001434"
)

transaction = Transaction()
statement = Statement()


while True:
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Mini Statement")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amount = float(input("Enter the amount to deposit: "))
        transaction.deposit(amount, account)
        statement.add_transaction(f"Deposited: {amount}")
    elif choice == "2":
        amount = float(input("Enter the amount to withdraw: "))
        transaction.withdraw(amount, account)
        statement.add_transaction(f"Withdrawn: {amount}")
    elif choice == "3":
        statement.display_statement()
    elif choice == "4":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
