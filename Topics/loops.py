# to write a program to check if a number is even or odd
for i in range(0, 11):
    if i % 2 == 0:
        print(i,"is even number")
    else:
        print(i,"is odd number")

#to print the weekdays only not weelends
week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
for day in week:
    if day == "saturday" or day == "sunday":
        continue
    print(f"{day} is a weekdays")
else:
    print("weekdays are printed successfully")

week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
for day in week:
    if day == ["saturday", "sunday"]:
        continue
    print(f"{day} is a weekdays")
else:
    print("weekdays are printed successfully")

#to print 5 starts
for i in range(1,6):
    print("*")

# to print stars in row
for i in range(1,6):
    print("*",end=" ")

print()
# to print stars in row and column
for i in range(5):
    for j in range(5):
        print("*",end=" ")
    print()

# i want to convert to loweer case
s = []
stu = ["SANTHOSH", "RAJESH", "KUMAR", "RAJ", "SAN"]
for i in stu:
    s.append(i.lower())
print(s)


email = ["santhosh@gmail.com", "siva@yahoo.com", "kumar@outlook.com"]
for i in email:
    if 