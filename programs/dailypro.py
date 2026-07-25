# hello world
from sqlalchemy import false


print("hello world")

# wapp to take input from user and print it
user = input("Enter something: ")
print("You entered:", user)

# wapp to take two numbers from user and print their sum
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
sum = num1 + num2
print("The sum of", num1, "and", num2, "is:", sum)

# wapp to swap two numbers without using a third variable
a = 10
b =20
print("Before swapping: a =", a, "b =", b)
a = a + b
b = a - b
a = a - b
print("After swapping: a =", a, "b =", b)

# method 2
a = 10
b = 20
a,b = b,a
print("After swapping: a =", a, "b =", b)

# method 3
a = 10
b = 20
temp = a
a = b
b = temp
print("After swapping: a =", a, "b =", b)

# wapp to check if a number is even or odd
num = int(input("Enter a number: "))
if num % 2 ==0:
    print(num, "is even")
else:
    print(num, "is odd")

# wapp to check if a number is positive, negative or zero
num = float(input("Enter a number: "))
if num > 0:
    print(num, "is positive")
elif num < 0:
    print(num, "is negative")
else:
    print(num, "is zero")

#  wapp to finf the largest of three numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a>b and a>c:
    print(a, "is the largest number")
elif b>c and b>a:
    print(b, "is the largest number")
else:
    print(c, "is the largest number")

# wapp to find the factorial of a number
num = int(input("Enter a number: "))
fact = 1
for i in range(1,num+1):
    fact *= i
print("The factorial of", num, "is:", fact)

# wapp to find the fibonacci series up to n terms
# fibonacci serices means the sum of previous two numbers
# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...
n = int(input("enter the number of terms:"))
a = 0
b = 1
for i in range(n):
    print(a, end=" ")
    c =a + b
    a = b
    b = c

# wapp to reverse a number
num = int(input("Enter a number: "))
rev = 0
while num > 0:
    digit = num % 10 # % is modulus operator which gives the remainder of the division 
    rev = rev * 10 + digit # rev = 0 * 10 + 5 = 5
    num //= 10 # /  / is floor division operator which gives the quotient of the division
print("The reverse of the number is:", rev)

# wapp to check if a number is prime or not
num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not a prime number")
            break
        else:
            print(num, "is a prime number")
            break
else:
    print(num, "is not a prime number")

# method2
n = int(input("Enter a number: "))
count = 0
for i in range(1, n +1):
    if n % i == 0:
        count += 1
if count == 2:
    print(n, "is a prime number")
else:
    print(n, "is not a prime number")

# wapp to find the sum of digits of a number
num = int(input("Enter a number: "))
sum = 0
while num > 0:
    digit = num % 10
    sum += digit
    num //= 10
print("The sum of digits is:", sum)

# wpp a to find the reverse of a string
str1 = input("Enter a string: ")
print(" the reverse of the string is:", str1[::-1])

# wapp to check if a string is palindrome or not
str1 = input("Enter a string: ")
if str1 == str1[::-1]:
    print(str1, "is a palindrome")
else:
    print(str1, "is not a palindrome")

# metod2
str = input("Enter a string to check if it's a palindrome: ")
rev = str[::-1]
if str == rev:
    print(f"{str} is a palindrome")
else:
    print(f"{str} is not a palindrome")

# wapp to check if two strings are anagrams or not
str1 = input("Enter a string: ")
str2 = input("Enter a string: ")
dict1 = {}
dict2 = {}
for i in str1:
    dict1[i] = dict1.get(i, 0)+1 # get() method returns the value of the key if it is in the dictionary, else it returns the default value which is 0 in this case
for i in str2:
    dict2[i] = dict2.get(i, 0)+1
if dict1 == dict2:
    print(str1, "and", str2, "are anagrams")
else:
    print(str1, "and", str2, "are not anagrams")

# method 2
str1 = input("Enter a string: ")
str2 = input("Enter a string: ")
if sorted(str1) == sorted(str2): # sorted() function is used to sort the characters of the string in ascending order
    print(str1, "and", str2, "are anagrams")
else:
    print(str1, "and", str2, "are not anagrams")


# wpp to count vowels and consonants in a string
str = input("Enter a string: ")
v = 0
c = 0
for i in str:
    if i.isalpha():
        if i in "aeiouAEIOU":
            v += 1
        else:
            c += 1
print("The number of vowels is:", v)
print("The number of consonants is:", c)

# wapp to find the length of a string without using len() function
str = input("Enter a string: ")
count = 0
for i in str:
    count += 1
print("The length of the string is:", count)

# wapp to remove all spaces from a string
str = input("Enter a string: ")
print(str.repace(" ", ""))

# wpp to count occurrences of a character in a string
str = input("Enter a string: ")
char = input("Enter a character: ")
count = 0
for i in str:
    if i == char:
        count += 1
print("The character", char, "occurs", count, "times in the string")

# method 2
str = input("Enter a string: ")
char = input("Enter a character: ")
count = str.count(char) # count() method returns the number of occurrences of a substring in the string
print("The character", char, "occurs", count, "times in the string")

# wpp to replace vowels with *
str = input("Enter a string: ")
for i in str:
    if i in "aeiouAEIOU":
        str = str.replace(i, "*")
print("The string after replacing vowels with * is:", str)

# wpp to check the anagram of a string
str1 = input("Enter a string: ")
str2 = input("Enter a string: ")
if sorted(str1) == sorted(str2):
    print(str1, "and", str2, "are anagrams")
else:
    print(str1, "and", str2, "are not anagrams")

# method 2
str1 = input("Enter a string: ")
str2 = input("Enter a string: ")
dict1 = {}
dict2 = {}
for i in str1:
    dict1[1] = dict1.get(i,0)+1
for i in str2:
    dict2[i] = dict2.get(i,0)+1
if dict1 == dict2:
    print(str1, "and", str2, "are anagrams")
else:
    print(str1, "and", str2, "are not anagrams")

# wpp to find the first non repected character in a string
str = input("Enter a string: ")
for i in str:
    if str.count(i) == 1:
        print("The first non repeated character is:", i)
        break

# armstrong number
#armstrong number is a number that is equal to the sum of its own digits raised to the power of the number of digits. For example, 153 is an armstrong number because 1^3 + 5^3 + 3^3 = 153.
n = int(input("Enter a number: "))
sum = 0
temp = n
while temp > 0:
    digit = temp % 10
    sum += digit ** 3
    temp //= 10
if n == sum:
    print(n, "is an armstrong number")
else:
    print(n, "is not an armstrong number")

# prime number
num = int(input("Enter a number: "))
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, "is not a prime number")
            break
        else:
            print(num, "is a prime number")
            break
else:
    print(num, "is not a prime number")


# perfect number
# perfect number is a positive integer that is equal to the sum of its proper positive divisors
# eg: 6 is a perfect number because its proper positive divisors are 1, 2 and 3 and 1 + 2 + 3 = 6
num = int(input("Enter a number: "))
s = 0
for i in range(1, num):
    if num % i == 0:
        s += i
if s == num:
    print(num, "is a perfect number")
else:
    print(num, "is not a perfect number")

# wpp to check if a string is palindrome or not
str1 = input("Enter a string: ")
rev = str[::-1]
if str1 == rev:
    print(str1, "is a palindrome")
else:
    print(str1, "is not a palindrome")

#wpp calculate the power of a number without using **
a = int(input("Enter the base number: "))
b = int(input("Enter the exponent: "))
res = 1
for i in range(b):
    res *= a
print("The result of", a, "raised to the power of", b, "is:", res)

# wpp to multiplcation of two numbers 
n = int(input("Enter first number: "))
for i in range(1, 11):
    print(n, "x", i, "=", n*i)

# wpp to even or odd
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(num, "is even")
else:
    print(num, "is odd")

# wpp to calculate the sum of first n natural numbers
n = int(input("Enter a number: "))
sum = 0
for i in range(1, n+1):
    sum += i
print("The sum of first", n, "natural numbers is:", sum)

# wpp to python to print divide by 3 and 5
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(i,end=" ")

# epp to define a function that return the square of a number
def square(num):
    return num ** 2
print(square(int(input("Enter a number: "))))

# wpp to define a function that return the cube of a number
def cube(num):
    return num ** 3
print(cube(int(input("Enter a number: "))))

# wpp to define a function that check if anumber is prime

def is_prime(num):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
n = int(input("Enter a number: "))
print(n, "is prime") if is_prime(n) else print(n, "is not prime")



# wpp to define a function that check rhat calculate factorial using recursion
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)
print(factorial(int(input("enter a number:"))))

# wpp to define a function that find the maximum of three numbers
def maximum(a, b, c):
    if a > b and a > c:
        return a
    elif b > c and b > a:
        return b
    else:
        return c
print(maximum(int(input("Enter first number: ")), int(input("Enter second number: ")), int(input("Enter third number: "))))

# method 2
def maximum(a, b, c):
    return max(a, b, c)
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
print("The maximum of", a, b, c, "is:", maximum(a, b, c))

# wpp to define a function that return the reverse of string
def reverse_string(str):
    return str[::-1]
print(reverse_string(input("Enter a string: ")))

# wpp to define a function that count vowels and consonants in a 
def vowel_consonant_count(str):
    v = 0
    c = 0
    for i in str:
        if i.isaplha():
            if i in "aeiousAEIOU":
                v += 1
            else:
                c += 1
    return v, c
str = input("Enter a string: ")
v, c = vowel_consonant_count(str)
print("The number of vowels is:", v)
print("The number of consonants is:", c)

#wpp to define a functional that generate fibonacci serices up to n
def fibonacci(n):
    a = 0
    b = 0
    for i in range(n):
        print(a, end = " ")
        c = a+b
        a = b
        b = c
print(fibonacci(int(input("Enter the number of terms: "))))

# wpp to define a function that calculatr power of number using recursion
def power(a, b):
    if b == 0:
        return 1
    else:
        return a * power(a, b - 1)
a = int(input("Enter the base number: "))
b = int(input("Enter the exponent: "))
print("The result of", a, "raised to the power of", b, "is:", power(a, b))

# wpp to calculate factorial using recursion
def factorial(num):
    if num == 0:
        return 1
    else:
        return num * factorial(num - 1)
print(factorial(int(input("Enter a number: "))))

# wpp to print number from n to 1 using recursion
def print_n_to_1(n):
    if n == 0:
        return
    else:
        print(n, end = " ")
        print_n_to_1(n - 1)
print_n_to_1(int(input("Enter a number: ")))


# lambda function to calculate the square of a number
square = lambda x: x ** 2
print(square(int(input("Enter a number: "))))

# wpp to find the maximum element in a tuple
t = tuple(map(int, input("Enter elements of tuple separated by space: ").split()))
print("The maximum element in the tuple is:", max(t))

# wpp to convert a list into a tuple
l = list(map(int, input("Enter elements of list separated by space: ").split()))
t = tuple(l)
print("The tuple is:", t)

# wpp to find the union of two sets
s1 = set(map(int,input("Enter elements of first set separated by space: ").split()))
s2 = set(map(int,input("Enter elements of second set separated by space: ").split()))
print("The union of the two sets is:", s1 | s2)

# wpp to find the intersection of two sets
s1 = set(map(int,input("Enter elements of first set separated by space: ").split()))
s2 = set(map(int,input("Enter elements of second set separated by space: ").split()))
print("The intersection of the two sets is:", s1 & s2)

# wpp to find the check if a set is subset of another set
s1 = set(map(int, input("enter elements of first set :").split()))
s2 = set(map(int, input("enter elements of second set :").split()))
if s1.issubset(s2):
    print("s1 is a subset of s2")
else:
    print("s1 is not a subset of s2")

# wpp to remove duplicate from a list using set
l = list(map(int, input("enter element of list:").split()))
print(list(set(l)))

# wpp to count unique elements in a list using set
l = list(map(int, input("enter elements of list:").split()))
print(len(set(l)))

# wpp a to access values from a dictionary
d = {'a': 1, 'b': 2, 'c': 3}
print("The value of key 'a' is:", d['a'])

# wpp to python program to update value in a dictionary
d = {'a': 1, 'b': 2, 'c': 3}
key = input("Enter the key to update: ")
value = int(input("Enter the new value: "))
if key in d:
    d[key] = value
    print("The updated dictionary is:", d)
elif key not in d:
    print("Key not found in the dictionary")
else:
    print("Invalid input")

# simple method
d = {'a': 1, 'b': 2, 'c': 3}
d[a] = 4
print("The updated dictionary is:", d)

# wpp to remove a key from a dictionary
d = {'a': 1, 'b': 2, 'c': 3}
key = input("Enter the key to remove: ")
if key in d:
    del d[key]
    print("The updated dictionary is:", d)
elif key not in d:
    print("Key not found in the dictionary")
else:
    print("Invalid input")

d = {'a': 1, 'b': 2, 'c': 3}
d.pop('a')
print("The updated dictionary is:", d)

d = {'a': 1, 'b': 2, 'c': 3}
del d['a']
print("The updated dictionary is:", d)

# wpp to python program to merge two dictionaries
d1 = {'a': 1, 'b': 2}
d2 = {'c': 3, 'd': 4}
d1.update(d2)
print("The merged dictionary is:", d1)

# wpp to count the frequency of characters in a string using a dictionary
s = input("Enter a string: ")
freq = {}
for char in s:
    freq[char]=freq.get(char, 0)+1 # expalin this line of code
# This line of code is used to count the frequency of each character in the string.
print("The frequency of characters in the string is:", freq)

# wpp to count the frequency of words in a string using a dictionary
s = input("enter a string:").split()
freq = {} # why we use {} here
# We use {} here to create an empty dictionary. A dictionary is a collection of key-value pairs. In this case, we will use the words in the string as keys and their frequencies as values.
for word in s:
    freq[word] = freq.get(word,0)+1
print("The frequency of words in the string is:", freq)

# wpp to find the sum of values in a dictionary
d = {'a': 1, 'b': 2, 'c': 3}
print("The sum of values in the dictionary is:", sum(d.values()))

# wpp to find the maximum value in a dictionary
d = {'a': 1, 'b': 2, 'c': 3}
print("The maximum value in the dictionary is:", max(d.values()))

# or
d = {'a': 1, 'b': 2, 'c': 3}
max_key = max(d, key=d.get)
print("The maximum value in the dictionary is:", d[max_key])

# wpp a to sort a dictonary by value
d = {'a': 3, 'b': 1, 'c': 2}
print(dict(sorted(d.items(), key=lambda x: x[1])))

# wpp to check if a key exists in a dictionary
d = {'a': 1, 'b': 2, 'c': 3}
key = input("Enter a key to check: ")
if key in d:
    print("The key", key, "exists in the dictionary")
else:
    print("The key", key, "does not exist in the dictionary")

# WPP to find the length of a dictionary
d = {'a': 1, 'b': 2, 'c': 3}
print("The length of the dictionary is:", len(d))

# Wpp to iterate over a list using for loop
l = [1, 2, 3, 4, 5]
for i in l:
    print(i, end=" ")

l = list(map(int, input("enter any list:").split()))
for i in l:
    print(i, end=" ")

# while loop
l = list(map(int,input("enter any list:").split()))
i = 0
while i < lem(l):
    print(l[i], end=" ")
    i += 1

# wpp to find the largest word in a sentence
sentence = input("Enter a sentence: ")
word = sentence.split()
largest_word = max(word, key=len)
print("The largest word in the sentence is:", largest_word)
print("The length of the largest word is:", len(largest_word))

# wpp to find the smallest word in a sentence
sentence = input("Enter a sentence: ")
words = sentence.split()
smallest_word = min(words, key=len)
print("The smallest word in the sentence is:", smallest_word)
print("The length of the smallest word is:", len(smallest_word))

# method2
sentence = input("Enter a sentence: ")
words = sentence.split()
smallest_word = words[0]
for word in words:
    if len(word) < len(smallest_word):
        smallest_word = word
print("The smallest word in the sentence is:", smallest_word)
print("The length of the smallest word is:", len(smallest_word))

# simple interest
p = float(input("Enter the principal amount: "))
r = float(input("Enter the rate of interest: "))
t = float(input("Enter the time in years: "))
si = (p * r * t) / 100
print("The simple interest is:", si)

# compound interest
p = float(input("Enter the principal amount: "))
r = float(input("Enter the rate of interest: "))
t = float(input("Enter the time in years: "))
ci = p * (1 = r/100) ** t - p
print("The compound interest is:", ci)
 
# wpp to check if a character is uppercase or lowercase
char = input("Enter a character: ")
if char.isupper():
    print(char, "is uppercase")
else:
    print(char, "is lowercase")
    
# wpp to count the number of uppercase and lowercase characters in a string
str = input("Enter a string: ")
upper = 0
lower = 0
for i in str:
    if str.isupper():
        upper += 1
    elif str.islower():
        lower += 1
print("The number of uppercase characters is:", upper)
print("The number of lowercase characters is:", lower)

# wpp to reverse a distionary
d = {'a': 1, 'b': 2, 'c': 3}
rev = {v:k for k,v in d.items()} # explain these lines of code
# This line of code creates a new dictionary called 'rev' by reversing the key-value pairs in the original dictionary 'd'. The 'items()' method returns a view object that displays a list of a dictionary's key-value tuple pairs. The dictionary comprehension iterates over these pairs, swapping the keys and values to create the new reversed dictionary.
print("The reversed dictionary is:", rev)

