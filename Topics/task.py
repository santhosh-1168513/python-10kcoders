"""*Task 1 – Student Management System*
Scenario
A school wants to maintain student results.
Requirements
Ask the user to enter the student name.
Ask the user to enter marks for 5 subjects using a loop.
Calculate the total marks.
Calculate the average marks.
Display:
Pass if average is 35 or above.
Fail if average is below 35.
Assign grade:
A → Average 90 and above
B → Average 75 to 89
C → Average 60 to 74
D → Average 35 to 59
F → Below 35
Ask the user whether they want to enter another student.
Continue until the user enters "No".
Display:
Total students processed
Total passed students
Total failed students"""


total_students = 0
passed_students = 0
failed_students = 0

while True:
    name = input("Enter student name: ")
    marks_list = []
    for i in range(5):
        marks = int(input(f"enter the {i+1} subject marks: "))
        marks_list.append(marks)
    
    total_marks = sum(marks_list)
    average_marks = total_marks / 5
    print(f"Total Marks: {total_marks}")
    print(f"Average Marks: {average_marks}")    

    if average_marks >= 35:
        print("Pass")
        passed_students += 1
    else:
        print("Fail")
        failed_students += 1

    if average_marks >= 90:
        print("Grade: A")
    elif average_marks >= 75:
        print("Grade: B")
    elif average_marks >= 60:
        print("Grade: C")
    elif average_marks >= 35:
        print("Grade: D")
    else:
        print("Grade: F")
    
    total_students += 1
    another = input("Do you want to enter another student? (Yes/No): ")
    if another.lower() == "no":
        break

print(f"\nTotal students processed: {total_students}")
print(f"Total passed students: {passed_students}")
print(f"Total failed students: {failed_students}")


# Task 2 – ATM PIN Validation System
# Scenario
# An ATM allows only 3 PIN attempts.
# Requirements
# Store the correct PIN as 1234.
# Ask the user to enter the PIN.
# If PIN is correct:
# Display "Login Successful".
# Display account balance.
# If PIN is incorrect:
# Display "Wrong PIN".
# Allow only 3 attempts using a loop.
# If all 3 attempts fail:
# Display "Account Blocked".
# Count and display total attempts used.'''

correct_pin = "1234"
attempts = 0

while attempts < 3:
    enter_pin = input("Enter your PIN: ")
    if enter_pin == correct_pin:
        print("Login Successful")
        print("Account Balance: $1000")
        attempts += 1
        break
    else:
        print("Wrong PIN")
        attempts += 1

if attempts == 3:
    print("Account Blocked")

print(f"Total attempts used: {attempts}")

# Task 1: Number Pyramid
# Problem: Write a program to print a pyramid of numbers up to n.
n = int(input("Enter the number of rows for the pyramid: "))
for row in range(1, n+1):
    for spaces in range(n - row):
        print(" ", end=" ")
    for star in range(1, row + 1):
        print("*"end=" ")
    print()

Task 2: Alphabet Triangle
Problem: Print a triangle of alphabets starting from numpy import number

from A.
Task 3:Hourglass pattern  
Combination of inverted and upright pyramids.

####################################################################
# *Tasks* 
# Write a Python program to find the most repeated word in a given paragraph.
paragraph = """python is well known programming language. python is easy to learn and python is widely used in data science is is is."""
words = paragraph.split()

max_count = 0
max_word = ""

for word in words:
    count = words.count(word)
    if count > max_count:
        max_count = count
        max_word = word

print("Most repeated word:", max_word)
print("Count:", max_count)



p = """python is well known programming language. python is easy to learn and python is widely used in data science is is is."""
words = p.split()
max_count = 0
max_word = ""
for word in words:
    count = words.count(word)
    if count > max_count:
        max_count = count
        max_word = word
print("Most repeated word:", max_word)
print("Count:", max_count)


#Write a Python program to remove duplicate words from a paragraph while maintaining the original order of words.
paragraph = input("Enter paragraph: ")

words = paragraph.split()
result = []

for word in words:
    if word not in result:
        result.append(word)

# Write a Python program to count the number of uppercase letters, lowercase letters, digits, and special characters present in a paragraph.
paragraph = input("Enter paragraph: ")

upper = lower = digit = special = 0

for ch in paragraph:
    if ch.isupper():
        upper += 1
    elif ch.islower():
        lower += 1
    elif ch.isdigit():
        digit += 1
    elif ch != " ":
        special += 1

print("Uppercase:", upper)
print("Lowercase:", lower)
print("Digits:", digit)
print("Special Characters:", special)
# Write a Python program to reverse the complete paragraph.
paragraph = input("Enter paragraph: ")

print(paragraph[::-1])

# Write a Python program to reverse each word in a paragraph without changing the order of the words.
paragraph = input("Enter a paragraph: ")

words = paragraph.split()

reverse_words = []

for word in words:
    reverse_words.append(word[::-1])

print("Paragraph after reversing each word:")
print(" ".join(reverse_words))

############################# function task ###################################

# Challenge Task 
# Design a Movie Ticket Booking function:
# def book_ticket(customer_name, movie_name, tickets=1, *snacks, **details):
# Requirements:
# Print customer name, movie name, and number of tickets.
# Print all snacks ordered.
# Print theatre, seat type, payment mode, and show time.
# Calculate the total ticket cost.

def book_ticket(customer_name, movie_name, tickets=1, *snacks, **details):
    ticket_price = 200
    total_cost = ticket_price * tickets

    print("---- Movie Ticket Booking Details ---")
    print(f"Customer Name: {customer_name}")
    print(f"Movie Name: {movie_name}")
    print(f"Number of Tickets: {tickets}")
    print(f"Total Ticket Cost: {total_cost}")

    print("Snacks Ordered:")
    if snacks:
        for snacks in snacks:
            print(f"- {snacks}")
    else:
        print("No snacks ordered.")

    print("Additional Details:")
    print("theatre:", details.get("theatre", "not specified"))
    print("seat type:", details.get("seat_type", "regular"))
    print("payment mode:", details.get("payment_mode", "cash"))
    print("show time:", details.get("show_time", "not specified"))

    print("--------------------------------------")
    print(f"Total Ticket Cost: ${total_cost}")
    print("Thank you for booking with us!")
    print("--------------------------------------")

    return total_cost

#function call
book_ticket(
    "santhos",
    "Avengers",
    tickets=2,
    snacks="popcorn",
    theatre="PVR",
    seat_type="premium",
    payment_mode="credit card",
    show_time="7:00 PM"
)    

# *Challenge Task* 
# *Bank Loan EMI*
# def loan_details(customer_name, loan_amount, years=1, *charges, **details):
# Requirements
# Print customer name.
# Print loan amount.
# Print processing charges.
# Print interest rate.
# Calculate EMI.
# Print total repayment.

def loan_details(customer_name, loan_amount, years=1, *charges, **details):
    print("---- Bank Loan Details ----")
    print(f"customer_name: {customer_name}")
    print(f"loan_amount: {loan_amount}")
    print(f"years: {years}")

    print("Processing Charges:")
    if charges:
        for charge in charges:
            print(f"- {charge}")
    else:
        print("No processing charges.")

    interest_rate = details.get("interest_rate", 0)
    print(f"Interest Rate: {interest_rate}%")

    # simple interest calculation
    total_interest = (loan_amount * interest_rate * years) / 100
    total_repayment = loan_amount + total_interest + sum(charges)
    emi = total_repayment / (years * 12)

    print(f"EMI: {round(emi, 2)}")
    print(f"Total Interest: {total_interest}")
    print(f"Total Repayment: {total_repayment}")
    
# function call
loan_details(
    "john",
    50000,
    2,
    1000, 500,  # processing charges
    interest_rate=5
)

# *Hospital Bill*
# def hospital_bill(patient_name, disease, days=1, *tests, **details):
# Requirements
# Print patient details.
# Print all medical tests.
# Print doctor name and room type.
# Calculate room charges.
# Add test charges.
# Print final hospital bill.

def hospital_bill(patient_name, disease, days=1, *tests, **details):
    print("---- Hospital Bill ----")
    print(f"Patient Name: {patient_name}")
    print(f"Disease: {disease}")
    print(f"Days Admitted: {days}")

    print("Medical Tests:")
    if tests:
        for test in tests:
            print(f"- {test}")
    else:
        print("No medical tests.")

    doctor_name = details.get("doctor_name", "not specified")
    room_type = details.get("room_type", "general")
    room_charge_per_day = details.get("room_charge_per_day", 0)
    
    total_room_charges = room_charge_per_day * days
    total_test_charges = sum(details.get("test_charges", []))
    final_bill = total_room_charges + total_test_charges

    print(f"Doctor Name: {doctor_name}")
    print(f"Room Type: {room_type}")
    print(f"Room Charges: {total_room_charges}")
    print(f"Test Charges: {total_test_charges}")
    print(f"Final Hospital Bill: {final_bill}")

# function call
hospital_bill(
    "Alice",
    "Flu",
    3,
    "Blood Test",
    "X-Ray",
    doctor_name="Dr. Smith",
    room_type="private",
    room_charge_per_day=500,
    test_charges=[200, 300]
)

# Scenario-Based Exercises1. 
# Student Marks (Tuples)Input: [("Alice", 85), ("Bob", 35), ("Charlie", 90)]
# Use filter → Select students who passed (marks ≥ 40)Use 
# sorted → Rank students by marksUse
# map → Add 5 grace marks to everyoneUse 
# reduce → Find total class score

from functools import reduce    
students = [("Alice", 85), ("Bob", 35), ("Charlie", 90)]
passed_students = list(filter(lambda x: x[1] >= 40, students))
rank_students = sorted(passed_students, key=lambda x: x[1], reverse=True) 
grace_students = list(map(lambda x: (x[0], x[1] +5), rank_students))
reduce_total_score = reduce(lambda x, y: x + y[1], grace_students, 0)
print("Passed Students:", passed_students)
print("Ranked Students:", rank_students)
print("Grace Marks Added:", grace_students)
print("Total Class Score:", reduce_total_score)



#  Task 1: Guess My Number (Game)

# Objective: Create a number guessing game.

# Requirements:
# Computer generates a random number between 1 and 100.
# User keeps guessing until correct.
# Give hints:
# Too High 🔺
# Too Low 🔻
# Count number of attempts.
# Show a congratulation message.
# Give only 7 chances.
# Add difficulty levels (Easy, Medium, Hard)

import random
number = random.randint(1,100)
attempts = 0
print("Welcome to the Guess My Number Game!")
while True:
    guess = int(input("enter your guess (between 1 and 100): "))
    attempts =+ 1
    if guess < number:
        print("too low")
    elif guess > number:
        print("too high")
    else:
        print(f"congratulations! you guessed the number {number} in {attempts} attempts.")
        break
print("Game Over! The number was:", number)







import random
print("Welcome to the Guess My Number Game!")
number = random.randint(1,100)
attempt =0
print("\n Difficulty Levels:")
print("1. Easy (10 attempts)")
print("2. Medium (7 attempts)")
print("3. Hard (5 attempts)")
difficulty = int(input("Choose difficulty level (1-3): "))
if difficulty == 1:
    max_attempts = 10
elif difficulty == 2:
    max_attempts = 7
elif difficulty == 3:
    max_attempts = 5
else:
    print("Invalid choice. Defaulting to Medium level.")
    max_attempts = 7

while attempt < max_attempts:
    guess = int(input("\n enter the guess number between 1 and 100: "))
    attempt += 1
    if guess < number:
        print("too low")
    elif guess > number:
        print("too high")
    else:
        print(f"congratulations! you guessed the number {number} in {attempt} attempts.")
        break
print("Game Over! The number was:", number)