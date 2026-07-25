# # python tasks :-
# # ---------------------------------------------
# # 1. Shopping Bill
# # A customer buys:
# # Rice = ₹500
# # Oil = ₹200
# # Sugar = ₹15
# # Calculate:
# # Total amount
# # GST @ 18%
# # Final bill amount

rice_price = 500
oil_price = 200
sugar_price = 15    
total_amount = rice_price + oil_price + sugar_price
gst = total_amount * 0.18
final_bill_amount = total_amount + gst
print("total_amount:", total_amount)
print("gst:", gst)
print("final_bill_amount:", final_bill_amount)
print("------------------------------------------")
# 2. Mobile Purchase
# A mobile phone costs ₹25,000.
# Calculate:
# 10% discount
# Discount amount
# Final payable amount
mobile_price = 25000
discount = 0.10
discount_amount = mobile_price * discount
final_payable_amount = mobile_price - discount_amount
print("discount:", discount)
print("discount_amount:", discount_amount)
print("final_payable_amount:", final_payable_amount)
print("------------------------------------------")
# 3. Employee Salary
# An employee's basic salary is ₹30,000.
# Calculate:
# HRA = 20%
# DA = 10%
# Total salary

emp_sal = 30000
hra = emp_sal * 0.20
da = emp_sal * 0.10
total_sal = emp_sal + hra + da
print("hra:", hra)
print("da:", da)
print("total_sal:", total_sal)
print("------------------------------------------")
# 4. Student Marks
# Marks:
# English = 80
# Maths = 90
# Science = 85
# Calculate:
# Total marks
# Average marks
# Percentage
eng = 80
maths = 90
science = 85
total_marks = eng + maths + science
avg_marks = total_marks/3
percentage = (total_marks/300)*100
print('total_marks:', total_marks)
print('average_marks:', avg_marks)
print('percentage:', percentage)
print("------------------------------------------")


# 5. Restaurant Bill
# A family orders:
# Biryani = ₹300
# Cool Drinks = ₹100
# Ice Cream = ₹150
# Calculate:
# Total bill
# GST @ 5%
# Final bill

biryani_price = 300
cool_drinks_price = 100
ice_cream_price = 150
total_bill = biryani_price + cool_drinks_price + ice_cream_price
gst = total_bill * 0.05
final_bill = total_bill + gst
print(f"total_bill: {total_bill} and gst is: {gst} then final bill is: {final_bill}")
print("------------------------------------------")

# 6. Electricity Bill
# Units consumed = 250
# Rate per unit = ₹8
# Calculate:
# Total bill amount
unit_consumed = 250
rate_per_unit = 8
total_bill_= unit_consumed * rate_per_unit
print(f"total_bill: {total_bill_}")
print("------------------------------------------")

# 7. Movie Ticket Booking
# Ticket price = ₹200
# Number of tickets = 5
# Calculate:
# Total cost
# GST @ 12%
# Final amount

tp = 200
nt = 5
tc = tp * 5
gst = tc * 0.12
fc = tc + gst
print(F"total_cost: {tc} and gst is: {gst} then final cost is: {fc}")
print("------------------------------------------")

# 8. Online Course Fee
# Course fee = ₹15,000
# Discount = 20%
# Calculate:
# Discount amount
# Final fee
cf = 15000
discount = 0.20
discount_amount = cf * discount     
final_fee = cf - discount_amount
print(f"discount_amount: {discount_amount} and final fee is: {final_fee}")
print("------------------------------------------") 


# 9. Bank Fixed Deposit
# Principal = ₹50,000
# Rate = 6%
# Time = 2 years
# Calculate:
# Simple Interest
# Total Amount
principal = 50000
rate = 0.06         
time = 2
simple_interest = (principal * rate * time) / 100
total_amount = principal + simple_interest      
print(f"simple_interest: {simple_interest} and total amount is: {total_amount}")
print("------------------------------------------")

# 10. Petrol Expense
# Petrol price per litre = ₹105
# Litres purchased = 12
# Calculate:
# Total petrol cost
petrol_price_per_litre = 105
litres_purchased = 12               
total_petrol_cost = petrol_price_per_litre * litres_purchased
print(f"total_petrol_cost: {total_petrol_cost}")
print("------------------------------------------")



# 11. Laptop Purchase
# Laptop price = ₹60,000
# Discount = 15%
# GST = 18%
# Calculate:
# Discount amount
# Price after discount
# Final price after GST

laptop_price = 60000
discount = 0.15     
gst = 0.18
discount_amount = laptop_price * discount
price_after_discount = laptop_price - discount_amount
final_price = price_after_discount + (price_after_discount * gst)
print(f"discount_amount: {discount_amount}, price_after_discount: {price_after_discount}, final_price: {final_price}")  
print("------------------------------------------")

# 12. House Rent Calculation
# Monthly rent = ₹12,000
# Calculate:
# Rent for 6 months
# Rent for 1 year

monthly_rent = 12000
rent_for_6_months = monthly_rent * 6
rent_for_1_year = monthly_rent * 12
print(f"rent_for_6_months: {rent_for_6_months}, rent_for_1_year: {rent_for_1_year}")
print("------------------------------------------")

# 13. Cricket Score
# Runs scored in 5 matches:
# 45, 67, 89, 34, 78
# Calculate:
# Total runs
# Average runs
runs = [45, 67, 89, 34, 78]
total_runs = sum(runs)
average_runs = total_runs / len(runs)
print(f"total_runs: {total_runs}, average_runs: {average_runs}")
print("------------------------------------------")

# 14. Grocery Store
# Items:
# Milk = ₹60
# Bread = ₹40
# Eggs = ₹80
# Calculate:
# Total bill
# GST @ 5%
# Final amount

milk_price = 60 
bread_price = 40
eggs_price = 80
total_bill = milk_price + bread_price + eggs_price
gst = total_bill * 0.05 
final_amount = total_bill + gst
print(f"total_bill: {total_bill}, gst: {gst}, final_amount: {final_amount}")
print("------------------------------------------")

# 15. Salary Increment  
# Current salary = ₹40,000
# Increment = 10%
# Calculate:
# Increment amount
# New salary
current_salary = 40000
increment = 0.10
increment_amount = current_salary * increment
new_salary = current_salary + increment_amount
print(f"increment_amount: {increment_amount}, new_salary: {new_salary}")

# 16. Bike EMI
# Bike price = ₹1,20,000
# Down payment = ₹20,000
# Calculate:
# Loan amount 
# Number of EMIs = 24
# EMI amount
bike_price = 120000
down_payment = 20000    
loan_amount = bike_price - down_payment
number_of_emis = 24
emi_amount = loan_amount / number_of_emis
print(f"loan_amount: {loan_amount}, emi_amount: {emi_amount}")
print("------------------------------------------")

# 17. School Fee
# Tuition Fee = ₹25,000
# Exam Fee = ₹2,000
# Bus Fee = ₹5,000
# Calculate:
# Total annual fee

tuition_fee = 25000
exam_fee = 2000
bus_fee = 5000
total_annual_fee = tuition_fee + exam_fee + bus_fee
print(f"total_annual_fee: {total_annual_fee}")
# 18. Water Consumption
# Water consumed = 15,000 litres
# Cost per litre = ₹0.02
# Calculate:
# Total water bill
water_consumed = 15000
cost_per_litre = 0.02
total_water_bill = water_consumed * cost_per_litre
print(f"total_water_bill: {total_water_bill}")

# 19. Data Analyst Salary Package
# Basic Salary = ₹50,000
# Bonus = ₹10,000
# Calculate:
# Annual salary package
basic_salary = 50000
bonus = 10000
annual_salary_package = (basic_salary + bonus) * 12
print(f"annual_salary_package: {annual_salary_package}")
print("------------------------------------------")

# 20. E-commerce Order
# Product Price = ₹2,500
# Shipping Charge = ₹100
# GST = 18%
# Calculate:
# Total amount payable
product_price = 2500
shipping_charge = 100
gst = (product_price + shipping_charge) * 0.18
total_amount_payable = product_price + shipping_charge + gst
print(f"total_amount_payable: {total_amount_payable}")
print("------------------------------------------")