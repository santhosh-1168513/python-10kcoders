# # calculate
def cal(a, b):
    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)


cal(20,30)


def add(a, b):
    print(a+b)

def sub(a, b):
    print(a-b)
def mul(a, b):
    print(a*b)
def div(a, b):
    print(a/b)
def mod(a, b):
    print(a%b)

mul(20,3)

mul(int(input("enter the first number:")),int(input("enter the second number:")))

# # to calculator if pressed 1 for add, 2 for sub, 3 for mul, 4 for div, 5 for mod
a = int(input("enter the first number:"))
b = int(input("enter the second number:"))
user_op = int(input("enter the number"))
while user_op <= 8:
    if user_op == 1:
        def add(a, b):
            print(a+b)
        add(a, b)
    elif user_op == 2:
        def sub(a, b):
            print(a-b)
        sub(a, b)
    elif user_op == 3:
        def mul(a, b):
            print(a*b)
        mul(a, b)
    elif user_op == 4:
        def div(a, b):
            print(a/b)
        div(a, b)
    elif user_op == 5:
        def mod(a, b):
            print(a%b)
        mod(a, b)
    elif user_op == 6:
        def pow(a, b):
            print(a**b)
        pow(a, b)
    elif user_op == 7:
        def floor_div(a, b):
            print(a//b)
        floor_div(a, b)
    elif user_op > 8:
        print("invalid input")
    break


# ###########################################################
#positional arguments
def items(name, price):
    print(f"item_name is : {name}")
    print(f"item_price is : {price}")

items(price=2500,name="mouse")

# keyword arguments
def items(name, price, qty=1):
    print(f"item_name is : {name}")
    print(f"item_price is : {price}")
    print(f"item_qty is : {qty}")

items(price=2500,name="mouse",qty=3)

# arguments with variable length
def items(*productnames):
    print(productnames)

items("mouse","keyboard","monitor","cpu")

# keyword arguments with variable length 
def student(**student_details):
    print(student_details)

student(name="john",age=20,rollno=101)


def student(**student_details):
    # print(student_details)
    for key, value in student_details.items():
        print(f"{key} : {value}")

student(name="john",age=20,rollno=101)

# write a python program for user defined by varying given passing argument tto even or odd number
def even_odd(*numbers):
    for num in numbers:
        if num %2 == 0:
            print(f"{num} is even")
        else:
            print(f"{num} is odd")

even_odd(1,2,3,4,5,6,7,8,9,10)
print(type(even_odd(1,2,3,4,5,6,7,8,9,10)))

def verify(a):
    if a % 2 == 0:
        print(f"{a} is even")
    else:
        print(f"{a} is odd")
verify(a=int(input("enter the number:")))


def place_order(customername, productname, qyt=1, *benefits, **details):
    print(f"customer name is : {customername}")
    print(f"product name is : {productname}")
    print(f"product quantity is : {qyt}")

    print("\n----------------------additional benefits are----------------------- ")
    for benefit in benefits:
        print(benefit)

    print("\n----------------------customer details are-----------------------")
    for key, value in details.items():
        print(f"{key} : {value}")


place_order(
    "john", "mouse", 2, "free shipping", "discount",
    address="123 street", phone="1234567890"
)

# IMP CALL BY REFERENCE AND CALL BY VALUE


## call by sharing reference
def item(list):
    list.append("40")                                       
    print("inside function value: ", list)

i = ["10", "20", "30"]
item(i)
print("before function value: ", i)

def item(s):
    s =20
    print("inside function value: ", s)





### lambda function
total = lambda a,b : a+b
print(total(10,20))

total = lambda a:"even" if a%2==0 else "odd"
print(total(10))

# map is used to apply a function to all the items in an iterable (like a list) and return a new iterable with the results. It takes two arguments: a function and an iterable. The function is applied to each item in the iterable, and the result is returned as a map object, which can be converted to a list or other data structures.
numbers = [1, 2, 3, 4, 5]
res = list(map(lambda x:x*2, numbers)) 
print(res)

# filter is used to filter items from an iterable based on a condition defined by a function. It takes two arguments: a function and an iterable. The function should return True or False for each item in the iterable. Only the items for which the function returns True are included in the result, which is returned as a filter object that can be converted to a list or other data structures.
marks =[54,61,89,92,25,78,88,91]
filtered_marks = list(filter(lambda x:x>=35, marks))
print(filtered_marks)

#write program a user inputs as cities and filter the cities which city is bangalore, them show the city is bangalore and if not show the city is not bangalore
citys = list(input("enter the city names: ").split(","))
filtered_cities = list(filter(lambda x: x == "bangalore", citys))
if filtered_cities:
    print("The city is Bangalore")
else:
    print("The city is not Bangalore")
fltered_cities = list(filter(lambda x: x.lower() == "bangalore", citys))
if fltered_cities:
    print("The city is Bangalore")
else:
    print("The city is not Bangalore")

# example of sorting a list of tuples based on the second element (age) in ascending order
employees = [ 
    ("John", 28, "Engineer"), 
    ("Alice", 32, "Manager"), 
    ("Bob", 25, "Analyst"), 
    ("Eve", 30, "Designer")
]

sorted_employee = (sorted(employees, key=lambda x: x[1], reverse=True))  # Sort by age in descending order
print(sorted_employee)


# reduce is used to apply a function cumulatively to the items of an iterable, reducing the iterable to a single value. It takes two arguments: a function and an iterable. The function should take two arguments and return a single value. The reduce function applies the function cumulatively to the items of the iterable, from left to right, so as to reduce the iterable to a single value. The result is returned as a single value.
from functools import reduce

from concurrent.interpreters import create
from venv import create    
list = [1, 2, 3, 4, 5]
result = reduce(lambda x,y : x+y, list)
print(result)  # Output: 15 (1+2+3+4+5)


# nested function is a function defined inside another function. The inner function can access the variables and parameters of the outer function. Nested functions are often used for encapsulation, to create closures, or to organize code in a more readable way.
def outer():
    print("This is the outer function.")
    
    def inner():
        print("This is the inner function.")
    
    inner()  # Call the inner function


outer()

# example of nested function 

def result(a,b):
    def add():
        print(a+b)
    
    add()  # Call the inner function
result(10, 20) # Output: 30


# 
def result():
    count = 0

    def counter():
        nonlocal count  # Declare count as nonlocal to modify it
        count += 1
        print(f"Count: {count}")

    counter()  # Call the inner function
    counter()
    counter()


result()

def atm(amount, balance):
    balance = 1000  # Example balance
    def withdraw(amount):
        if amount > balance:
            nonlocal balance        
            balance -= amount
            print(f"customer bank name is : {bank_name}")
            print(f"Withdrawn: {amount}, New Balance: {balance}")
        else:
            print("Insufficient balance.")
        








def student(name, marks):
    def result():
        if marks >= 35:
            print(f"{name} has passed with marks: {marks}")
        else:
            print(f"{name} has failed with marks: {marks}")
    result()  # Call the inner function

student("Alice", 85)  # Output: Alice has passed with marks: 85
student("Bob", 30)    # Output: Bob has failed with marks: 30


def student():
    name = "santhosh"
    marks = 85
    def result():
        if marks >= 35:
            print(f"{name} has passed with marks: {marks}")
        else:
            print(f"{name} has failed with marks: {marks}")
    result()  # Call the inner function

student()  # Output: santhosh has passed with marks: 85




####################################
#recursion function is a function that calls itself in order to solve a problem. It typically has a base case to terminate the recursion and prevent infinite loops. Recursion is often used for problems that can be broken down into smaller, similar subproblems.
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(10))  # Output: 55 (the 10th Fibonacci number)

# 
# Write a program to create employee salary as an outer function you have to take two parameters sal and name inside of outer function 
#create two inner functions one is to calculate the total salary and another is to calculate the bonus and as bonus pass 10% and as expected output employee name, performance salary, bonus, total salary after and bonus
def employee_salary(name, salary):
    def calculate_bonus():
        bonus = salary * 0.10
        return bonus
    
    def calculate_total_salary():
        bonus = calculate_bonus()
        total = salary + bonus
        return total
    
    calculate_bonus()
    calculate_total_salary()

    print(f"employee name is :{name}")
    print(f"pervious salary is :{salary}")
    print(f"bonus is :{calculate_bonus()}")
    print(f"total salary after bonus is :{calculate_total_salary()}")

employee_salary("santhosh", 50000)
















    def calculate_total_salary():
        bonus = calculate_bonus()
        tax = salary * 0.15
        total_after_tax_and_bonus = salary - tax + bonus
        return total_after_tax_and_bonus, bonus
    
    bonus = calculate_bonus()
    total = calculate_total_salary()[0]
    print(f"Employee Name: {name}")
    print(f"Performance Salary: {salary}")
    print(f"Bonus (10%): {bonus}")
    print(f"Total Salary after tax and bonus: {total}")

employee_salary("John", 50000)


count=0
def add(c,b):
    global  count
    print(c+b)
    if c==10 and b==20:
        count+=1
    print(count)
add(10,20)


d = 100
def fun():
    global d # declare d as global to modify it inside the function
    d = d+100
    print(d) # Output: 200
print(d) # Output: 100
fun()
print(d) # Output: 200

a = 50
def fun():
    a = 100  # This creates a new local variable 'a' inside the function
    print(a)  # Output: 100 (local variable)
fun()


a = 50
def fun():
    global a
    a = 100
    print(a)  # Output: 100 (global variable)
print(a) 
fun()
print(a)  # Output: 100 (global variable modified by the function)

def fun(a):
    a = 5
x = 4
fun(x)
print(x)  # Output: 4 (x remains unchanged because integers are immutable and passed by value)

def fun(a):
    a.append(4)
x = [1, 2, 3]
fun(x)
print(x)  

def student():
    name = "santhosh"
    print(name)

student()  # Output: santhosh

college = "alt"
def display_college():
    global college
    college = "alts"
    print(college)
print(college)  
display_college()
print(college)  # Output: alts (global variable modified by the function)

def fun1():
    a = 10
    b = 5
    def fun2():
        print(a)
        print(b)
    fun2()  # Call the inner function
fun1()  # Output: 10, 5 (inner function can access outer function's variables)`

def outer_function():
    x = 5
    def inner_function():
        print(x)  # Accessing variable from outer function
        return inner_function()  # Call the inner function'
a = outer_function()  # Call the outer function
print(a)  # Output: 5 (the value of x from the outer function)`

def outer():
    print("This is the outer function.")
    def inner():
        print("This is the inner function.")
    inner()  # Call the inner function
outer()

def greeting():
    def message():
        print("Hello, welcome to the program!")
    message()  # Call the inner function
greeting()  # Output: Hello, welcome to the program!

def outer_function():
    name = "santhosh"
    def inner_function():
        print(f"Hello, {name}!")  # Accessing variable from outer function
    inner_function()  # Call the inner function 
outer_function()  # Output: Hello, santhosh!

def calculate():
    a = 10
    b = 20
    def add():
        return a + b  # Accessing variables from outer function
        print(add)
    add()
calculate()  # Output: 30 (the sum of a and b from the outer function)

def school():
    def techer():
        print("This is the teacher function.")
    def student():
        print("This is the student function.")
    techer()  # Call the teacher function
    student()  # Call the student function
school()  # Output: This is the teacher function. This is the student function.