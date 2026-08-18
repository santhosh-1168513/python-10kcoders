import numpy as np
# import time

# # on list
# # v = 10000000
# # list1 =list(range(v))
# # starttime = time.time()
# # result = [i*2 for i in list1]
# # endtime = time.time()
# # print("Time taken for list comprehension:", endtime - starttime)

# # # on numpy array
# # arr = np.arange(v)
# # arr_starttime = time.time()
# # res = arr *2
# # arr_endtime = time.time()
# # print("Time taken for numpy array operation:", arr_endtime - arr_starttime)

# # numpy is faster than list comprehension because it is implemented in C and optimized for performance. 
# # It uses vectorized operations that allow for efficient computation on large arrays, 
# # while list comprehension involves iterating over each element in the list,
# #  which can be slower for large datasets.

# # different essential ways to create numpy array
# # 1. Using np.array() - Manually creation 1D array

# arr = np.array([10, 20, 30, 40, 50])
# print(arr)
# print(arr.dtype)  # Output: int64 (or int32 depending on the system)    
# print(f"dimension array : {arr.ndim}")   # Output: 1
# print(arr.shape)  # Output: (5,)
# print(f"no of elements {arr.size}")  # Output: 5   
# print(f"no of array {arr.shape}") 
# print("-------------------------------------")

# # 2d array
# arr2 = np.array([
#     [10, 20, 30],
#     [40, 50, 60]
# ])
# print(arr2)
# print(arr2.dtype)  # Output: int64 (or int32 depending on the system)
# print(f"dimension array : {arr2.ndim}")   # Output: 2
# print(arr2.shape)  # Output: (2, 3)
# print(f"no of elements {arr2.size}")  # Output: 6
# print("-------------------------------------")

# # 3d array
# arr3 = np.array([[
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90]
# ]])
# print(arr3)
# print(arr3.dtype)  # Output: int64 (or int32 depending on the system
# print(f"dimension array : {arr3.ndim}")   # Output: 3
# print(arr3.shape)  # Output: (1, 3, 3)
# print(f"no of elements {arr3.size}")  # Output: 9
# print("-------------------------------------")

# # 2. np.zeros() - Create an array filled with zeros
# arr_zeros = np.zeros((3, 4))  # Creates a 3x4 array filled with zeros
# print(arr_zeros)
# print()

# arr_zeros = np.zeros((2, 3, 4))  # Creates a 2x3x4 array filled with zeros
# print(arr_zeros)

# # 3. np.ones() - Create an array filled with ones
# arr_ones = np.ones((2, 3))  
# print(arr_ones)

# arr_ones = np.ones((4,2))
# print(arr_ones)

# # 4. np.arange() - Create an array with a range of values
# arr = np.arange(1,10)
# print(arr)

# # 5. np.linspace() - Create an array with evenly spaced values
# arr = np.linspace(1, 10, 5)  # Creates an array with 5 evenly spaced values between 1 and 10
# print(arr)

# # 6. np.random.rand() - Create an array with random values between 0 and 1
# n = np.random.rand(5) # Creates a 3x4 array with random values between 0 and 1
# print(n)

# n = np.random.rand(2, 3) # Creates a 2x3 array with random values between 0 and 1
# print(n)

# n = np.random.rand(2, 3, 4) # Creates a 2x3x4 array with random values between 0 and 1
# print(n)

# # 7 np.full() - Create an array filled with a specified value
# arr_full = np.full((2, 3), 7)  # Creates a 2x3 array filled with the value 7
# print(arr_full)

# # 8. np.empty() - Create an uninitialized array (values will be random)
# arr_empty = np.empty((2, 3))  # Creates a 2x3
# print(arr_empty)
##################################### DAY2#####################################
# indexing and slicing in numpy array
# starts with 0 index

# a = np.array([1, 2, 3, 4, 5])
# print(a[2])

# a1 =np.array([[10,20,30],
#               [40,50,60]])
# print(a1[1,2])
# print(a1[0,])
# print(a1[1,2])

# a2 = np.array([[
#     [10, 20, 30],
#     [40, 50, 60],
#     [70, 80, 90]
#     ],
#     [
#     [100,200,300], 
#     [400,500,600],
#     [700,800,900]
#     ]])
# print(a2.ndim)
# # print(a2[0,1,2])
# # print(a2[1,2,0]) 
# # print(a2[0,1,0])
# print(a2[1,0,1])
# print(a2[:,1,2])
# # slicing in numpy array
# # [start:stop:step]

# # print(a2[1:4:1])
# # print(a2[:,1:3])

# #arithmetic operations in numpy array
# a = np.array([1,2,3,4,5])
# print(a+5)
# print(a-5)
# print(a*5)
# print(a/5)
# print(a**2)
# print(a%2)
# print(a//2)


# # vectorization in numpy array
# # vectorization is the process of performing operations on entire arrays or large chunks of data at once
# l1 = [1,2,3,4,5]
# l2 = [10,20,30,40,50]
# # without vectorization
# c = []
# for i in range(len(l1)):
#     c.append(l1[i]+l2[i])
# print(c)


# a = np.array([1,2,3,4,5])
# b = np.array([10,20,30,40,50])
# res = a + b
# print(res)

# print(a>a)

# marks = np.array([89, 90, 91, 90, 77, 77, 91])
# print(marks>75)
# print(marks[marks>75])  # Output: [89 90 91 90 77 77 91]

# # vectorization functions in numpy
# # np.add() - Element-wise addition
# # np.subtract() - Element-wise subtraction
# # np.multiply() - Element-wise multiplication
# # np.divide() - Element-wise division
# # np.power() - Element-wise exponentiation
# # np.sqrt() - Element-wise square root
# # np.sin(), np.cos(), np.tan() - Element-wise trigonometric functions
# # np.exp() - Element-wise exponential
# # np.max(), np.min(), np.mean(), np.median(), np.std() - Statistical functions

# marks = np.array([89, 90, 91, 90, 77, 77, 91])
# print(np.add(marks, 10)) 
# print(np.subtract(marks, 5))
# print(np.multiply(marks, 2))
# print(np.divide(marks, 2))

# import random
# np.random.seed(10)
# arr =np.random.randint(1,100,10)
# print(arr)


############################################################################

# # stack() it used to combine two array and create the new dimension
# a1 = np.array([10,20,30])
# a2 = np.array([40,50,60])
# combo = np.stack((a1,a2))
# print(combo)

# # hstack() it used to combine two array and create the new dimension
# combo =np.hstack((a1,a2))
# print(combo)

# # vstack() it used to combine two array and create the new dimension
# combo =np.vstack((a1,a2))
# print(combo)


# # split() it used to split the array into multiple sub-arrays
# arr = np.arange(9)
# splits = np.split(arr, 3)  # Splits the array into 3 equal parts
# print(splits)

# # example of split, concatenate, reshape, and flatten
# arr = np.arange(9)
# s1, s2, s3 =np.split(arr, 3)  # Splits the array into 3 equal parts
# print(s1,s2,s3)
# c=np.concatenate((s1,s2,s3))  # Concatenate the split arrays back together
# print(c.reshape(3,3))  # Reshape the concatenated array into a 3x3 array
# print(c.flatten())  # Flatten the concatenated array into a 1D array

# # example of vectorization
# import random
# np.random.seed(10) 
# salary =np.random.randint(10000,100000,10)
# print(f"BEFORE salary increment : {salary}")
# salary = salary+(salary*0.5)
# print(f"AFTER salary increment : {salary}")


# # broadcasting in numpy allows for operations between arrays of different shapes.
# # arr1 = np.array([1, 2, 3, 4, 5])
# # arr2 = np.array([10, 20, 30, 4])

# # res = arr1 + arr2  # Element-wise addition
# # print(res)

# # arr1 = np.array({[1,2,3,4]})
# # arr2 = np.array([
# #     [10],
# #     [20],
# #     [30],
# #     [40]
# # ])
# # res = arr1 + arr2  # Broadcasting addition
# # print(res)

# # arr1 = np.array([[1, 2, 3],
# #                  [4, 5, 6]])
# # arr2 = np.array([10,20,30])
# # result = arr1 + arr2  # Broadcasting addition
# # print(result)

# # arr1 = np.array([[1, 2, 3],
# #                     [4, 5, 6],
# #                     [7, 8, 9]])
# # arr2 = np.array([[1],
# #                     [2],
# #                     [3]])
# # result = arr1 + arr2  # Broadcasting addition
# # print(result)


# # arr1 = np.array([[1],
# #                     [2],
# #                     [3]])
# # arr2 = np.array([[10, 20, 30],
# #                     [40, 50, 60],
# #                     [70, 80, 90]
# #                     ])
# # result = arr1 + arr2  # Broadcasting addition
# # result1 = arr1 * arr2  # Broadcasting multiplication
# # print(result)
# # print(result1)


# # arr1 = np.array([[1, 2, 3],
# #                     [4, 5, 6],
# #                     [7, 8, 9]])
# # arr2 = np.array([[10 , 20, 30],
# #                     [40, 50, 60],
# #                     [70, 80, 90]
# #                     ])
# # print(arr1 + arr2)  # Element-wise addition

# arr1 = np.array([[1],
#                  [2],
#                  [3]])
# arr2 = np.array([[1],
#                  [2],
#                  [3]])
# print(arr1 + arr2)  # Element-wise addition


# # statistics in numpy array
# import random
# np.random.seed(10)
# marks = np.random.randint(36,99,10)
# print(f"marks : {marks}")

# r = np.reshape(marks, (2,5))
# r1 = np.reshape(marks, (5,2))
# print(r)
# print(r1)   

# print(np.sum(r,axis=0))  # Sum along columns
# print(np.sum(r,axis=1))  # Sum along rows

# print(np.max(marks))
# print(np.min(marks))
# print(np.mean(marks))
# print(np.median(marks))
# print(np.std(marks))
# print(np.var(marks))
# print(np.percentile(marks, 25))  # 25th percentile

# print(np.max(r, axis=1))  # Max along rows
# print(np.max(r, axis=0))  # Min along columns

# ######################################### Day4  ###################################

# marks = np.array([89, 90, 91, 90, 77, 77, 91,36,45,37])
# marks = np.sort(marks)
# print(marks)
# print(np.sum(marks))
# print(np.max(marks))
# print(np.min(marks))
# print(np.mean(marks)) # mean is the average of the numbers in the array. It is calculated by summing all the elements and dividing by the number of elements.
# print(np.median(marks))

# salary = np.random.randint([21000,13000,45000,70000,24000,3300,10000000])
# print(np.mean(salary))

# # unique values in numpy array
# marks = np.array([89, 90, 91, 90, 77, 77, 91,36,45,37,93,35,170])
# print(np.unique(marks))

# values,count=np.unique(marks,return_counts=True)  
# # print(values)  # Unique values in the arra
# # print(count)

# # for  mode, we not perform in mode directly
# mode = values[np.argmax(count)]
# print(mode)  # Mode of the array

# print(np.argmax(marks))  # Index of the maximum value, not value itself
# print(np.argmin(marks))  # Index of the minimum value, not value itself

# # range 
# r = np.max(marks) - np.min(marks)
# print(r)  # Range of the array

# # variance
# print(np.var(marks))

# # standard deviation
# print(np.std(marks))

# # Percentile 
# res = np.percentile(marks, 50)  
# print(res)

# # quantile
# q1 = np.quantile(marks, 0.25)
# q2 = np.quantile(marks, 0.50)
# q3 = np.quantile(marks, 0.75)

# print(q1)  
# print(q2)
# print(q3)

# # IQR 
# # iqr is the interquartile range, which is the difference between the third quartile (Q3) and the first quartile (Q1). 
# # It measures the spread of the middle 50% of the data and is less affected by outliers than the range.
# iqr = q3 -q1
# print(f" IQR : {iqr}")
# lower_bound = q1 - 1.5 * iqr
# upper_bound = q3 + 1.5 * iqr
# print(f"Lower Bound: {lower_bound}, Upper Bound: {upper_bound}")

# outliers = marks[(marks < lower_bound) | (marks > upper_bound)]
# print(f"Outliers: {outliers}")

# marks = marks[(marks >= lower_bound) & (marks <= upper_bound)]
# print(f"Marks after removing outliers: {np.sort(marks)}")

# print("-------------------------------------")
# # task : create a numpy array of 25 random integers between 1 and 100,
# # then replace the last element

# # to find the outliters 
# import random
# np.random.seed(10)
# v = np.random.randint(1,100,25)
# v[24] = 1000
# v[9] = -4585
# v[5] = -256
# print(v)

# q1 = np.quantile(v, 0.25)
# q2 = np.quantile(v, 0.50)
# q3 = np.quantile(v, 0.75)

# print(q1)
# print(q2)
# print(q3)

# iqr = q3 - q1
# lower_bound = q1 - 1.5 * iqr
# upper_bound = q3 + 1.5 * iqr
# print(f"Lower Bound: {lower_bound}, Upper Bound: {upper_bound}")

# outliers = v[(v < lower_bound) | (v > upper_bound)]
# print(f"Outliers: {outliers}")

# value = v[(v >= lower_bound) & (v <= upper_bound)]
# print(f"values of removing outlier : {np.sort(value)}")

# # cumsum() - Cumulative sum of the array elements
# marks = np.array([89, 90, 91, 90, 77, 77, 91,36,45,37])
# res = np.cumsum(marks)
# print(res)  

####################################### day 5 #######################################

# # matrix 
# a = np.random.randint(1,7,6)
# a = a.reshape(2,3)  # Reshape the array into a 2x3 array

# b = np.random.randint(1,7,6)
# b = b.reshape(2,3)  # Reshape the array into a 2x3 array

# result = a + b  # Element-wise addition of the two matrices
# print(result)

# # multiplication of two matrices
# # we used the dot product for matrix multiplication (np.dot() or the @ operator).
# # and by using matmul() function we can also perform the matrix multiplication

# # example of matrix multiplication
# a = np.random.randint(1,7,6)
# b = np.random.randint(1,7,6)
# a = a.reshape(2,3)  # Reshape the array into a 2
# b = b.reshape(3,2)  # Reshape the array into a 3x2 array

# result = np.dot(a,b)  # Matrix multiplication using dot product
# result1 = a @ b  # Matrix multiplication using @ operator
# result2 = np.matmul(a,b)  # Matrix multiplication using matmul() function
# print(result)
# print(result1)
# print(result2)

# # transpose of a matrix
# # The transpose of a matrix is obtained by flipping the matrix over its diagonal,
# # which means that the rows become columns and the columns become rows.

# arr = np.array([1,2],
#                [3,4])
# res = np.linalg.det(arr) # linalg is liner algebra and det is determinant of the matrix 

# np.linalg.solve() is a function in NumPy that solves a system of linear equations of the form Ax = b, where A is a square matrix and b is a vector. 
# It returns the solution vector x.
a = np.array([[2, 1],
              [1, 1]])
b = np.array([5, 3])
res = np.linalg.solve(a, b)  
print(res)

x = np.array([[3,2],
              [4,1]])
y = np.array([5,2])
res1 = np.linalg.solve(x,y)
print(res1)


