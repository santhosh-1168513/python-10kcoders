# water = 100
# level = 0
# while level <= water:
#     print("water level is",level)
#     level += 10
# print("water level is full")


# s = input("enter the yes or no: ")
# ink = 0
# while s == "yes":
#     ink += 10
#     print("ink level is",ink)
#     break
# print("ink level is full")

# s = input("enter the yes or no: ")
# ink = 0
# while s == "yes":
#     if ink < 100:
#         ink += 10
#         print("ink level is",ink)
#     else:
#         print("ink level is full")
#         break
# print("ink level is full")



# ink_level = 10
# while ink_level > 0:
#     answer = input("do you want to print the page yes or no: ")
#     if answer == "yes":
#         print("pen is working")
#         ink_level -=2
#     else:
#         print("pen is not working")
#         break
# print("ink level is",ink_level)   


# 4*1= 4
# 4*2= 8
# 4*3= 12
# n = int(input("enter the number: "))
# i = 1
# while i<=10:
#     print(n, "*", i, "=", n*i)
#     i += 1

# i = 1
# v = 4
# while i<10:
#     j = 1
#     while i <= 1:
#         print(f"{v} * {i} = {v*i}")
#         j += 1
#     i += 1



print("4"*3)


rows = 5
for row in range(1, rows+1):
    print("*" * row)
print()

rows = 5
for row in range(5,0,-1):
    print("*" * row)

rows = 5
