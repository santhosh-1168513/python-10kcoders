# TO FIND THE GIVEN NUMBER IS EVEN OR ODD NUMBER
num = int(input("enter the number:"))
if num % 2 == 0:
    print(f"{num} is an even number")
else:
    print(f"{num} is an odd number")

#variable  number is largest amoung three variable
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a > b and a > c:
    print(f"{a} is the largest number")
elif b > a and b > c:
    print(f"{b} is the largest number")
else:
    print(f"{c} is the largest number")

#find the factorial of a number
num = int(input("enter the number:"))
for i in range(1, num+1):
    fact = 1
    fact = fact * i # or fact *= i
    print(f"factorial of {i} is {fact}")
print(f"factorial of {num} is {fact}")

#finacci serice
n = int(input("Enter the number of terms: "))
a = 0
b = 1
for i in range(n):
    c = a + b
    a = b
    b = c
    print(c, end=" ")   

# method 2
prev = 0
cur = 1
for i in range(n):
    print(prev, end=" ")
    prev, cur = cur, prev + cur

# which number is prime or not
num = int(input("Enter a number to check the prime no aren't: "))
if num > 1:
    for i in range(2, num-1):
        if num % i == 0:
            print(f"{num} is not a prime number")
            break
        else:
            print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")

# sum of digits in a number
num = 123
total = 0
while num > 0:
    digit = num % 10 # % it extracts the last digit of a number
    total += digit
    num //= 10 # /it removes the last digit of a number
print(f"Sum of digits: {total}")

#to find rhe perfect number or not(A perfect number is a number that is equal to the sum of its proper divisors (excluding the number itself). eg 6, 28, 496, 8128)
num = int(input("enter the number: "))
sum = 0
for i in range(1, num):
    if num % i == 0:
        sum = sum + i
if sum == num:
    print(f"{num} is a perfect number")
else:
    print(f"{num} is not a perfect number")

#to find the palindrome number or not (A palindrome number remains the same when reversed.)
num = int(input("enter the number: "))
temp = num
reverse = 0
while num > 0:
    digit = num % 10  # to get the last digit
    reverse = reverse * 10 + digit  # to reverse the number
    num //= 10  # to remove the last digit
if temp == reverse:
    print(f"{temp} is a palindrome number")
else:
    print(f"{temp} is not a palindrome number")

# % it extracts the last digit of a number  
# / / it removes the last digit of a number

#to find the strong number or not
#A strong number is a number whose sum of the factorials of its digits equals the number itself.

num = int(input("Enter a number: "))
temp = num
sum = 0
while num > 0:
    digit = num % 10   # to get the last digit
    fact = 1   # to calculate the factorial of the digit
    for i in range(1, digit + 1):  # to calculate the factorial of the digit
        fact *= i 
    sum += fact  # to add the factorial of the digit to the sum
    num //= 10  # to remove the last digit
if sum == temp:
    print(f"{temp} is a strong number")
else:
    print(f"{temp} is not a strong number")

s = input("Enter a string: ")

reverse = ""

for ch in s:
    reverse = ch + reverse

print(reverse)

# to find the amstrong number or not
# num = input("enter the number")
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


num = 153
temp = num
total = 0
s = len(str(num))

while temp > 0:
    digit = temp%10
    total += digit**s
    temp = temp//10
if temp == num:
    print("number is amstrong")
else:
    print("not amstrong number")
