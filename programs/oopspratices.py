
class Laptop:
    def __init__(self, brand, model, price, ram, storage):
        self.brand = brand
        self.model = model
        self.price = price
        self.ram = ram
        self.storage = storage

    def display_details(self):
        print("-----------------------------")
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Price: ${self.price}")
        print(f"RAM: {self.ram} GB")
        print(f"Storage: {self.storage} GB")
        print("-----------------------------")

    def upgrade_ram(self, additional_ram):
        self.ram += additional_ram
        print(f"RAM upgraded to {self.ram} GB")

    def apply_discount(self, discount_percentage):
        discount_amount = (discount_percentage / 100)
        self.price -= discount_amount * self.price
        print(f"Discount of {discount_percentage}% applied")
        print(f"New price: ${self.price : .2f}")

# Example usage(object creation)
hp = Laptop("hp vitus","intel core i5", 50000, 8, 512)
hp.display_details()

additional_ram = 8
hp.upgrade_ram(additional_ram)

discount_percentage = 10
hp.apply_discount(discount_percentage)
hp.display_details()

#-------------------------- Example2 --------------------------
class Employee:
    def __init__(self, e_id, ename, department, salary):
        self.e_id = e_id
        self.ename = ename
        self.department = department
        self.salary = salary

    def display_details(Self):
        print("-----------------------------")
        print(f"Employee ID: {Self.e_id}")
        print(f"Employee Name: {Self.ename}")
        print(f"Department: {Self.department}")
        print(f"Salary: ${Self.salary}")
        print("-----------------------------")

    def increase_salary(self, parcent):
        increase_amount = (parcent/ 100) * self.salary
        self.salary += increase_amount
        print(f"Salary increased by {parcent}%")
        print(f"New salary: ${self.salary : .2f}")

    def change_department(self, new_department):
        self.department = new_department
        print(f"Department changed to {self.department}")

# Example usage(object creation)
employee1 = Employee("9581we", "santhosh", "it", 240000)
employee2 = Employee("9582we", "sai", "hr", 200000)
employee3 = Employee("9583we", "kumar", "finance", 300000)

employee1.display_details()
employee2.display_details()
employee3.display_details()

employee1.increase_salary(15)

employee2.change_department("finance")

employee1.display_details()
employee2.display_details()
employee3.display_details()

# -------------------------- Example3 --------------------------
# encapsulation - private attributes and methods
class BankAccount:
    def __init__(self, account_number, account_holder, balance):
        self.__account_number = account_number
        self.__account_holder = account_holder
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"₹{amount} deposited successfully.")
            print(f"Current Balance: ₹{self.__balance}")
        else:
            print("Deposit amount must be greater than 0.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be greater than 0.")
        elif amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            print(f"₹{amount} withdrawn successfully.")
            print(f"Current Balance: ₹{self.__balance}")

    def display_account(self):
        print("\n----------------------------")
        print(f"Account Number : {self.__account_number}")
        print(f"Account Holder : {self.__account_holder}")
        print(f"Balance        : ₹{self.__balance}")
        print("----------------------------")


# Object Creation
account1 = BankAccount("9530902932", "Santhosh", 1000)
account2 = BankAccount("9530902933", "Sai", 2000)

# Transactions for Account 1
print("\nAccount 1 Transactions")
account1.deposit(500)
account1.withdraw(200)
account1.display_account()

# Transactions for Account 2
print("\nAccount 2 Transactions")
account2.deposit(1000)
account2.withdraw(4000)   # Insufficient balance
account2.display_account()

# Testing Invalid Transactions
print("\nTesting Invalid Transactions")
account1.deposit(-100)
account1.withdraw(-500)

# --------------------------- Example4 --------------------------

class Employee:
    def __init__(self, emp_id, ename, salary):
        self.__emp_id = emp_id
        self.__ename = ename
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, new_salary):
        if new_salary >= 0 and new_salary <= 2000000:
            self.__salary = new_salary
            print(f"Salary updated to {self.__salary}")
        else:
            print("Invalid salary. Salary must be between 0 and 2,000,000.")

    def display_details(self):
        print(f"Employee ID: {self.__emp_id}")
        print(f"Employee Name: {self.__ename}")
        print(f"Salary: {self.__salary}")

# Example usage
employee1 = Employee("E001", "Santhosh", 50000)
employee2 = Employee("E002", "Sai", 60000)
employee3 = Employee("E003", "Kumar", 70000)

employee1.salary= 55000  # Valid salary update
employee1.salary= 2500000  # Invalid salary update
employee1.salary= -1000  # Invalid salary update

employee1.display_details()
employee2.display_details()
employee3.display_details()

# @property: A property allows you to access a method like an attribute (variable). It is mainly used to control access to private variables while keeping the syntax simple.
# A getter is a method used to read a private variable.
# A setter is a method used to set or update the value of a private variable. It allows you to add validation or additional logic when modifying the variable's value.