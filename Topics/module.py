# module is a file that contains Python code, which can include functions, classes, and variables. 
# It can be imported and used in other Python files or scripts. 
# Modules help organize code into reusable components, making it easier to maintain and share.

# types of modules
# 1. Built-in modules: These are modules that come with Python and are available for
# use without any additional installation. Examples include math, os, sys, and random.
# 2. User-defined modules: These are modules created by users to organize their own code.

# how to import a module and types of import
# 1. import module_name: This imports the entire module, and you can access its functions and variables using the module name as a prefix. For example:
# import math
# 2. from module_name import function_name: This imports a specific function or variable from the module, allowing you to use it directly without the module name prefix. For example:
# from math import sqrt
# 3. from module_name import *: This imports all functions and variables from the module

# math module is a built-in module in Python that provides mathematical functions and constants. 
# It includes functions for basic arithmetic operations, trigonometry, logarithms, and more. 
# Some commonly used functions in the math module include sqrt(), sin(), cos(), tan(), log(), and factorial().
#  The math module also provides constants such as pi and e.

import math
# from math import sqrt # to import only sqrt function from math module
# from math import * # to import all functions from math module
print(math.sqrt(16))  # Output: 4.0
print(math.ceil(1099.90))  # Output: 1100
print(math.floor(1099.999999999))  # Output: 1099
print(math.trunc(1099.90))  # Output: 1099 # trunc() returns the integer part of a number by removing the decimal part, effectively truncating it towards zero.
print(math.factorial(5))  # Output: 120
print(math.pi)  # Output: 3.141592653589793
print(math.log(10))
print(math.log2(8))  # Output: 3.0
print(math.log10(100))
print(math.log(100, 10))  # Output: 2.0
# print(math.modf(10, 3))  # its remove the decimal part and integerpart
print(math.exp(2))  # Output: 7.38905609893065
print(math.pow(2, 3))  # Output: 8.0
print(math.radians(180))  # Output: 3.141592653589793
print(math.degrees(math.pi))  # Output: 180.0
print(math.isqrt(16))  # Output: 4 isqrt() returns the integer square root of a non-negative integer. It is equivalent to floor(sqrt(n)).
print(math.gcd(12, 18))  # Output: 6
print(math.lcm(12, 18))  # Output: 36
print(math.fabs(-5.5))  # Output: 5.5 fabs() returns the absolute value of a number as a float. its convert the negative values to positive values
print(math.fmod(10, 3))  # Output: 1.0 fmod() returns the remainder of the division of two numbers.
print(math.sin(math.pi/2))  # Output: 1.0
print(math.cos(0))  # Output: 1.0
print(math.tan(math.pi/4))  # Output: 1.0 why math.pi/4 is used in the above example because it represents a 45-degree angle in radians, which is the input for the tangent function to return a value of 1.0
print(math.sin(math.radians(90)))  # Output: 1.0


# random module is a built-in module in Python that provides functions for generating random numbers and performing random operations.
# It includes functions for generating random integers, floating-point numbers, and selecting random elements from sequences
import random
print(random.random()) # it produce the output within the range of 0.0 to 1.0 range
print(random.randint(1, 10)) # it produce the output within the range of 1 to 10 range
print(random.randrange(1, 10, 3)) # it produce the output within the range of 1 to 10 range with step size of 3
print(random.uniform(1.0, 5.0)) # it produce the output within the range of 1 to 5 range with decimal values

list1 = [1, 2, 3, 4, 5]
print(random.choice(list1))  # it produce the output from the list1 randomly
list2 = ['apple', 'banana', 'cherry', 'date', 'date']
print(random.choice(list2))  # it produce the output from the list2 randomly
print(random.choices(list2, k=2))  # it produce the output from the list2 randomly with k=2 means it will return 2 random elements from the list
print(random.choices(list2, k=4))  # allows duplicates, so the same element can be selected multiple times in the output list.
print(random.sample(list2, k=2))  # it produce the output from the list2 randomly with k=2 means it will return 2 random elements from the list but it will not allow duplicates

random.shuffle(list1)
print(list1)   # it will shuffle the list1 randomly

# random.seed(2)   # it will set the seed for the random number generator, ensuring that the sequence of random numbers generated is reproducible.
# print(random.randint(1,10))  

dice = random.randint(1, 11)  
print(f"rolling dice: {dice}")  

coinface = random.choice(['Heads', 'Tails'])
print(f"flipping coin: {coinface}")

# Generate a list of 5 random numbers between 1 and 100
num = [random.randint(1,100) for _ in range(5)]
print(f"random numbers: {num}")

# method 2
num =[]
for i in range(5):
    num.append(random.randint(1,100))
print(f"random numbers: {num}")


# wpp to find out 4 appers in rolling dices roll the dices 100 times and find out how many times 4 appears in the output
count = 0
for i in range(100):
    dice = random.randint(1,6)
    if dice == 4:
        count += 1
print(f"4 appeared {count} times in 100 rolls of the dice.")

# wpp  to find our how many times 1, 2, 3, 4, 5, 6 appears in rolling dices roll the dices 100 times and find out how many times each number appears in the output
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0
count6 = 0
# count1 = count2 = count3 = count4 = count5 = count6 = 0
for i in range(100):
    dice = random.randint(1,6)
    if dice == 1:
        count1 += 1
    elif dice == 2:
        count2 += 1
    elif dice == 3:
        count3 += 1
    elif dice == 4:
        count4 += 1
    elif dice == 5:
        count5 += 1
    else:
        count6 += 1
print(f"1 appeared {count1} times in 100 rolls of the dice.")
print(f"2 appeared {count2} times in 100 rolls of the dice.")   
print(f"3 appeared {count3} times in 100 rolls of the dice.")
print(f"4 appeared {count4} times in 100 rolls of the dice.")
print(f"5 appeared {count5} times in 100 rolls of the dice.")
print(f"6 appeared {count6} times in 100 rolls of the dice.")
print("---------------------------------------------------")

# method 2
c = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0}
for i in range(100):
    dice = random.randint(1, 6)
    c[dice] += 1
print(f"1 appeared {c[1]} times in 100 rolls of the dice.")
print(f"2 appeared {c[2]} times in 100 rolls of the dice.")
print(f"3 appeared {c[3]} times in 100 rolls of the dice.")
print(f"4 appeared {c[4]} times in 100 rolls of the dice.")
print(f"5 appeared {c[5]} times in 100 rolls of the dice.")
print(f"6 appeared {c[6]} times in 100 rolls of the dice.")

# guess the number game
guess = int(input("Guess a number between 1 and 100: "))
secret_number = random.randint(1, 100)
while guess != secret_number:
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("You guessed the number.")
    break
print("---------------------------------------------------")


secret_number = random.randint(1, 100)
while True:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("You guessed the number.")
        break


    
###########################################################################
# re module is a built-in module in Python that provides functions for working with regular expressions.
# It includes functions for pattern matching, searching, and manipulating text.

import re
s = "python is easy to  to learn"
txt =re.match('python', s)
# match() function is used to check if the beginning of a string matches a specified pattern.
print(txt)  # Output: <re.Match object; span=(0, 6), match='python'>
print(txt.group())  # Output: python

# search() function is used to search for a pattern in a string and returns the first occurrence of the pattern.
txt = re.search('easy', s)
print(txt)  # Output: <re.Match object; span=(13, 17), match='easy'>
print(txt.group())  # Output: easy

# findall() function is used to find all occurrences of a pattern in a string and returns them as a list.
import re
s = "python is easy to  to learn"
txt = re.findall('to', s)
print(txt)  # Output: ['to' 'to']


import re
paragraph = """
Python is a high-level, interpreted programming language that is widely used for web development, data analysis, artificial intelligence, and scientific computing. It was created by Guido van Rossum and first released in 1991. Python's design philosophy emphasizes code readability and simplicity, making it an ideal language for beginners and experienced programmers alike.
Python supports multiple programming paradigms, including procedural, object-oriented, and functional programming. It has   a large standard library that provides a wide range of modules and packages for various tasks, such as file I/O, networking, and database access. Python also has a vibrant community that contributes to its development and provides support through forums, tutorials, and documentation.
Python's popularity has grown rapidly in recent years, and it is now one of the most widely used programming languages in the world. Its versatility, ease of use, and extensive library support make it a popular choice for developers across different industries and domains.
"""
txt = re.findall('Python', paragraph)
print(txt)  

# finditer() function is used to find all occurrences of a pattern in a string and returns an iterator that yields match objects for each occurrence.
import re
paragraph = """
Python is a high-level, interpreted programming language that is widely used for web development, data analysis, artificial intelligence, and scientific computing. It was created by Guido van Rossum and first released in 1991. Python's design philosophy emphasizes code readability and simplicity, making it an ideal language for beginners and experienced programmers alike.
Python supports multiple programming paradigms, including procedural, object-oriented, and functional programming. It has   a large standard library that provides a wide range of modules and packages for various tasks, such as file I/O, networking, and database access. Python also has a vibrant community that contributes to its development and provides support through forums, tutorials, and documentation.
Python's popularity has grown rapidly in recent years, and it is now one of the most widely used programming languages in the world. Its versatility, ease of use, and extensive library support make it a popular choice for developers across different industries and domains.
"""
tx = re.finditer('Python', paragraph)
for match in tx:
    print(match.group(),match.start(), match.end())  
# 0utput:
# Python 1 7
# Python 228 234
# Python 376 382
# Python 646 652
# Python 785 791

# sub() function is used to replace occurrences of a pattern in a string with a specified replacement string.
import re
paragraph = """
Python is a high-level, interpreted programming language that is widely used for web development, data analysis, artificial intelligence, and scientific computing. It was created by Guido van Rossum and first released in 1991. Python's design philosophy emphasizes code readability and simplicity, making it an ideal language for beginners and experienced programmers alike.
Python supports multiple programming paradigms, including procedural, object-oriented, and functional programming. It has   a large standard library that provides a wide range of modules and packages for various tasks, such as file I/O, networking, and database access. Python also has a vibrant community that contributes to its development and provides support through forums, tutorials, and documentation.
Python's popularity has grown rapidly in recent years, and it is now one of the most widely used programming languages in the world. Its versatility, ease of use, and extensive library support make it a popular choice for developers across different industries and domains.
"""
txt = re.sub('Python', 'Java', paragraph)  # it will replace all occurrences of 'Python' with 'Java' in the paragraph
print(txt)

# split() function is used to split a string into a list of substrings based on a specified delimiter.
# syntax: re.split(pattern, string, maxsplit=0, flags=0)
import re
txt = "python, java, c++, c#, javascript"
txt1 = "python,java;c++ c# javascript"
result = re.split(', ', txt)  # it will split the string into a list of substrings based on the delimiter ', '
result1 = re.split('[,; ]', txt1)  # it will split the string into a list of substrings based on the delimiters ', ', ';' and ' '
print(result)  # Output: ['python', 'java', 'c++', 'c #', 'javascript']
print(result1)  # Output: ['python', 'java', 'c++', 'c#', 'javascript']



# symbols used in regular expressions with examples
# 1. . (dot): Matches any single character except a newline.
# Example: re.findall('p.t', 'pat, pet, pit, pot, put') will match 'pat', 'pet', 'pit', 'pot', and 'put'.
# 2. ^ (caret): Matches the start of a string.
# Example: re.findall('^p', 'python, java, c++') will match 'p' at the start of the string.
# 3. $ (dollar sign): Matches the end of a string.
# Example: re.findall('t$', 'python, java, c++') will match '
#t' at the end of the string.
# 4. * (asterisk): Matches zero or more occurrences of the preceding character or group.
# Example: re.findall('p*', 'ppython, java, c++') will match 'pp' and 'p' in 'ppython'.
# 5. + (plus): Matches one or more occurrences of the preceding character or group
# Example: re.findall('p+', 'ppython, java, c++') will match 'pp' in 'ppython'.
# 6. ? (question mark): Matches zero or one occurrence of the preceding character or group.
# Example: re.findall('p?', 'ppython, java, c++') will match 'p' in 'ppython'.
# 7. [] (square brackets): Matches any single character within the brackets.
# Example: re.findall('[aeiou]', 'python, java, c++') will match 'o', 'a', and 'a' in the string.

emailid = ['santhosh@gmail,com', 'siva@gmail.com', 'vani.com', 'qwe.in']
validemail = []
pattern = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$" # explain this line
for email in emailid:
    if re.match(pattern, email):
        validemail.append(email)

print("Valid email addresses:")
for email in validemail:
    print(email)
###########################################################3

# os module 
# os module is used to interact with the operating system
import os
print(os.getcwd())  # Output: current working directory 

os.chdir('C:\\Users\\Santhosh\\Desktop')  # change the current working directory to the specified path

os.makedirs('C:\\Users\\Santhosh\\Desktop\\NewFolder')  # create a new directory at the specified path

# to create a new file in the specified directory
import os
# os.chdir('c:\\Users\\sivasankar\\Downloads\\python pratices')  # change the current working directory to the specified path
# os.open('newfile.', os.O_CREAT)  # create a new file named 'newfile.txt' in the current working directory
print(os.getcwd())  # Output: current working directory
os.chdir('C:\\Users\\Santhosh\\Desktop\\NewFolder')  # change the current working directory to the specified path
os.open('newfile.txt', os.O_CREAT)  # create a new file named 'newfile.txt' in the current working directory
os.rename('newfile.txt', 'renamedfile.txt')  # rename the file 'newfile.txt' to 'renamedfile.txt'
os.remove('renamedfile.txt')  # delete the file 'renamedfile.txt'
import os
print(os.path.exists('C:\\Users\\Santhosh\\Desktop\\NewFolder'))  # check if the specified path exists


# sys module is a built-in module in Python that provides access to some variables used or maintained by the interpreter and to functions that interact with the interpreter.
import sys
print(sys.version)
print(sys.platform)

print("program started")
sys.exit()  # exit the program
print("program ended")  # this line will not be executed because the program has exited


#########################################################
# copy module is a built-in module in Python that provides functions for creating shallow and deep copies of objects.
# shallow copy creates a new object that is a copy of the original object, but it does not create copies of the objects that are referenced by the original object. Instead, it copies the references to those objects. This means that if you modify a mutable object in the shallow copy, it will also affect the original object.
import copy
list = [1, 2, 3, [4, 5]]

# list[3][0] = 5  # modifying the original list
list[0]= 1000
list2 = copy.copy(list)  # shallow copy
print(f"original list: {list}, shallow copy: {list2}")

# deep copy creates a new object that is a copy of the original object, and it also creates copies of all the objects that are referenced by the original object. This means that if you modify a mutable object in the deep copy, it will not affect the original object.
import copy
list = [1, 2, 3, [4, 5]]
copy.deepcopy(list)  # deep copy
l3 = copy.deepcopy(list)
list[3][0] = 5  # modifying the original list
print(f"original list: {list}, deep copy: {l3}")

####################################################################

# json module is a built-in module in Python that provides functions for working with JSON (JavaScript Object Notation) data. It includes functions for encoding and decoding JSON data, as well as for working with JSON objects and arrays.
# dump () function is used to serialize a Python object and write it to a file in JSON format.
import os.open("main.json", os.O_CREAT)
d  = {
    "empid": [1,2,3]
    ,"empname": ["santhosh", "siva", "vani"]
    ,"location": ["chennai", "bangalore", "hyderabad"]

}

import json
with open("main.json", "w") as f:
    json.dump(d, f)  # write the dictionary d to the file main.json in JSON format

import os
os.open("usercredentials.json", os.O_CREAT)
usercredentials = {
    
    "username": "santhosh"
    ,"password": 1234
}

with open("usercredentials.json", "w") as f:
    json.dump(usercredentials, f)   # write the dictionary usercredentials to the file usercredentials.json in JSON format
print("data written to the file usercredentials.json in JSON format")

#############################################################################
# time module

import time
print(time.time())

print(time.localtime())

# measure the execution time of a code block
import time
start = time.time()
for i in range(1000000):
    pass
end = time.time()
print(f"Execution time: {end - start} seconds")

# sleep() function is used to pause the execution of a program for a specified number of seconds.
import time
print("start")
time.sleep(5)  # sleep for 5 seconds
print("end")

import time
for i in range(5,0,-1):
    print(i)
    time.sleep(1)
print("Done")

# time,strftime() function is used to format a time object as a string according to a specified format.
import time
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))  # Output: current date and time in the format YYYY-MM-DD HH:MM:SS

# | Function         | Purpose                              |
# | ---------------- | ------------------------------------ |
# | `time()`         | Current timestamp in seconds         |
# | `sleep()`        | Pause execution                      |
# | `ctime()`        | Human-readable time                  |
# | `localtime()`    | Local structured time                |
# | `gmtime()`       | UTC structured time                  |
# | `strftime()`     | Format date/time                     |
# | `strptime()`     | Parse date/time string               |
# | `mktime()`       | Convert structured time to timestamp |
# | `perf_counter()` | High-precision performance timer     |
# | `process_time()` | CPU execution time                   |


#########################################################################
# calendar module is a built-in module in Python that provides functions for working with calendars and dates. It includes functions for generating calendars, checking leap years, and performing date calculations.
import calendar
print(calendar.month(2024, 6))  
print(calendar.calendar(2026))
print(calendar.isleap(2024))  # Output: True
print(calendar.isleap(2023))  # Output: False
print(calendar.leapdays(2000, 2024))  # Output: 6
print(calendar.monthrange(2026, 7)) # Output: (2, 31)
print(calendar.weekday(2024, 6, 1))  # Output: 5
# 0 is Monday, 1 is Tuesday, 2 is Wednesday, 3 is Thursday, 4 is Friday, 5 is Saturday, and 6 is Sunday.
# | Function                    | Purpose                          |
# | --------------------------- | -------------------------------- |
# | `calendar(year)`            | Print the entire year's calendar |
# | `month(year, month)`        | Print one month's calendar       |
# | `isleap(year)`              | Check if it's a leap year        |
# | `leapdays(start, end)`      | Count leap years in a range      |
# | `monthrange(year, month)`   | First weekday and number of days |
# | `weekday(year, month, day)` | Day of the week                  |
# | `day_name`                  | Weekday names                    |
# | `month_name`                | Month names                      |

###############################################################################
# datetime module is a built-in module in Python that provides classes for manipulating dates and times. It includes classes for representing dates, times, and time intervals, as well as functions for formatting and parsing date and time strings.
import datetime
from datetime import datetime,time
print(datetime.now())  # Output: current date and time
print(datetime.today())  # Output: current date and time

from datetime import datetime
now = datetime.now()
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print(now.microsecond)

presentdate = datetime.now()

furturedate = presentdate + timedelta(days=10)  # add 10 days to the present date
print(f"Present date: {presentdate}, Future date: {furturedate}")
############################################################################

#statistics module is a built-in module in Python that provides functions for performing statistical calculations on data. It includes functions for calculating measures of central tendency, dispersion, and correlation, as well as functions for generating random samples and distributions.
import statistics
marks = [80, 90, 70, 60, 50]
print(statistics.mean(marks))  # Output: 70.0
print(statistics.median(marks))  # Output: 70.0
print(statistics.mode(marks))  # Output: 80
print(statistics.multimode(marks)) #Returns all values with the highest frequency.

values = [1, 2, 3, 4, 5]
print(statistics.stdev(values))  # Output: 1.5811388300841898
print(statistics.variance(values))  # Output: 2.5

# to find out givrn year is leap year or not
year = int(input("Enter a year: "))
if calendar.isleap(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

# to find out age by taking date of birth as input
from datetime import datetime
dob = input("Enter your date of birth (YYYY-MM-DD): ")
dob = datetime.strptime(dob, "%Y-%m-%d")
today = datetime.now()
print(f"Your age is: {today.year - dob.year} years.")

dob =datetime.strptime(input("Enter your date of birth (YYYY-MM-DD): "), "%Y-%m-%d")
# print(dob)

todaydate = datetime.today()
age=(int(todaydate.strftime("%Y")) - int(dob.strftime("%Y")))
print(f"Your age is: {age} years.")

#outlier is a value that is significantly different from the other values in a dataset. 
# It can be much higher or much lower than the other values, and it can have a significant impact on statistical calculations such as the mean and standard deviation.

# | Function           | Purpose                       |
# | ------------------ | ----------------------------- |
# | `mean()`           | Average                       |
# | `median()`         | Middle value                  |
# | `mode()`           | Most frequent value           |
# | `multimode()`      | Multiple modes                |
# | `fmean()`          | Fast mean                     |
# | `variance()`       | Sample variance               |
# | `stdev()`          | Sample standard deviation     |
# | `pvariance()`      | Population variance           |
# | `pstdev()`         | Population standard deviation |
# | `geometric_mean()` | Geometric mean                |
# | `harmonic_mean()`  | Harmonic mean                 |



######################################################3
# user -defined modules
from Topics.calculator import *
# from calculator import add, sub, mul  # to import specific functions from the module
add(20,30)

##
import Topics.calculator as c
c.add(20,30)
c.sub(50,20)
c.mul(10,2)



import Topics.calculator as c
c.deposit()
print(c.bankname)


# write a p crate a emp module with emp details and display them from the main module 
#importing emp module from calculator.py
from Topics.calculator import emp_details
emp_details("santhosh", 22, 50000, "9581927787")
