##############################################################################
#1. compound interest calculator
#2. simple interest calculator
#3. print a to z
##############################################################################

# importing moudel
import Topics.calculator as calculator

# compound interest calculator
def compound_interest(principal, rate, time, n):
    rate = rate/100
    amount = principal * (1 + rate/n)**(n*time)
    interest = amount - principal
    return interest, amount

p = float(input("Enter the principal amount: "))
r = float(input("Enter the annual interest rate (in %): "))
t = float(input("Enter the time (in years): "))
n = int(input("Enter the number of times interest is compounded per year: "))

total, final_amount = compound_interest(p, r, t, n)
print(f"Total interest earned: {total:.2f}")
print(f"Final amount after {t} years: {final_amount:.2f}")

#METHOD 2
def compound_interest_method2(principal, rate, time, n):
    rate = rate/100
    amount = principal
    for i in range(int(n * time)):
        amount += amount * (rate / n)
    interest = amount - principal
    return interest, amount

p = float(input("Enter the principal amount: "))
r = float(input("Enter the annual interest rate (in %): "))
t = float(input("Enter the time (in years): "))
n = int(input("Enter the number of times interest is compounded per year: "))

total, final_amount = compound_interest_method2(p, r, t, n)
print(f"Total interest earned (Method 2): {total:.2f}")
print(f"Final amount after {t} years (Method 2): {final_amount:.2f}")

# method 3 using recursion
def compound_interest_recursion(principal, rate, time, n, current_time=0):
    # use integer number of compounding steps
    steps = int(time * n)
    def recurse(current_amount, step):
        if step >= steps:
            return current_amount, current_amount - principal
        current_amount += current_amount * (rate / 100) / n
        return recurse(current_amount, step + 1)
    return recurse(principal, 0)

p = float(input("Enter the principal amount: "))
r = float(input("Enter the annual interest rate (in %): "))
t = float(input("Enter the time (in years): "))
n = int(input("Enter the number of times interest is compounded per year: "))
final_amount, interest = compound_interest_recursion(p, r, t, n)
print(f"Total interest earned (Method 3): {interest:.2f}")

# method4 buitin function
def compound_interest_builtin(principal, rate, time, n):
    from math import pow
    rate = rate/100
    amount = principal * pow((1 + rate/n), (n*time))
    interest = amount - principal
    return interest, amount

p = float(input("Enter the principal amount: "))
r = float(input("Enter the annual interest rate (in %): "))
t = float(input("Enter the time (in years): "))
n = int(input("Enter the number of times interest is compounded per year: "))

total, final_amount = compound_interest_builtin(p, r, t, n)
print(f"Total interest earned (Method 4): {total:.2f}")
print(f"Final amount after {t} years (Method 4): {final_amount:.2f}")

##################################################################################################

# simple interest calculator
# formula: SI = (P * R * T) / 100
def simple_interest(principal, rate, time):
    interest = (principal * rate * time)/100
    return interest
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (in %): "))
time = float(input("Enter the time (in years): "))
interest = simple_interest(principal, rate, time)
print(f"Total simple interest earned: {interest:.2f}")

# method 2
def simple_interset_method2(principal, rate, time):
    interest = (principal * rate * time)/100
    return interest
print(simple_interset_method2(1000, 5, 2))
print(simple_interset_method2(1500, 4.5, 3))

# method3
data = [(1000, 5, 2), (1500, 4.5, 3), (2000, 6, 1)]
si_list = [(p * r * t)/100 for p , r, t in data]
print(si_list)

#method4 lambda function
simple_interest_lambda = lambda p, r, t,: (p * r * t)/100
print(simple_interest_lambda(1000, 5, 2))

##############################################################################
# print a to z
print("alphabet A-z", end=" ")
for i in range(65, 91):
    print(chr(i), end=" ")

print("alphabet a-z", end=" ")
for i in range(97, 123):
    print(chr(i), end=" ")

###################################################
# remove characters from a string
text = "Hello, World!"
new_text = text.replace("o", "")
print(new_text)  


