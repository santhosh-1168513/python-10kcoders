# oop concept is a programming paradigm that uses objects and classes to organize code. 
# It allows for encapsulation, inheritance, and polymorphism, which can lead to more modular and reusable code.

# class is a blueprint for creating objects. It defines a set of attributes and methods that the created objects will have. 
# An object is an instance of a class, which means it is a specific realization of the class with its own unique data.
# methods are functions that are defined within a class and can be called on objects of that class.
# types of methods in python are instance methods, class methods, and static methods.

# instance methods are the most common type of method in python classes. 
# They are defined with the self parameter, which refers to the instance of the class that the method is being called on. Instance methods can access and modify the attributes of the instance, and they can also call other methods of the instance.
class student:
    def student_details(self, sid, sname, sage): # what is self? self is a reference to the current instance of the class. It is used to access variables that belong to the class.
        self.sid = sid
        self.sname = sname
        self.sage = sage
        print(f"student id is {self.sid}")
        print(f"student name is {self.sname}")
        print(f"student age is {self.sage}")
# s is a object of student class
s = student()
s.student_details(101, "john", 20)


# __init__ method is a special method in python classes.
#  It is called when an object is created from the class and allows the class to initialize the attributes of the class.
class student:
    def __init__(self, sid, sname, sage): # constructor/ special method, sid, sname, sage are parameters or attributes of the class
        self.sid = sid
        self.sname = sname
        self.sage = sage
    def student_details(self): # instance method
        print(f"student id is {self.sid}")
        print(f"student name is {self.sname}")
        print(f"student age is {self.sage}")
s1 = student(101, "john", 20) # object creation
s1.student_details()
s2 = student(102, "jane", 21)
s2.student_details()


# create a class called employee with attributes eid, ename, esalary, edepartment and methods employee_details and working.
class employee:
    company_name = "ABC company" # class variable, it is shared by all the objects of the class
    def __init__(self, eid, ename, esalary, edepartment):
        self.eid = eid
        self.ename = ename
        self.esalary = esalary
        self.edepartment = edepartment

    def employee_details(self):
        print(f"employee id is {self.eid}")
        print(f"employee name is {self.ename}")
        print(f"employee salary is {self.esalary}")
        print(f"employee department is {self.edepartment}")

    def working(self):
        print(f"{self.ename} is working in {self.edepartment} department of {self.company_name}")

e1 = employee(101, "santhosh", 50000, "data science")
e1.employee_details()
e1.working()

e2 = employee(102, "john", 60000, "data engineering")
# re initializing the object e2 with new values
e2.ename = "siva"
e2.employee_details()
e2.working()




# bank application 
class bank:
    def __init__(self, bankid, branchname, branchmanager, ifsccode, contactnumber, location, branchamount):
        self.bankid = bankid
        self.branchname = branchname
        self.branchmanager = branchmanager
        self.ifsccode = ifsccode
        self.contactnumber = contactnumber
        self.location = location

    def bank_details(self):
        print(f"bank id is {self.bankid}")
        print(f"branch name is {self.branchname}")
        print(f"branch manager is {self.branchmanager}")
        print(f"ifsc code is {self.ifsccode}")
        print(f"contact number is {self.contactnumber}")
        print(f"location is {self.location}")

    def deposit(self, amount):
        self.branchamount = amount
        if amount> 0:
            self.branchamount += amount
            print(f"amount deposited is {self.branchamount}")
            print(f"total amount in the branch is {self.branchamount}")

b = bank(101, "sbi", "john", "sbi001", 1234567890, "chennai", 100000)
b.bank_details()
b.deposit(50000)

######################## day2 ###########################


class bank:
    def __init__(self, bankid, branchname, branchmanager,
                 ifscode, contactno, location, balance):
        self.bankid = bankid  # instance variable, unique to each object
        self.branchname = branchname
        self.branchmanager = branchmanager
        self.ifscode = ifscode
        self.contactno = contactno
        self.location = location
        self.balance = balance

    def deposit(self, amount):
        """Deposit amount into the balance."""
        # instance method; accesses instance variables
        if amount > 0:
            self.balance += amount
            print(f"amount deposited is {amount}")
        else:
            print("invalid amount")

    def check_balance(self):
        print(f"total balance is {self.balance}")


b = bank(
    101,
    "union bank",
    "santhosh",
    "ubi6565549",
    1234567890,
    "chennai",
    100000,
)  # object creation

b.check_balance()

b.deposit(500000)
b.check_balance()

# class methods are defined using the @classmethod decorator and take cls as the first parameter instead of self.
# class methods can access and modify class variables, but they cannot access instance variables.

class employee:
    company_name = "xyz company"  # class variable

    def __init__(self, ename, salary):
        self.ename = ename
        self.salary = salary

    def employee_details(self):
        print(f"employee name is {self.ename}")
        print(f"employee salary is {self.salary}")

    @classmethod
    def company_details(cls):
        # class method; cls is a reference to the class itself
        print("before re-initialize", cls.company_name)
        cls.company_name = "abc company"
        print("after re-initialize", cls.company_name)
        # print("employee is working in", cls.company_name)
        print("after re-initialize", cls.company_name)

e = employee("santhosh", 50000)
e.company_details() # calling class method without creating an object of the class

# static methods are defined using the @staticmethod decorator and do not take self or cls as the first parameter.
# static methods cannot access or modify class or instance variables, and they are used for utility functions

# outer class is animal and inner class is dog and cat. 
class animal:
    class dog:
        def __init__(self,dname,dcolor,dage,dbreed):
            self.dname = dname
            self.dcolor = dcolor
            self.dage = dage
            self.dbreed = dbreed
        def dog_details(self):
            print(f"dog name is {self.dname}")
            print(f"dog color is {self.dcolor}")
            print(f"dog age is {self.dage}")
            print(f"dog breed is {self.dbreed}")

    class cat:
        def __init__(self,cname,ccolor,cage,cbreed):
            self.cname = cname
            self.ccolor = ccolor
            self.cage = cage
            self.cbreed = cbreed
        def cat_details(self):
            print(f"cat name is {self.cname}")
            print(f"cat color is {self.ccolor}")
            print(f"cat age is {self.cage}")
            print(f"cat breed is {self.cbreed}")
d = animal.dog("tommy", "brown", 2, "labrador")
d.dog_details()
c = animal.cat("kitty", "white", 1, "persian")
c.cat_details()

###################### day3 ########################
# encapsulation is the process of hiding the internal details of an object
# and exposing only the necessary information to the outside world.


class bank:
    def __init__(self, customername, bankname, balance):
        # public member variable, can be accessed from outside the class
        self.customername = customername
        # protected member variable, can be accessed from outside the class
        # but should not be modified
        self.bankname = bankname
        # private member variable, can only be accessed from within the class
        self.__balance = balance
    
    def get_current_balance(self):
        print(f"current balance is {self.__balance}")
    
    def get_deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"amount deposited is {amount}")

    def del_current_balance(self):
        print(f"current balance is {self.__balance}")
        del self.__balance
        print(f" deleted current balance is {self.__balance}")

b = bank("santhosh", "union bank", 10000)
# # accessing public member variable
# print(b.customername)
# # accessing protected member variable
# print(b.bankname)
# # accessing private member variable
# print(b._bank__balance)


# b.get_current_balance()
# b.set_deposit(656531)
b.del_current_balance()

# b.__balance = 500000
# print(b.__balance)  # this will create a new variable __balance in the object b, it will not modify the private member variable __balance



# class name is employee and it has private member variable __salary and public member variable ename. emp id 


class employee:
    def __init__(self, ename, eid, esalary):
        self.ename = ename
        self.eid = eid
        self.__salary = esalary
    
    def display(self):
        print(f"employee name is {self.ename}")
        print(f"employee id is {self.eid}")
        print(f"employee salary is {self.__salary}")

    def update_salary(self, new_salary):
        self.__salary = new_salary
    
    def get_salary(self):
        return self.__salary
    
emp1 = employee("santhosh", 101, 50000)
print(emp1.eid)
print(emp1.ename)

print(emp1.get_salary()) # this is the correct way to access the private member variable __salary
emp1.update_salary(60000)
print("after updating salary", emp1.get_salary())
emp1.display()






class Employee:
    def __init__(self, employee_id, employee_name, department, salary):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.department = department
        self.__salary = salary  # private attribute

    @property
    def salary(self):
        return self.__salary
    
    @salary.setter
    def salary(self, value):
        if value > 0:
            self.__salary = value
        else:
            print("Salary cannot be negative.")
        

e1 = Employee(101, "santhosh kumar", "it", 45999)
print(e1.employee_id)
print(e1.employee_name)
print(e1.department)
print(e1.salary)  # accessing private attribute using getter

e1.salary = 10000
print(e1.salary)  # accessing private attribute using getter



# Task 
# Create an Employee class with attributes:
# Employee ID
# Employee Name
# Department
# Salary Display the employee details.
# Use a class variable to store the company name shared by all employees.
# Count the total number of employees using a class variable.
# Create a class method to change the company name for all employees.
# Create a static method to calculate income tax based on salary.
# Create a static method to validate an employee ID format.
# Make the salary attribute private and provide getter and setter methods.
# Validate the salary using a setter (salary cannot be negative).
# Delete an employee's salary using a property deleter.
# Create a read-only Employee ID using the @property decorator.
# Prevent users from assigning a salary greater than ₹10,00,000.


class Employee:
    company_name = "10kcoders"
    employee_count = 0  
    def __init__(self, emp_id, emp_name, department, salary):
        self.__emp_id = emp_id
        self.empname = emp_name
        self.department = department
        self.__salary = salary
        Employee.employee_count += 1  # Increment employee count

    @property
    def emp_id(self):
        return self.__emp_id

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value < 0:
            print("salary cannot be negative")
        elif value > 1000000:
            print("salary cannot be greater than 10,00,000")
        else:
            self.__salary = value

    @salary.deleter
    def salary(self):
        print("salary deleted")
        del self.__salary

    def display(self):
        print(f"Employee ID: {self.__emp_id}")
        print(f"Employee Name: {self.empname}")
        print(f"Department: {self.department}")
        print(f"Salary: {self.__salary}")
        print(f"Company Name: {Employee.company_name}")

    @classmethod
    def change_company_name(cls, new_name):
        cls.company_name = new_name

    @staticmethod
    def calculate_income_tax(salary):
        if salary <= 250000:
            return 0
        elif salary <= 500000:
            return salary * 0.05
        elif salary <= 1000000:
            return salary * 0.2
        else:
            return salary * 0.3

    @staticmethod
    def validate_employee_id(emp_id):
        if isinstance(emp_id, int) and emp_id > 0:
            return True
        else:
            return False

e1 = Employee(101, "santhosh", "it", 50000)
e1.display()

print(f"Income Tax: {Employee.calculate_income_tax(e1.salary)}")
print(f"Is Employee ID valid? {Employee.validate_employee_id(e1.emp_id)}")
print(f"Total Employees: {Employee.employee_count}")
print(f"Company Name: {Employee.company_name}")
print("Changing company name to 'TechCorp'")
Employee.change_company_name("TechCorp")

e1.salary = 1200000  # Attempt to set salary greater than 10,00,000
e1.salary = 800000  # Valid salary update
e1.display()
del e1.salary  # Deleting salary

#######################################################################
# Inheritance is a mechanism in object-oriented programming that allows a class to inherit properties and behaviors (methods) from another class.

#single inheritance is a type of inheritance where a child class inherits from a single parent class.
class Parent:
    def greet(self):
        print("Hello from Parent class")

class Child(Parent):
    def studying(self):
        print("Child is studying")

c = Child()
c.greet()
c.studying()

# multilevel inheritance is a type of inheritance where a class inherits
# from a child class, which in turn inherits from a parent class.
class Grandparent:
    def land(self):
        print("my grandparent has 10 acres of land")


class Parent(Grandparent):
    def home(self):
        print("my father has a home")


class Child(Parent):
    def bike(self):
        print("my child has a bike")


c = Child()
c.land()  # inherited from Grandparent
c.bike()
c.home()  # inherited from Parent


class Parent:
    def __init__(self, fathername, fathercontact):
        self.fathername = fathername
        self.fathercontact = fathercontact

    def info(self):
        print(f"father name is {self.fathername}")
        print(f"father contact is {self.fathercontact}")

    def greet(self):
        print(f"Hello from Parent class, {self.fathername}")


class Child(Parent):
    def __init__(self, name, contactno):
        super().__init__(
            self.childname = name,
            self.childcontact = contactno,
        )  # calling the constructor of the parent class
        self.childname = childname
        self.childcontact = childcontact

    def childinfo(self):
        print(f"child name is {self.childname}")
        print(f"child contact is {self.childcontact}")

    def studying(self):
        print(f"{self.childname} is studying dont disturb him")


c = Child("viswanath", 1234567890)

c.info()
c.greet()
c.studying()

















######################### day2##################
# multiple inheritance is a type of inheritance where a class can inherit from multiple parent classes.
class father:
    def land(self):
        print("my parent has 10 acres of land")

class mother:
    def gold(self):
        print("my mother has gold")

class child(father, mother):
    def bike(self):
        print(" it is my bike")

c = child()
c.land()
c.gold()
c.bike()

# example 2
class sqlexcept:
    def queries(self):
        print("sql queries is writing..")

class pythonexcept:
    def code(self):
        print("python code is writing to develop web apps")

class datascience(sqlexcept, pythonexcept):
    def model(self):
        print("by using ml i can buid a model")

d = datascience()
d.queries()
d.code()
d.model()



#################
# hierarchical inheritance is a type of inheritance where multiple child classes inherit from a single parent class.
class father:
    def land(self):
        print("my parent has 10 acres of land")

    def home(self):
        print("3bhk home is there")

class child1(father):
    def gold(self):
        print("my mother has gold")

class child2(father):
    def bike(self):
        print(" it is my bike")

c1 = child1()
c2 = child2()
print("---------------child1 details--------------")
c1.land()
c1.home()
c1.gold()

print("---------------child2 details--------------")
c2.land()
c2.home()
c2.bike()



class employee:
    def __init__(self, ename, eid, esalary, eloc):
        self.ename = ename
        self.eid = eid
        self.salary = esalary
        self.eloc = eloc
    
    def displayinfo(self):
        print(f"employee name is {self.ename}")
        print(f"employee id is {self.eid}")
        print(f"employee salary is {self.salary}")
        print(f"employee location is {self.eloc}")

class manager(employee):
    def additionalinfo(self, fathername):
        self.fathername = fathername

    def manageradditionalinfo(self):
        print(f"manager father name is {self.fathername}")

class pythondeveloper(employee):
    def aditionalinfo(self, fathername):
        self.fathername = fathername

    def pythonadditionalinfo(self):
        print(f"python developer father name is {self.fathername}")


m = manager("santhosh", 101, 50000, "chennai")
m.manageradditionalinfo("siva")
m.employee.info()



#########
# hybrid inheritance is a combination of two or more types of inheritance. It allows a class to inherit from multiple parent classes, which can be a combination of single, multiple, and hierarchical inheritance.

class A:
    def data(self):
        print("class A data")
class B(A):
    def dataa(self):
        print("class B data")
class C:
    def info(self):
        print("class C data")

class D(B, C):
    def details(self):
        print("class D data")

e = D()
e.data()
e.dataa()
e.info()

# parent is shape and add the child class as rectangle, circle, triangle. Add a method called display in the parent class and override it in the child classes to display the shape name. and area of the shape
class Shape:
    def __init__(self, shape_name):
        self.shape_name = shape_name
class Rectangle(Shape):
    def __init__(self, length, breadth):
        super().__init__("Rectangle")
        self.length = length
        self.breadth = breadth
    def area(self):
        return self.length * self.breadth
    def display(self):
        print(f"Shape name is {self.shape_name}")
        print(f"Area of rectangle is {self.area()}")
class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius
    def area(self):
        return 3.14 * self.radius * self.radius
    def display(self):
        print(f"Shape name is {self.shape_name}")
        print(f"Area of circle is {self.area()}")
class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__("Triangle")
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height
    def display(self):
        print(f"Shape name is {self.shape_name}")
        print(f"Area of triangle is {self.area()}")


r = Rectangle(10, 20)
r.display()

c = Circle(10)
c.display()

t = Triangle(10, 20)
t.display()


# with patterns
class Shape:
    def __init__(self, shape_name):
        self.shape_name = shape_name


class Rectangle(Shape):
    def __init__(self, length, breadth):
        super().__init__("Rectangle")
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def pattern(self):
        for i in range(self.breadth):
            print("* " * self.length)

    def display(self):
        print(f"Shape Name : {self.shape_name}")
        print(f"Area       : {self.area()}")
        print("Pattern:")
        self.pattern()


class Circle(Shape):
    def __init__(self, radius):
        super().__init__("Circle")
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def pattern(self):
        print("   ***")
        print(" *     *")
        print("*       *")
        print("*       *")
        print(" *     *")
        print("   ***")

    def display(self):
        print(f"Shape Name : {self.shape_name}")
        print(f"Area       : {self.area()}")
        print("Pattern:")
        self.pattern()


class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__("Triangle")
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def pattern(self):
        for i in range(1, self.height + 1):
            print("* " * i)

    def display(self):
        print(f"Shape Name : {self.shape_name}")
        print(f"Area       : {self.area()}")
        print("Pattern:")
        self.pattern()


r = Rectangle(5, 3)
r.display()

print()

c = Circle(5)
c.display()

print()

t = Triangle(10, 5)
t.display()

#school is parent class and, school name is class variable and stu_name, stu_marks,stu_class  and add the student1 details and student2 details and display the school name and student details
class School:
    school_name = "10kcoders"
class Student(School):
    def __init__(self, stu_name, stu_marks, stu_class):
        self.stu_name = stu_name
        self.stu_marks = stu_marks
        self.stu_class = stu_class

    def display(self):
        print("-----------------Student Details-----------------")
        print(f"school name is {self.school_name}")
        print(f"student name is {self.stu_name}")
        print(f"student marks is {self.stu_marks}")
        print(f"student class is {self.stu_class}")

class Student1(Student):
    def __init__(self, stu_name, stu_marks, stu_class):
        super().__init__(stu_name, stu_marks, stu_class)

class Student2(Student):
    def __init__(self, stu_name, stu_marks, stu_class):
        super().__init__(stu_name, stu_marks, stu_class)

s1 = Student1("santhosh", 90, "10th") 
s2 = Student2("john", 80, "10th")
s1.display()
s2.display()

#######################################################################
# polynorphism is a concept in object-oriented programming that allows objects of different classes to be treated as objects of a common superclass. 
# It enables a single interface to represent different underlying forms (data types).

# method overriding is a feature of polymorphism where a subclass provides a specific implementation of a method that is already defined in its superclass.
# same methods name but different implementation in the child class
class Animal:
    def sound(self):
        pass
class Dog(Animal):
    def sound(self):
        print("Dog barks")
class Cat(Animal):
    def sound(self):
        print("Cat meows")
d = Dog()
d.sound()
c=Cat()
c.sound()

# example 2
class Employee:
    def work(self):
        print("Employee is working")
class Developer(Employee):
    def work(self):
        print("Developer is coding")
class testing(Employee):
    def work(self):
        print("Tester is testing")

t = testing()
t.work()
d = Developer()
d.work()

# example 3
class Bank:
    def __init__(self, bank_name):
        self.bank_name = bank_name
class SBI(Bank):
    def interest_rate(self):
        print("SBI interest rate is 5.0%")
class HDFC(Bank):
    def interest_rate(self):
        print("HDFC interest rate is 6.0%")
class ICICI(Bank):
    def interest_rate(self):
        print("ICICI interest rate is 7.0%")

s = SBI("SBI")
s.interest_rate()
h = HDFC("HDFC")
h.interest_rate()
i = ICICI("ICICI")
i.interest_rate()

##############################
# duck typing is a concept in programming where the type or class of an object is determined by its behavior (methods and properties) rather than its explicit declaration.
# In duck typing, if an object behaves like a certain type (i.e., it has the necessary methods and properties), it can be treated as that type, regardless of its actual class.
# method name is same but different implementation in the class

class Bird:
    def fly(self):
        print("Bird is flying")

class Airplane:
    def fly(self):
        print("Airplane is flying")

class superman:
    def fly(self):
        print("superman is flying")

def flying(other):
    other.fly()

b = Bird() # creating an object of Bird class
flying(b) # calling the fly method of Bird class
a = Airplane()
flying(a) # calling the fly method of Airplane class
s = superman()
flying(s) # calling the fly method of superman class
