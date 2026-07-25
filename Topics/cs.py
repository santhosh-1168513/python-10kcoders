#write a program as a age if age is more than 18 print like adult, age is more than 40 print senior citizen, 
# age is more than 60 print like old man, if no condition print like dead man
age = int(input("enter your age:"))
if age <= 18:
    print("child")
elif age >= 18 and age < 40:
    print("adult")
elif age >= 40 and age < 60:
    print("senior citizen")
elif age >= 60 and age < 100:
    print("old-man")
else:
    print("dead-man")

# wpa a by taking a use input as marks if amrks is present in range of 35 and 50 display grade as c, 
# if marks is present in range of 50 and 75 display grade as b, if marks is present in range of 75 and 100 display grade as a, if marks is less than 35 display fail
marks = int(input("enter your marks:"))
if marks < 35:
    print("fail")
elif marks >= 35 and marks < 50:
    print("grade c")
elif marks >= 50 and marks < 75:
    print("grade b")
elif marks >= 75 and marks <= 100:
    print("grade a")
else:
    print("invalid marks")
    

# wap verify the stu name is santhosh if yes calculate the grade based on the marks
stu = input("enter your name:")
if stu == "santhosh":
    print("name is verified ")
    marks = int(input("enter your marks:"))
    if marks < 35:
        print("fail")
    elif marks >= 35 and marks < 50:
        print("grade c")
    elif marks >= 50 and marks < 75:
        print("grade b")
    elif marks >= 75 and marks <= 100:
        print("grade a")
    else:
        print("invalid marks")
else:
    print("name is not valided")

# Verify username and password, then assign role (Admin/User/Guest).
role = input("Enter your role (Admin/User/Guest): ")
if role == "admin":
    print("welcome admin, you get the assess")
elif role == "user":
    print("welcome user, you get the assess")
else:
    print("welcome guest, you get the assess")

# Verify customer ID, then calculate discount and final bill.
ci = int(input("enter your customer id:"))
if ci == 12345:
    print("customer id is verified")
    bill_amount = float(input("enter the bill amount:"))
    if bill_amount > 1000:
        discount = bill_amount * 0.1
        final_bill = bill_amount - discount
        print(f"you get a discount of {discount}, your final bill is {final_bill}")
    else:
        print("you are not eligible for discount, your final bill is", bill_amount)
else:
    print("customer id is not valided")
    
# Verify student name, attendance, and marks, then decide eligibility and grade.
stu = input("enter your name:")
if stu == "santhosh":
    print("name is verified")
    att = int(input("enter your attendance percentage:"))
    if att >= 75:
        print("you are eliable for grade calculation")
        marks = int(input("enter your marks:"))
        if marks < 35:
            print("fail")
        elif marks >= 35 and marks < 50:
            print("grade c")
        elif marks >= 50 and marks < 75:
            print("grade b")
        elif marks >= 75 and marks <= 100:
            print("grade a")
        else:
            print("invalid marks")
    else:
        print("you are not eligible for grade calculation")
else:
    print("name is not valid")

# Verify account number, PIN, and balance before withdrawal.
acc_num = int(input("enter your account number:"))
if acc_num == 123456789:
    print("account nummber is verified")
    pin = int(input("enter your pin number:"))
    if pin == 1234:
        print("pin number is verifed")
        balance = float(input("enter the balance amount to withdraw:"))
        if balance >= 1000:
            print("you are eligible for withdrawal")
        else:
            print("you are not eligible for withdrawal")
    else:
        print("pin number is not verified")
else:
    print("account number is not valided")

# Verify employee ID, department, and salary before calculating bonus.
emp_id = int(input("enter the employee id:"))
if emp_id == 12345:
    print("employee id is verified")
    dept = input("enter the department:")
    if dept == "it":
        print("department is verified")
        sal = float(input("enter the salary:"))
        if sal > 0:
            bouns = sal * 0.5
            print(f"you bouns is {bouns}")
            print(f"your total salary is {sal + bouns}")
        else:
            print("invalid salary")
    else: 
        print("department is not verified")
else:
    print("employee id is not valided")

#leap year checker
year = int(input("enter the year:"))
if year %4 == 0:
    if year %100 == 0:
        if year %400 == 0:
            print(f"{year} is a leap year")
        else:
            print(f"{year} is not a leap year")
    else:
        print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")

#Check whether a number is positive, negative, or zero using nested if.
num = int(input("enter the number:"))
if num > 0:
    print(f"{num} is a positive number")
elif num < 0:
    print(f"{num} is a negative number")
else:
    print(f"{num} is zero")

