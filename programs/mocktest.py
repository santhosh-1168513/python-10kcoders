# # # right angled triangle
# # #Write a Python program to print a right-angled triangle of stars for n = 5.
# # n = 5
# # for row in range(1, n+1):
# #     for star in range(row):
# #         print("*", end=" ")
# #     print()
# # print()

# # n = 5
# # for row in range(n, 0, -1):
# #     for star in range(row):
# #         print("*", end=" ")
# #     print()

# # #Write a Python program to print a centred pyramid of stars for n = 5.
# # n = 5
# # for row in range(1, n+1):
# #     for space in range(n-row):
# #         print(" ", end=" ")
# #     for star in range(2*row-1):
# #         print("*", end=" ")
# #     print()

# # #Write a Python program to print a diamond shape of stars for n = 5.
# # n = 5
# # for row in range(1, n+1):
# #     for space in range(n-row):
# #         print(" ", end=" ")
# #     for star in range(2*row-1):
# #         print("*", end=" ")
# #     print()
# # for row in range(n-1, 0, -1):
# #     for space in range(n-row):
# #         print(" ", end=" ")
# #     for star in range(2*row-1):
# #         print("*", end=" ")
# #     print()

# # #Write a Python program to print a hollow pyramid of stars for n = 5.
# # n =5
# # for row in range(1, n+1):
# #     for space in range(n-row):
# #         print(" ", end=" ")
# #     for star in range(2*row-1):
# #         if star == 0 or star == 2*row-2 or row == n:
# #             print("*", end=" ")
# #         else:
# #             print(" ", end=" ")
# #     print()












# # #string programs
# # p = input("enter a string:")
# # if p == p[::-1]:
# #     print(f" {p} is a palindrome")
# # else:
# #     print(f" {p} is not a palindrome")


# # #Write a Python program to determine if two strings are anagrams of each other. Ignore case.
# # s1 = input("enter the first string:")
# # s2 = input("enter the second string:")
# # if sorted(s1) == sorted(s2):
# #     print(f"{s1} and {s2} are angram")
# # else:
# #     print(f"{s1} and {s2} are not anagram")

# # #Write a Python program to count the frequency of each character in a string. Ignore spaces.
# # n = "hell0 world"
# # freq = {}
# # for ch in n:
# #     if ch in freq:
# #         freq[ch] = freq[ch] + 1
# #     else:
# #         freq[ch] = 1
# # print(freq)
# # #Write a Python program to reverse a given string without using slicing (not s[::-1]).
# # input = "python"
# # output = ""
# # for ch in input:
# #     output = ch + output
# # print(f"Reversed string: {output}")

# # #Write a Python program to find the first character in a string that appears only once. Return none if not found
# # n = "aabb"
# # for ch in n:
# #     if n.count(ch) == 1:
# #         print(ch)
# #         break
# #     else:
# #         print("None")





# #Write a Python program to check if a number is prime.
# num = int(input("Enter a number: "))
# if num > 1:
#     for i in range(2, num+1):
#         if num % i == 0:
#             print(f"{num} is not a prime number")
#             break
#     else:
#         print(f"{num} is a prime number")
# else:
#     print(f"{num} is not a prime number")

# #Write a Python program to check if a number is prime.
# n = int(input("Enter a number: "))
# a = 0
# b =1
# for i in range(n):
#     c = a+b
#     a=b
#     b=c
#     print(c, end=" ")

# #Write a Python program to check whether a number is a perfect number (sum of proper divisors excluding the number itself).
# num = int(input("Enter a number: "))
# sum = 0
# for i in range(1, num):
#     if num % i == 0:
#         sum += i
# if sum == num:
#     print(f"{num} is a perfect number")
# else:
#     print(f"{num} is not a perfect number")

# # Write a Python program to find the factorial of a number.
# n = int(input("Enter a number: "))
# n = 5
# for i in range(1, n+1):
#     fact = 1
#     fact *= i
#     print(f"Factorial of {i} is {fact}")
# print(f"Factorial of {n} is {fact}")

# #Write a Python program to calculate the sum of all digits of a given non-negative integer.
# num = 1234
# total = 0
# while num > 0:
#     digit = num % 10
#     total += digit
#     num //= 10
# print(f"Sum of digits: {total}")

# MOCK TEST 11-07-2026
# . Count the frequency of each word in a sentence.
sentance = input("Enter a sentence: ")
word = sentance.split()
freq = {}
for word in sentance:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1
print(freq)

# 2. Check if a number is prime.  
num = int(input("Enter a number: "))
if num >1:
    for i in range(2,num):
        if num % i ==0:
            print(f"{num} is not a prime number")
            break
        else:
            print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")

# 3. Find the factorial of a number.  
num = int(input("Enter a number: "))
fact = 1
for i in range(1, num+1):
    fact *= i
print(f"Factorial of {num} is {fact}")

# 4. Generate Fibonacci numbers.  
num = int(input("Enter the number of terms: "))
a = 0
b = 1
for i in range(num):
    c = a + b
    a = b
    b = c
    print(c, end=" ")

# 5. Check whether a number is an Armstrong number.
num = 153
temp = num
power = len(str(num))
sum = 0
for i in num:
    sum += int(i) ** power
if sum == int(temp):
    print(f"{num} is a amstrong number")
else:
    print(f"not armstrong")

# 6. Check whether a number is a palindrome.
num = int(input("Enter a number: "))
temp = num
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10
if temp == reverse:
    print(f"{temp} is a palindrome number")
else:
    print(f"{temp} is not a palindrome number")

# 7. Find the second largest element.
numbers = [10, 20, 40, 30, 50]
second_largest = sorted(numbers)[-2]
print("Second Largest:", second_largest)

# 8. Find the first non-repeated character. 
char = input("Enter a string: ")
for ch in char:
    if char.count(ch)==1:
        print(f"First non-repeated character: {ch}")
        break
    else:
        print("No non-repeated character found.")

# 9. Find whether a string contains at least one vowel
char = input("Enter a string: ")
vowels = "aeiouAEIOU"
for ch in char:
    if ch in vowels:
        print(f"{char} contains at least one vowel")
        break
    else:
        print(f"{char} doesnt contain ") 
# 10. Separate alphabets, digits, and special characters. 
alpha = input("Enter a string: ")
alphabets = ""
digits = ""
special_chars = ""
for ch in alpha:
    if ch.isalpha():
        alphabets += ch
    elif ch.isdigit():
        digits += ch
    else:
        special_chars += ch
print(f"Alphabets: {alphabets}")
print(f"Digits: {digits}")
print(f"Special Characters: {special_chars}")

# 11. Reverse a number.  
num = int(input("Enter a number: "))
reverse = 0
while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10
print(f"Reversed number: {reverse}")

# 12. Count the digits in a number.  
num = int(input("Enter a number: "))
count = 0
while num > 0:
    num //= 10
    count += 1
print(f"Number of digits: {count}")

# 13. Find the sum of digits. 
num = int(input("Enter a number: "))
sum_digits = 0
while num > 0:
    digit = num % 10
    sum_digits += digit
    num //= 10
print(f"Sum of digits: {sum_digits}")

# 14. Swap two numbers without using a third variable.  
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
a,b = b,a
print(f"After swapping: a = {a}, b = {b}")

# 15. Generate multiplication tables. 
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")

# 16. Explain lambda functions with examples. 
Lambda Functions: A lambda function is an anonymous function used to write short, single-expression functions.

# 17. Explain Python's random module. 
The random module in Python provides functions to generate random numbers and perform random operations.

# 18. Difference between == and is
== compares values, while is checks whether two variables refer to the same object.  

# 19. Mutable vs immutable objects  
Mutable objects can be modified after creation, whereas immutable objects cannot.

# 20. List vs tuple  
A list is mutable, while a tuple is immutable.

# 21. Dictionary vs set 
 A dictionary is a collection of key-value pairs, while a set is an unordered collection of unique elements. 

# 22. Deep copy vs shallow copy


##########################################
# Test date : 25-07-2026
# name : santhosh
# batch : D5b

# 1. find the largest of three numbers by function
def largest_number(a, b, c):
    return max(a, b, c)

largest = largest_number(10, 25, 15)
print(f"The largest number is: {largest}")

# 2. function to count vowels in a string
def count_vowels(s):
    vowels = "aeiousAEIUOS"
    count = 0
    for ch in s:
        if ch in vowels:
            count += 1
    return count

input = "python programming"
vowel_count = count_vowels(input)
print(f"Number of vowels in '{input}': {vowel_count}")

# class is student, class contain name, roll,
class Student:
    def __init__(self, student_name, student_roll):
        self.student_name = student_name
        self.student_roll = student_roll

    def display(self):
        print(f"Student Name: {self.student_name}")
        print(f"Student Roll: {self.student_roll}")

s = Student("rahul", 101)
s.display()

# class is bankaccount, contain account holder name, account number, balance, two methods deposit and diaplay balance
class BankAccount:
    bank_name = "SBI"
    def __init__(self, account_name, account_number, balance):
        self.account_name = account_name
        self.account_number = account_number
        self.balance = balance

    def display_balance(self):
        print(f"Bank Name: {self.bank_name}")
        print(f"Account Holder: {self.account_name}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: {self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: {amount}. New Balance: {self.balance}")

account = BankAccount("santhosh", 9581927787, 1000)
account.deposit(500)
account.display_balance()

# pattern programs right angle triangle
n =5
for row in range(1, n+1):
    for star in range(row):
        print("*", end=" ")
    print()

# inveerted right angle triangle
n = 5
for row in range(n, 0, -1):
    for star in range(row):
        print("*", end=" ")
    print()

# hallow square pattern
n = 5
for row in range(n):
    for col in range(n):
        if row == 0 or row == n-1 or col == 0 or col == n-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


# count the frequency of each character in a string
string = "programming"
freq = {}
for char in string:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1
print(f"Frequency of each character: {freq}")

# remove duplicates from a string
string = "programming"
result = ""
for char in string:
    if char not in result:
        result += char
print(f"String after removing duplicates: {result}")

# find the longest word in sentence
sentence = "Python is a programming language"
words = sentence.split()
longest_word = max(words, key=len)
print(f"The longest word is: {longest_word}")

# find the second largest number 
numbers = [10, 45, 20, 80, 60]
second_largest = sorted(numbers)[-2]
print(f"The second largest number is: {second_largest}")

# STRONG number
num = int(input("Enter a number: "))
temp = num
sum = 0
while num > 0:
    digit = num % 10   
    fact = 1   
    for i in range(1, digit + 1):  
        fact *= i 
    sum += fact  
    num //= 10  
if sum == temp:
    print(f"{temp} is a strong number")
else:
    print(f"{temp} is not a strong number")