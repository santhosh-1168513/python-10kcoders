# to print the right angle triangle pattern
rows = 5
for row in range(1, rows+1):
    for star in range(row):
        print("*", end="")
    print()
print() # for space only

# inverted right angle triangle pattern
for row in range(rows, 0, -1):
    for star in range(row):
        print("*", end="")
    print()
print() # for space only

# to print pyramid pattern
for row in range(1, rows+1):
    for spaces in range(rows - row):
        print(" ", end="")
    for star in range(2 * row -1):
        print("*", end="")
    print()
print()

#inverted pyrmid pattern
for row in range(rows, 0, -1):
    for space in range(rows - row):
        print(" ", end=" ")
    for star in range(2 * row - 1):
        print("*", end=" ")
    print()
print()

#diamond patten
for row in range(1, rows+1):
    for space in range(rows - row):
        print(" ", end=" ")
    for star in range(2 * row - 1):
        print("*", end=" ")
    print()
for row in range(rows-1, 0, -1):
    for space in range(rows - row):
        print(" ", end=" ")
    for star in range(2 * row - 1):
        print("*", end=" ")
    print()

# reverse left angle triangle pattern
for row in range(rows, 0, -1):
    for star in range(row):
        print("*", end=" ")
    print()


# left angle triangle pattern
for row in range(1, rows+1):
    for spaces in range(rows - row):
        print(" ", end=" ")
    for star in range(row):
        print("*", end=" ")
    print()
print()

for row in range(rows, 0, -1):
    for spaces in range(rows - row):
        print(" ", end=" ")
    for star in range(row):
        print("*", end=" ")
    print()
print()

# hallow square pattern
for row in range(1, rows+1):
    for star in range(rows):
        if row == 1 or row == rows or star == 0 or star == rows-1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

#hallow rectangle pattern
for row in range(1, rows+1):
    for star in range(rows+2):
        if row == 1 or row == rows or star == 0 or star == rows+1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print()

# hallow right angle triangle pattern
for row in range(1, rows+1):
    for star in range(row):
        if star == 0 or star == row-1 or row == rows:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print()

#hallow inverse right angle triangle pattern
for row in range(rows, 0, -1):
    for star in range(row):
        if star == 0 or star == row - 1 or row == rows:
            print("*", end=" ")
        else:   
            print(" ", end=" ") 
    print()
print()

#Hollow Pyramid Pattern in Python
for row in range(1,rows+1):
    for space in range(rows - row):
        print(" ", end=" ")
    for star in range(2 * row -1):
        if star == 0 or star == 2 * row - 2 or row == rows:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print() 

#Hollow Inverted Pyramid Pattern in Python
for row in range(rows, 0, -1):
    for space in range(rows - row):
        print(" ", end=" ")
    for star in range(2* row - 1):
        if star ==0 or star == 2*row -2 or row == rows:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
print()

#HALLOW DIAMOND PATTERN IN PYTHON
for row in range(1, rows+1):
    for space in range(rows - row):
        print(" ", end=" ")
    for star in range(2 * rows-1):
        if star == 0 or star == 2*row-2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()
for row in range(rows-1, 0, -1):
    for space in range(rows - row):
        print(" ", end=" ")
    for star in range(2*row-1):
        if star == 0 or star == 2*row-2:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()


# number right angle triangle pattern
for row in range(1, rows+1):
    for num in range(1, row+1):
        print(num, end=" ")
    print()
print()

# number inverted right angle triangle pattern
for row in range(rows, 0, -1):
    for num in range(1, row+1):
        print(num, end=" ")
    print()

for row in range(1, rows+1):
    for space in range(rows - row):
        print(" ", end=" ")
    for num in range(1, row+1):
        print(num, end=" ")
    print()
print()

# number pyramid pattern
for row in range(1, rows+1):
    for space in range(rows - row):
        print(" ", end=" ")
    for num in range(1, row+1):
        print(num, end=" ")
    for num in range(row-1, 0, -1):
        print(num, end=" ")
    print()

#alphabet right angle triangle pattern
for row in range(1, rows+1):
    for alp in range(row):
        print(chr(65 + alp), end= " ")
    print()

for i in range(1, rows + 1):  # Outer loop for rows
    for j in range(1, rows + 1):  # Inner loop for columns
        print(j, end=" ")  # Print numbers
    print()

# pascal's triangle
n = 5
for i in range(n):
    num = 1
    for j in range(1, i + 1):
        print(num, end=" ")
        num = num * (i - j) // (j+1)
    print()

# floyds triangle
n = 5
num = 1
for i in range(1, n + 1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

