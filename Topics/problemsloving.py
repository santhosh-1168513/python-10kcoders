#---------------------------------------------TASK 1-------------------------------------------------------------

# 1. Take a number and check whether it is **positive**.
n = int(input("Enter a number: "))
if n>0:
    print("The number is positive.")

# 2. Take a number and check whether it is **negative**.
n = int(input("Enter a number: "))
if n<0:
    print("The number is negative.")

# 3. Take a number and check whether it is **zero**.
n = int(input("Enter a number: "))
if n ==0:
    print("The number is zero.")

# 4. Take a number and check whether it is **positive, negative, or zero**.
n = int(input("Enter a number: "))
if n>0:
    print("The number is positive.")
elif n<0:   
    print("The number is negative.")
else:
    print("The number is zero.")

# 5. Take a number and check whether it is **even or odd**.
n = int(input("Enter a number: "))
if n%2==0:
    print("The number is even.")
else:
    print("The number is odd.")

# 6. Take two numbers and print the **greater number**.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a>b:
    print(f"The greater number is: {a}")
else:
    print(f"The greater number is: {b}")

# 7. Take two numbers and print the **smaller number**.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a<b:
    print(f"The smaller number is: {a}")
else:
    print(f"The smaller number is: {b}")

# 8. Take two numbers and check whether they are **equal or not**.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a==b:
    print("The numbers are equal.")
else:
    print("The numbers are not equal.")
# 9. Take three numbers and print the **largest number**.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a>b and a>c:
    print(f"The largest number is: {a}")
elif b>a and b>c:
    print(f"The largest number is: {b}")
else:
    print(f"The largest number is: {c}")

# 10. Take three numbers and print the **smallest number**.
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if a<b and a<c:
    print(f"The smallest number is: {a}")
elif b<a and b<c:
    print(f"The smallest number is: {b}")
else:
    print(f"The smallest number is: {c}")

# 11. Check whether a number is **divisible by 5**.
n = int(input("Enter a number: "))
if n%5==0:
    print("The number is divisible by 5.")
else:
    print("The number is not divisible by 5.")
# 12. Check whether a number is **divisible by 10**.
n = int(input("Enter a number: "))
if n%10==0:
    print("The number is divisible by 10.")
else:
    print("The number is not divisible by 10.")

# 13. Check whether a number is **divisible by both 3 and 5**.
n = int(input("Enter a number: "))
if n%3==0 and n%5==0:
    print("The number is divisible by both 3 and 5.")
else:
    print("The number is not divisible by both 3 and 5.")

# 14. Check whether a number is **divisible by either 3 or 5**.
n = int(input("Enter a number: "))
if n%3==0 or n%5==0:
    print("The number is divisible by either 3 or 5.")
else:
    print("The number is not divisible by either 3 or 5.")

# 15. Check whether a number is **not divisible by 7**.
n = int(input("Enter a number: "))
if n%7!=0:
    print("The number is not divisible by 7.")
else:
    print("The number is divisible by 7.")

# 16. Check whether a number lies between **10 and 50**.
n = int(input("Enter a number: "))
if 10<n<50:
    print("The number lies between 10 and 50.")
else:
    print("The number does not lie between 10 and 50.")

# 17. Check whether a number is **outside the range 10 to 50**.
n = int(input("Enter a number: "))
if n<=10 and n>=50:
    print("The number is outside the range 10 to 50.")
else:
    print("The number is within the range 10 to 50.")

# 18. Check whether a number is a **two-digit number**.
n = int(input("Enter a number: "))
if 10<n<99:
    print("The number is a two-digit number.")

# 19. Check whether a number is a **three-digit number**.
n = int(input("Enter a number: "))
if 100<n<999:
    print("The number is a three-digit number.")

# 20. Check whether a number is greater than **100 and even**.
n = int(input("Enter a number: "))
if n>100 and n%2==0:
    print("The number is greater than 100 and even.")
else:
    print("The number is not greater than 100 and even.")

# 21. Take marks and print **Pass** if marks are 40 or above, otherwise **Fail**.
marks = int(input("Enter marks: "))
if marks>=40:
    print("Pass")
else:   
    print("Fail")

# 22. Take marks and print grade **A** if marks are 90 or above, **B** if 75–89, **C** if 60–74, otherwise **D**.
marks = int(input("Enter marks: "))
if marks>=90:
    print("Grade A")
elif: marks>=75 and marks<=89:
    print("Grade B")
elif: marks>=60 and marks<=74:
    print("Grade C")
else:
    print("Grade D")

# 23. Take marks and check whether they are **valid marks** between 0 and 100.
marks = int(input("Enter marks: "))
if marks>=0 and marks<=100:
    print("Valid marks")
else:
    print("Invalid marks")

# 24. Take age and check whether a person is **eligible to vote**.
n = int(input("Enter age: "))
if n>=18:
    print("Eligible to vote")
else:
    print("Not eligible to vote")

# 25. Take age and check whether a person is a **minor or adult**.
n = int(input("Enter age: "))
if n<18:
    print("Minor")
else:
    print("Adult")

# 26. Take age and check whether a person is **between 18 and 60**.
n = int(input("Enter age: "))
if n>=18 and n<=60:
    print("Between 18 and 60")
else:
    print("Not between 18 and 60")

# 27. Take salary and check whether it is **greater than 50,000**.
salary = int(input("Enter salary: "))
if salary>50000:
    print("Salary is greater than 50,000")
else:
    print("Salary is not greater than 50,000")

# 28. Take salary and calculate a **10% bonus only if salary is greater than 50,000**.
salary = int(input("Enter salary: "))
if salary >= 50000:
    bouns = salary * 0.1
    print(f"Bonus is: {bouns}")

# 29. Take purchase amount and give a **discount if amount is greater than 1,000**
sale_amount = int(input("Enter purchase amount: "))
if sale_amount>1000:
    discount = sale_amount * 0.1
    print(f"Discount is: {discount}")

# 30. Take a number and check whether it is **even and greater than 50**.
n = int(input("Enter a number: "))
if n%2==0 and n>50:
    print("The number is even and greater than 50.")
else:
    print("The number is not even and greater than 50.")

# 31. Take two numbers and check whether **both are positive**.
n = int(input("Enter first number: "))
m = int(input("Enter second number: "))
if n>0 and m>0:
    print("Both numbers are positive.")
else: 
    print("Both numbers are not positive.")

# 32. Take two numbers and check whether **at least one is positive**.
n = int(input("Enter first number: "))
m = int(input("Enter second number: "))
if n>0 or m>0:
    print("At least one number is positive.")
else:
    print("Neither number is positive.")

# 33. Take two numbers and check whether **both are even**.
n = int(input("Enter first number: "))
m = int(input("Enter second number: "))
if n%2==0 and m%2==0:
    print("Both numbers are even.")

# 34. Take two numbers and check whether **one or both are divisible by 5**.
n = int(input("Enter first number: "))
m = int(input("Enter second number: "))
if n%5==0 or m%5==0:
    print("One or both numbers are divisible by 5.")

# 35. Take three numbers and check whether **all three are equal**.
n = int(input("Enter first number: "))
m = int(input("Enter second number: "))
o = int(input("Enter third number: "))
if n==m and m==o:
    print("All three numbers are equal.")

# 36. Take three numbers and check whether **at least two numbers are equal**.
n = int(input("Enter first number: "))
m = int(input("Enter second number: "))
o = int(input("Enter third number: "))
if n==m or m==o or n==o:
    print("At least two numbers are equal.")

# 37. Take three numbers and check whether all three numbers are **different**.
n = int(input("Enter first number: "))
m = int(input("Enter second number: "))
o = int(input("Enter third number: "))
if n!=m and m!=o and n!=o:
    print("All three numbers are different.")


# 38. Take three numbers and print the **middle value**.
n = int(input("Enter first number: "))
m = int(input("Enter second number: "))
o = int(input("Enter third number: "))
if (n>m and n<o) or (n>o and n<m):
    print(f"The middle value is: {n}")
else:
    print(f"The middle value is: {m}" if (m>n and m<o) or (m>o and m<n) else f"The middle value is: {o}")

# 39. Take three numbers and print the largest **only if all three are positive**.
n = int(input("Enter first number: "))
m = int(input("Enter second number: "))
o = int(input("Enter third number: "))
if n>0 and m>0 and o>0:
    if n>m and n>o:
        print(f"The largest number is: {n}")
    elif m>n and m>o:
        print(f"The largest number is: {m}")
    else:
        print(f"The largest number is: {o}")
else:
    print("All three numbers are not positive.")

# 40. Take three numbers and check whether **exactly two numbers are even**.
n = int(input("Enter first number: "))
m = int(input("Enter second number: ")) 
o = int(input("Enter third number: "))
if (n%2==0 and m%2==0 and o%2!=0) or (n%2==0 and o%2==0 and m%2!=0) or (m%2==0 and o%2==0 and n%2!=0):
    print("Exactly two numbers are even.")


# 41. Take a year and check whether it is a **leap year**.
year = int(input("Enter a year: "))
if year%4==0 or (year%100==0 and year%400==0):
    print(f"{year} is a leap year.")

# 42. Take a number and check whether it is divisible by **2 or 3 but not both**.
n = int(input("Enter a number: "))
if (n%2==0 or n%3==0) and not (n%2==0 and n%3==0):
    print("The number is divisible by 2 or 3 but not both.")

# 43. Take a number and check whether it is divisible by **2, 3, and 5**.
n = int(input("Enter a number: "))
if n%2==0 and n%3==0 and n%5==0:
    print("The number is divisible by 2, 3, and 5.")

# 44. Take a number and check whether it is **between 1 and 100 and divisible by 10**.
n = int(input("Enter a number: "))
if 1<=n<=100 and n%10==0:
    print("The number is between 1 and 100 and divisible by 10.")

# 45. Take a number and check whether it is **positive and odd**.
n = int(input("Enter a number: "))
if n>0 and n%2==1:
    print("The number is positive and odd.")

# 46. Take a number and check whether it is **negative and even**.
if n<0 and n%2==0:
    print("The number is negative and even.")

# 47. Take temperature as a number and print:
# Above 35 → Hot
# 20–35 → Normal
# Below 20 → Cold
temperature = int(input("Enter temperature: "))
if temperature>35:
    print("Hot")
elif 20<=temperature<=35:
    print("Normal")
else:
    print("Cold")

# 48. Take electricity units and calculate the bill:
# Up to 100 units → ₹5/unit
# 101–200 → ₹7/unit
# Above 200 → ₹10/unit
units = int(input("Enter electricity units: "))
if units<=100:
    bill = units * 5
elif 101<=units<=200:
    bill = units * 7
else:
    bill = units * 10

# 49. Take three sides of a triangle and check whether they can form a **valid triangle** using the condition:
#     a + b > c, a + c > b, and b + c > a.

# 50. Take a number and classify it as:

# **Positive Even**
# **Positive Odd**
# **Negative Even**
# **Negative Odd**
# **Zero**