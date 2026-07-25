"""
        *
      * *
    * * *
  * * * *
* * * * * 
"""
rows = 5
for i in range(rows, 0, -1):
    for star in range(1, i + 1):
        print("*", end="")
    print()

"""
* * * * * 
* * * * 
* * * 
* * 
* 
"""
for row in range(5, 0, -1):
    for star in range(row):
        print("*", end=" ")
    print()

"""
        *
      * *
    * * *
  * * * *
* * * * * 
"""
for row in range(1,rows+1):
    for spaces in range(rows - row):
        print(" ", end=" ")
    for star in range(row):
        print("*", end=" ")
    print()
print()
"""
* * * * * 
  * * * * 
    * * * 
      * * 
        * 
"""
for row in range(rows, 0, -1):
    for spaces in range(rows - row):
        print(" ", end=" ")
    for star in range(row):
        print("*", end=" ")
    print()

"""
*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
* 
"""
for row in range(1,rows+1):
    for star in range(row):
        print("*", end=" ")
    print()
for row in range(rows-1,0,-1):
    for star in range(row):
        print("*", end=" ")
    print()
# pyramidpatten
for row in range(1, rows+1):
    for space in range(rows - row):
        print(" ", end=" ")
    for star in range(2 * row - 1):
        print("*", end=" ")
    print()
print()
# Inverted pyramid pattern
for row in range(rows, 0, -1):
    for space in range(rows - row):
        print(" ", end=" ")
    for star in range(2 * row - 1):
        print("*", end=" ")
    print()

#diamond pattern
for row in range(1, rows+1):
    for space in range(rows - row):
        print(" ", end=" ")
    for star in range(2 * row - 1):
        print("*", end=" ")
    print()
for row in range(rows, 0, -1):
    for space in range(rows - row):
        print(" ", end=" ")
    for star in range(2 * row - 1):
        print("*", end=" ")
    print()

# hollow box pattern
for row in range(1, rows + 1):
    for col in range(rows):
        # print stars on the first or last row, or first or last column
        if row == 1 or row == rows or col == 0 or col == rows - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

#hallow triangle pattern
for row in range(rows):
    for col in range(rows):
        # print stars on the first or last row, or first or last column
        if col == 0 or col == row or row == rows - 1:
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

