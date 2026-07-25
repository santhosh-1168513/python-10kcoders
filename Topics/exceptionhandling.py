# exception handling is a mechanism to handle runtime errors in a program. 
# It allows the program to continue executing even when an error occurs, instead of crashing.

from langsmith import expect


try:
    a = int(input("enter a values"))
    b = int(input("enter a values"))
    if a > b:
        print("a is greater than b")
except Exception:
    print("programmer pls check the code")
else:
    print(f" 100% done")
print("program is running")


# 
try:
    a = int(input("enter a values"))
    b = int(input("enter a values"))
    print(a/b)
except ZeroDivisionError:
    print("cannot divide by zero")
except ValueError:
    print("please enter a valid number")
else:
    print(f" 100% done")
finally:
    print("program is running")


try:
    with open("fruits.txt", "r") as f:
        data = f.read()
        print(data)
    a = 10
    b = 0
    print(a/b)
    v1 = int(input("enter a values"))
    v2 = int(input("enter a values"))
    print(v1+v2)
except FileNotFoundError:
    print("file not found")
except ZeroDivisionError:
    print("cannot divide by zero")
except ValueError:
    print("please enter a valid number")
else:
    print(f" 100% done")
finally:
    print("program is running")


# we dont the type of error we can use exception class to handle all the errors
try: 
    age = int(input("enter your age"))
    if age < 18:
        print("you are not eligible to vote")
except exception as e:
     print(type(e).__name__)
     print(f"type of error is {type(e).__name__} and error message is {e}")



age = int(input("enter your age"))
if age < 0:
    raise "values cannot be negative"

