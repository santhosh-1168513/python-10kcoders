import pandas as pd
import numpy as np

# s = pd.Series((10,20,30,40,50))
# print(s)

# s = pd.Series([10, 20, 30, 40, 50], index=['a', 'b', 'c', 'd', 'e'])
# print(s)

# data = {
#     "sid": [1, 2, 3, 4, 5],
#     "sname": ["John", "Jane", "Jim", "Jill", "Jack"],
#     "sage": [20, 25, None, 35, 40]
# }
# df = pd.DataFrame(data)
# print(df)


# # To read a CSV file using the csv module in python manually way
# # import csv
# # with open("students.csv", mode='r') as file:
# #     data = csv.reader(file)

# #     for line in data:
# #         print(line)


# # To read a CSV file using pandas data is varable
# data= pd.read_csv(r'C:\Users\sivasankar\Downloads\python pratices\Topics\students.csv')
# print(data)

# print(data.info()) # information about the Data

# print(data.describe()) # statistical information about the Data, it works only for numerical data

# print(data.shape) # returns a tuple representing the dimensionality of the DataFrame

# rows, columns = data.shape
# print(f"Number of rows: {rows}, Number of columns: {columns}")

# print(data.head()) # returns the first 5 rows of the DataFrame
# print(data.head(10)) # returns the first 10 rows of the DataFrame

# print(data.tail()) # returns the last 5 rows of the DataFrame
# print(data.tail(10)) # returns the last 10 rows of the DataFrame

# print(data.columns) # returns the column names of the DataFrame

# print(data['Name']) # returns the 'sname' column of the DataFrame

############################ TO READ THE EXCEL FILES #############################################

# TO read an Excel file using pandas

# df = pd.read_excel(r'C:\Users\sivasankar\Downloads\sample-chocolate-shipments-data-all-Apr-2025.xlsx', sheet_name='shipments')
# print(df)

# print(df.info()) # information about the Data
# print(df.head()) # returns the first 5 rows of the DataFrame

# from sqlalchemy import create_engine    
# import pandas as pd

# # create a connection to the database
# engine = create_engine("mysql+pymysql://root:rach@localhost:3306/green_bloom_db")

# df = pd.read_sql("SELECT * FROM products", engine)

# print(df)

# ----------------------------- DAY 2 ------------------------------------

# data = pd.read_csv(r'C:\Users\sivasankar\Downloads\python pratices\Topics\students.csv')
# print(data)


# print(data.loc[1:4,['Name','StudentID']]) # returns the rows from index 1 to 4 and columns 'Name' and 'student_id'

# print(data.loc[1:4]) # returns the rows from index 1 to 4 and all columns

# print(data.iloc[1:4,[0,1]]) # returns the rows from index 1 to 4 and columns at index 0 and 1

# # by head and tail
# print(data.head(5).tail(1))


# # to upadate the value of a specific cell in the DataFrame
# # data.loc[2, 'Name'] = 'santhosh'
# # print(data)

# # data.to_csv(r'C:\Users\sivasankar\Downloads\python pratices\Topics\students.csv', index=False) 
# # # to save the DataFrame to a CSV file without the index column

# # data.drop(6, axis=0, inplace=True) # to delete a row from the DataFrame by index
# # print(data)
# # # to save
# # data.to_csv(r'C:\Users\sivasankar\Downloads\python pratices\Topics\students.csv', index=False)

# # data.drop('Jane Smith', axis=1, inplace=True) # to delete a column from the DataFrame by column name
# # print(data)
# # data.to_csv(r'C:\Users\sivasankar\Downloads\python pratices\Topics\students.csv', index=False) # to save the DataFrame to a CSV file without the index column

# # iloc is used to select rows and columns by index position, while loc is used to select rows and columns by label.
# # variable.iloc[row_index, column_index] # to select a specific cell in the DataFrame by index position
# print(data.iloc[1,1])
# print(data.iloc[3, 1])

# print(data.iloc[0,1:3])
# print(data.iloc[1:4, 0:2]) 


# # newrecord = pd.DataFrame([7,'santhsoh,3.15,2026'],columns=data.columns)
# # pd.concat([data.iloc[2:], newrecord,data.iloc[:2]]).reset_index(drop=True)
# # print(data)

# ########################################## day3 ################################

# handle the null values by the find, fill, drop, and replace methods
# data ={
#     'stid':[1,2,3,4,5],
#     'sname':['santhosh',np.nan,'kumar','raja','karthi'],
#     'sage':[20,25,np.nan,34,40],
#     'study_hours':[2,2,np.nan,5,np.nan],
#     'smarks':[80,90,70,60,-60]
# }

# df = pd.DataFrame(data)
# print(df)

# print(df.loc[2:3])
# print(df.loc[3,'sage'])

# print(df.isnull()) # returns a DataFrame of the same shape as df, with True for each cell that is null and False for each cell that is not null
# print(df[df.isnull().any(axis=1)]) # returns a DataFrame of the rows that contain at least one null value

# print(df.isnull().sum()) # returns a Series with the count of null values in each column
# print(df.isnull().sum().sum()) # returns the total count of null values in the DataFrame

# print(df.dropna()) # returns a DataFrame with the rows that contain at least one null value dropped
# print(df.dropna(subset=['sage', 'study_hours'])) # returns a DataFrame with the columns that contain at least one null value dropped

# print(df.fillna(0)) # for numerical columns, it replaces the null values with 0
# print(df.fillna('unknown')) # for string columns, it replaces the null values with 'unknown'
# fpr particular column
# print(df['sage'].fillna(0))
# print(df['sname'].fillna('unknown'))
# df['sname']= df['sname'].fillna('unknown')

# df['sage']=df['sage'].fillna(df['sage'].median())
# print(df)
# # if outlier there dont fill with mean or median, we can use the mode to fill the null values

# df['sname']=df['sname'].ffill() # forward fill, it fills the null values with the previous value in the column
# print(df)
# df['sage']=df['sage'].bfill() # backward fill, it fills the null values with the next value in the column
# print(df)   


# for duplicates values
# print(df.duplicated()) # returns a Series with True for each row that is a duplicate of a previous row and False for each row that is not a duplicate
# print(df.duplicated(subset=['sname', 'sage','study_hours'])) # returns a Series with True for each row that is a duplicate of a previous row and False for each row that is not a duplicate
# print(df.drop_duplicates())
# print(df.drop_duplicates(subset=['study_hours'])) # returns a DataFrame with the duplicate rows dropped


# find the ouliers  of age
# q1 = df['sage'].quantile(0.25)
# q2 = df['sage'].quantile(0.5)
# q3 = df['sage'].quantile(0.75)

# iqr = q3 - q1
# lower_bound = q1 - 1.5 * iqr
# upper_bound = q3 + 1.5 * iqr

# outliers = df[(df['sage'] < lower_bound) | (df['sage'] > upper_bound)]
# print(outliers) 

# df = pd.DataFrame({
#     "empid":[1,2,3,4,5],
#     "empname":["sai","santhosh","manoj","kumar","kumar"],
#     "salary":[32000,35000,30000,40000,45000]
# })
# # asatype() method is used to convert the data type of a column in a DataFrame to a different data type. It can be used to convert a column to a different numerical type, string type, or categorical type.
# df['salary'] = df['salary'].astype(str)
# print(df.dtypes) 

######################################################################################################

data = pd.read_csv(r'C:\Users\sivasankar\Downloads\python pratices\Topics\students.csv')
# print(data)
print(data.info())
# print(data[data['Marks'] > 90])
# print(data[(data['Marks'] > 90) & (data['Age'] < 25)])
# print(data[(data['Marks'] > 90) | (data['Age'] < 25)])
# print(data[data['Department'].isin(['CSE', 'ECE'])])

# data['Name'] = data['Name'].str.upper()
# print(data)

# data['City'] = data['City'].str.lower()
# print(data)

# print(data[data['Name'].str.startswith('A') | data['Name'].str.startswith('S')])

# print(data[data['Name'].str.startswith('A') | data['Name'].str.endswith('S')])

# data['Name_len'] = data['Name'].str.len()
# print(data)

# data['occ'] = data['Name'].str.count('A')
# print(data)

# data['find'] = data['Name'].str.find('A')
# print(data[['Name', 'find']])

# data['slice'] = data['Name'].str.slice(0, 3)
# print(data[['Name', 'slice']])

# print(data['Name'].str.split('-'))

# print(data['Name'].str.extract(r'([A-Z][a-z]+)')) 
###########################################################################################
# dt accessor is used to access the datetime properties of a pandas Series or DataFrame column that contains datetime-like values. 
# It allows you to extract specific components of the datetime values, such as year, month, day, hour, minute, second, etc.

# print(data[data['Hiredate'].dt.year == 2015])
# data['month_name'] = data['Hiredate'].dt.month_name()
# print(data[['Hiredate', 'month_name']])

# years of experience of the employees
# today = pd.timestamp.today()
# df['exp'] = ((today - df['Hiredate']).dt.days/365)
# print(df[['Hiredate', 'exp']]


# apply() method is used to apply a function along an axis of the DataFrame or on values of Series. 
# It can be used to apply a function to each row or column of a DataFrame, or to each element of a Series.

# map() method is used to apply a function to each element of a Series.
#  It can be used to transform the values of a Series based on a mapping function or a dictionary.

# values of the 'Gender' column to 'M' for Male and 'F' for Female using the map()
# data['Gender_status'] = data['Gender'].map({'Male':'M', 'Female': 'F'})
# print(data[['Gender','Gender_status']])

###############################################################################################
