import pandas as pd
import numpy as np

# Full Cleaning Pipeline

# Create a messy DataFrame and write a cleaning pipeline that:
# data = {
#     "StudentID": [101, 102, 103, 104, 105, 106, 107, 108, 109, 101],
#     "Name": ["santhosh", "siva", "kumar", "sai", "Eva", "gopal", "vani", "viswanath", "Ivy", " Alice "],
#     "Age": [20, 21, 19, 22, 20, 21, 23, 20, 22, 20],
#     "City": [" Bangalore ", "Chennai", " Bangalore", "Mumbai ", "Chennai", "Delhi", " Mumbai", "Delhi ", "Chennai", " Bangalore "],
#     "Subject": ["Math", "Math", "Science", "Science", "Math", "English", "English", "Science", "Math", "Math"],
#     "Marks": [85, np.nan, 72, 95, 45, 88, np.nan, 120, 78, 85],
#     "Grade": ["A", "B", "C", "A", "D", "A", "B", "A", "B", "A"]
# }

# df = pd.DataFrame(data)
# # print(data)
# print(df)

# # 1. Detects and fills missing Marks with subject-wise median
# df['Marks'] = df['Marks'].fillna(df.groupby('Subject')['Marks'].transform('median'))

# # 2. Removes duplicate StudentIDs (keep first)
# print(df.drop_duplicates(subset='StudentID', keep='first'))

# # 3. Converts Marks to float and Age to int
# print(pd.to_numeric(df["Marks"], errors='coerce'))
# print(pd.to_numeric(df["Age"], errors='coerce').astype(int))

# # 4. Strips whitespace from Name and City columns
# print(df['Name'].str.strip())
# print(df["City"].str.strip())

# # 5. Removes outliers using IQR method on Marks
# q1 = df['Marks'].quantile(0.25)
# q3 = df['Marks'].quantile(0.75)

# iqr = q3 - q1
# lower_bound = q1 - 1.5 * iqr
# upper_bound = q3 + 1.5 * iqr
# df = df[(df['Marks'] >= lower_bound) & (df['Marks'] <= upper_bound)]
# print(df)





# Transform the Student Data
# Add a Grade_Points column mapping A→4, B→3, C→2, D→1
# Add a Result column: "Pass" if Marks ≥ 50, else "Fail"
# Add a Band column using pd.cut: Fail/Pass/Merit/Distinction
# Rank all students by Marks (1 = highest)
# Print the top 5 and bottom 5 students


#  Task
# GroupBy Analysis
# Find average Marks, max Marks, and student count per Subject
# Find the pass rate (Marks ≥ 50) per City
# Add a column showing each student's deviation from their subject average
# Create a pivot table: Subject × Grade showing count of students
# Filter to keep only Cities where average Marks > 75


#------------------------------------------------------------------------------------------------------------#
import pandas as pd

df = pd.read_csv(r'C:\Users\sivasankar\Downloads\python pratices\Topics\employees.csv')

print(df)


# stage 1:
# display the first 5 rows of the DataFrame
print(df.head())

# display the first 10 rows of the DataFrame
print(df.head(10))

# display the last 5 rows of the DataFrame
print(df.tail())

#find the number of rows and columns in the DataFrame
print(df.shape)

# display the column names of the DataFrame
print(df.columns)

# display the data types of each column in the DataFrame
print(df.dtypes)

# display the dataframe index
print(df.index)

# display the datatype of every column 
print(df.info())

# get the complete information about the DataFrame
print(df.describe())

# generate statisal information about the DataFrame
print(df.describe(include='all'))

# 1. Find the number of unique departments.
print(df["Department"].nunique())

# 2. Display all unique departments.
print(df["Department"].unique())

# 3. Find the number of unique cities.
print(df["City"].nunique())

# 4. Display all unique cities.
print(df["City"].unique())

# 5. Find the number of unique job titles.
print(df['Job_Title'].nunique())

# 6. Display all unique job titles.
print(df['Job_Title'].unique())

# 7. Find the number of unique performance ratings.
print(df['Performance'].nunique())

# 8. Display all unique performance ratings.
print(df['Performance'].unique())

#----------------------------------------------------------------------------------------------------
# satge2
# select one column
print(df['Name'])

# select multiple columns
print(df[['Name', 'Department']])

# multiple coloumns
#iloc is used to select rows and columns by their integer position in the DataFrame.
print(df.iloc[0])
print(df.iloc[1])

print(df.iloc[0:5])  
#0:5 -> 0,1,2,3,4

# select specific rows 
print(df.iloc[[0,5,11,15]])

# select specific rows and columns
print(df.iloc[0:5, 0:3])
# 0:5 -> ROWS 0,1,2,3,4
# 0:3 -> COLUMNS 0,1,2

# select specific rows and columns
print(df.iloc[[0,5,11,15], [0,1,2]])
#rows - > 0,5,11,15
#columns -> 0,1,2

# loc is used to select rows and columns by their labels in the DataFrame.
print(df.loc[0])

print(df.loc[0:4,['Name', 'Department']])

print(df.loc[[0,5,11,15], ['Name', 'Department']])

print(df.loc[df['Department'] == 'IT', ['Name', 'Department']])

print(df.loc[df['Salary'] > 60000, ['Name', 'Salary']])

# show all the rows where the Salary is greater than 50000
print(df['Salary']>50000)

# show all the rows where the Salary is greater than 50000
print(df[df['Salary']>50000])

# show only it employess
print(df[df['Department']=='IT'])

# multiple conditions
print(df[(df['Department']=='IT') & (df['Salary']>50000)])
# & - and
# | - or
# ~ - NOT

# multiple conditions using isin
print(df[df['Department'].isin(['IT', 'HR'])])

# range of values using between
print(df[df['Age'].between(25, 30)])

# not condition
print(df[~df['Department'].isin(['IT', 'HR'])])
print(df[df['Department']!='IT'])

# string filtering methods
#str.comtains() - checks if a string contains a specific substring
print(df[df['Name'].str.contains("kumar",na=False)])

#str.startswith() - checks if a string starts with a specific substring
print(df[df['Name'].str.startswith("s",na=False)])

#str.endswith() - checks if a string ends with a specific substring
print(df[df['Name'].str.endswith("h",na=False)])

# TASK
# 1. display emp with salary greater than 50000
print(df[df['Salary']>50000])

# 2. Display employees whose age is greater than 30.
print(df[df['Age']>30])

# 3. Display only Sales employees.
print(df[df['Department']=='Sales'])

# 4. Display employees with experience less than 5.
print(df[df['Experience']<5])

# 5. Display employees with salary less than or equal to 40000.
print(df[df['Salary']<=40000])

# 6. Display IT employees with salary greater than 60000.
print(df[(df['Department']=='IT') & (df['Salary']>60000)])

# 7. Display employees from IT or Finance.
print(df[df['Department'].isin(['IT', 'Finance'])])

# 8. Display employees whose age is between 25 and 30.
print(df[df['Age'].between(25, 30)])

# 9. Display employees from IT, HR, or Sales using isin().
print(df[df['Department'].isin(['IT', 'HR', 'Sales'])])

# 10. Display employees who are not from Marketing.
print(df[~df['Department'].isin(['Marketing'])])
print(df[df['Department']!='Marketing'])

# 11. Find employees whose name contains "Kumar".
print(df[df['Name'].str.contains("Kumar", na=False)])

# 12. Find employees whose name starts with "A".
print(df[df['Name'].str.startswith("A", na=False)])

# 13. Find employees whose job title contains "Manager".
print(df[df['Job_Title'].str.contains("Manager", na=False)])

# IT employees with salary > 60000 and experience < 5
print(
    df[
        (df['Department'] == 'IT')
        & (df['Salary'] > 60000)
        & (df['Experience'] < 5)
    ]
)

# -------------------------------------------------------------------------
# Data Cleaning:

# Detect missing values
# Count missing values
# Remove missing values
# Fill missing values
# Detect duplicates
# Remove duplicates
# Clean strings
# Replace values
# Change data types

# to detect missing values
print(df.isnull())
print(df.isna())
# if get the true where the missing values
# false where the values are present

# count the missing values in each column
print(df.isnull().sum())

# to find the rows containing missing values
print(df[df.isnull().any(axis=1)])
 #axis=1 means check for missing values across columns (i.e., in each row). If any column in a row has a missing value, that row will be included in the result.

# particlar column missing values
print(df[df['Salary'].isnull()])
print(df[df['Age'].isnull()])

# remove rows with missing values
# cleaned_df = df.dropna()
# print(cleaned_df)
#  # to check the missing values
# print(cleaned_df.shape)
# print(cleaned_df.isnull().sum())

# fill missing vaue
# by mean
# df['Salary'] = df['Salary'].fillna(df['Salary'].mean())
# df['Age'] = df['Age'].fillna(df['Age'].mean())
# df["City"] = df["City"].fillna("Unknown")
# df["Performance"] = df["Performance"].fillna("Not Rated")
# df['Experience'] = df['Experience'].fillna(df['Experience'].median())
# print(df.isnull().sum())


# detect the duplicate rows
print(df.duplicated())
print(df.duplicated().sum())
print(df[df.duplicated()])

# remove the duplicate rows
df = df.drop_duplicates()
print(df.shape)


# clean the extra spaces in the string columns
print(df.loc[31, 'Name'])

df['Name'] = df['Name'].str.strip()
print(df.loc[31, 'Name'])

df['Name'] = df['Name'].str.lower()
print(df.loc[0:40, 'Name'])

df['Name'] = df['Name'].str.title()
print(df.loc[0:40, 'Name'])

df['Name'] = df['Name'].str.upper()
print(df.loc[0:40, 'Name'])

# replace the values in a column
df['Department'] = df['Department'].replace('IT', 'Information Technology')

df['Gender'] = df['Gender'].replace({'M': 'Male', 'F': 'Female'})
print(df['Gender'])

df["Status"] = df["Status"].replace("Active", "ACTIVE")
print(df["Status"])

# check data types of each column
print(df.dtypes)

# convert the data type of a column
df['Salary'] = df['Salary'].astype(float)

# convert date column to datetime
df['Joining_Date']= pd.to_datetime(df['Joining_Date'], errors='coerce')
print(df['Joining_Date'])

#------------------------------------------------stage 5----------------------------------------#
# creating a new column based on existing columns
df['Total_compensation'] = df['Salary'] + df['Bonus']
print(df[['Salary', 'Bonus', 'Total_compensation']])

# apply is a method that allows you to apply a function along an axis of the DataFrame (either rows or columns). 
# It can be used to create new columns based on existing data.
# suppose
# salary >= 60000 -> High
# salary < 60000 -> Low
def categorize_salary(Salary):
    if Salary >= 60000:
        return 'High'
    else:
        return 'Low'    

df['Salary_Category'] = df['Salary'].apply(categorize_salary)
print(df[['Salary', 'Salary_Category']])

# lambda function is an anonymous function that can be defined in a single line. 
# It is often used for simple operations or when you need to pass a function as an argument to another function.
df['Salary_Category'] = df['Salary'].apply(lambda x: 'High' if x >= 60000 else 'Low')
print(df[['Salary', 'Salary_Category']])

# map is a method that allows you to map values of a Series according to an input mapping or function.
# It can be used to transform or replace values in a column based on a mapping dictionary or a function.
performance_map = {
    "Excellent": 3,
    "Good": 2,
    "Average": 1
}

df["Performance_Score"] = df["Performance"].map(performance_map)
print(df[["Performance", "Performance_Score"]])

# np,where is a function that allows you to apply conditional logic to your DataFrame.
# It can be used to create new columns based on conditions or to modify existing columns based on certain criteria.
import numpy as np
df['Salary_Level'] = np.where(df['Salary'] >= 60000, 'High', 'Low')
print(df[['Salary', 'Salary_Level']])

# to check the multiple conditions
conditions = [
    (df['Salary'] >= 60000) & (df['Experience'] >= 5),
    (df['Salary'] >= 60000) & (df['Experience'] < 5),
    (df['Salary'] < 60000) & (df['Experience'] >= 5),
    (df['Salary'] < 60000) & (df['Experience'] < 5)
]

choices = ['High Salary & Experienced', 'High Salary & Less Experienced', 'Low Salary & Experienced', 'Low Salary & Less Experienced']

df['Salary_Experience_Category'] = np.select(conditions, choices, default='Unknown')
print(df[['Salary', 'Experience', 'Salary_Experience_Category']])   

# pd.cut is a function that allows you to segment and sort data values into discrete bins or intervals.
# It can be used to create categorical variables based on continuous data.

df['Salary_Bin'] = pd.cut(df['Salary'], bins=[0, 40000, 60000, 80000, 100000],
                           labels=['Low', 'Medium', 'High', 'Very High'])

print(df[['Salary', 'Salary_Bin']])

#----------------------------------------------------------------stage6 -----------------------------------------
# group by : Group the data by something, then calculate something for each group.
print(df.groupby('Department')['Salary'].mean().round(2))
#            groupby dep            calculate average

print(df.groupby('Department')['Salary'].sum())
print(df.groupby('Department')['Salary'].max())
print(df.groupby('Department')['Salary'].min())
print(df.groupby('Department')['Salary'].count())
print(df.groupby('Department')['Salary'].std())
print(df.groupby('Department')['Salary'].var())

# incase multiple columns
print(df.groupby('Department')[['Salary', 'Bonus']].mean().round(2))

# muliple aggregation functions
print(df.groupby('Department')['Salary'].agg(
    ['mean', 'sum', 'max', 'min', 'count', 'std', 'var']).round(2))

# named aggreastion
print(df.groupby('Department').agg(
    Average_Salary=('Salary', 'mean'),
    Total_Salary=('Salary', 'sum'),
    Max_Salary=('Salary', 'max'),
    Min_Salary=('Salary', 'min'),
    Employee_Count=('Salary', 'count'),
    Salary_StdDev=('Salary', 'std'),
    Salary_Variance=('Salary', 'var')
).round(2))

# GROUPBY + SORTING
result = df.groupby('Department')['Salary'].mean().sort_values(ascending=True)
print(result)

# -------------------------------------------------- stage 7---------------------------------------------
# data and time 
# we'll work with
# pd.to_datetime()
# dt.year
# dt.month
# dt.day
# dt.month_name()
# dt.day_name()
# date filtering
# date differences

# convert the datatime
df['Joining_Date'] = pd.to_datetime(df['Joining_Date'], errors='coerce')
print(df["Joining_Date"].dtype) # to check

# extract year, month, day, month name, day name
df['Joining_Year'] = df['Joining_Date'].dt.year
df['Joining_Month'] = df['Joining_Date'].dt.month
df['Joining_Day'] = df['Joining_Date'].dt.day
df['Joining_Month_Name'] = df['Joining_Date'].dt.month_name()
df['Joining_Day_Name'] = df['Joining_Date'].dt.day_name()   
df['Joining_Quarter'] = df['Joining_Date'].dt.quarter
print(df[['Joining_Date', 'Joining_Year', 'Joining_Month', 'Joining_Day', 'Joining_Month_Name', 'Joining_Day_Name', 'Joining_Quarter']])    

# date filtering
# filter employees who joined after 2020-01-01
print(df[df['Joining_Date'] > '2020-01-01'])

# find employees who joined in 2021
print(df[df['Joining_Year'] == 2021])

# find employees who joined in January
print(df[df['Joining_Month'] == 1])

# find a data range
print(df[(df['Joining_Date'] >= '2020-01-01') & (df['Joining_Date'] <= '2021-12-31')])


# cal year of experience based on joining date and current date
df['Current_Date'] = pd.to_datetime('today')
df['Experience_Years'] = (df['Current_Date'] - df['Joining_Date']).dt.days // 365
print(df[['Joining_Date', 'Current_Date', 'Experience_Years']])

#-----------------------------------------------stage 8---------------------------------------------
# concat is used to combine two or more DataFrames along a particular axis (rows or columns).
# It can be used to merge datasets with similar structures or to append new data to an existing


salary_data = pd.DataFrame({
    "Employee_ID": ["E001", "E002", "E003", "E004", "E005"],
    "Bonus_2026": [6000, 5000, 9000, 3500, 7000]
})

department_data = pd.DataFrame({
    "Employee_ID": ["E001", "E002", "E003", "E004", "E005"],
    "Manager": [
        "Sanjay",
        "Lakshmi",
        "Ajay",
        "Gopal",
        "Mohan"
    ]
})

# CONCAT
df1 = pd.concat([salary_data, department_data], axis=1)
print(df1)
# axis=0 -> row wise
# axis=1 -> column wise

# you can reset the index of the concatenated DataFrame if needed

# merge is used to combine two DataFrames based on a common column or index. 
# It allows you to perform database-style joins (inner, outer, left, right) between datasets.

result = pd.merge(df, salary_data, on='Employee_ID')
print(result)

# JOINS : LEFT, RIGHT, INNER, OUTER
left_join = pd.merge(df, salary_data, on='Employee_ID', how='left')
print(left_join)

right_join = pd.merge(df, salary_data, on='Employee_ID', how='right')
print(right_join)

inner_join = pd.merge(df, salary_data, on='Employee_ID', how='inner')
print(inner_join)

outer_join = pd.merge(df, salary_data, on='Employee_ID', how='outer')
print(outer_join)


# PANDAS supports the merage using different column names 
employee_info = pd.DataFrame({
    "Employee_ID": ["E001", "E002", "E003"],
    "Name": ["Ravi", "Priya", "Arun"]
})

manager_info = pd.DataFrame({
    "Emp_ID": ["E001", "E002", "E003"],
    "Manager": ["Sanjay", "Lakshmi", "Ajay"]
})

result = pd.merge(employee_info, manager_info, left_on='Employee_ID', right_on='Emp_ID')
print(result)

# --------------------------------------------------- stage 9---------------------------------------------
# pivot table is a data summarization tool that allows you to reorganize and aggregate data in a tabular format.
# It can be used to calculate summary statistics, such as sums, averages, counts, and percentages, for different combinations of categorical variables. 
# pivot() → pivot_table() → melt() → set_index() → reset_index() → MultiIndex → rank() → shift() → rolling() → resample().
# syntax: pd.pivot_table(data, values=None, index=None, columns=None, aggfunc='mean', fill_value=None, margins=False, dropna=True, margins_name='All', observed=False)

result = pd.pivot_table(
    df,
    values='Salary',
    index='Department',
    columns='Gender',
    aggfunc='mean',
    fill_value=0
)
print(result)

# Why use pivot_table()?
# It is useful when you want to summarize data into a table for analysis.

# pivot() - rearranges data without perfoming aggregation. 
# It is used when you want to reshape the data without any calculations.
# example
small_df = df[["Department", "Gender", "Salary"]].dropna()
print(small_df)

# result = small_df.pivot(index='Department', columns='Gender', values='Salary')
# print(result)

# melt() - unpivots a DataFrame from wide format to long format.
# It is used when you want to transform the data from a wide format (multiple columns)

sales = pd.DataFrame({
    "Employee": ["A", "B", "C"],
    "Jan": [100, 200, 150],
    "Feb": [120, 210, 170],
    "Mar": [130, 220, 180]
})

print(sales)

long_sales = sales.melt(
    id_vars="Employee",
    var_name="Month",
    value_name="Sales"
)
print(long_sales)

# set_index() - sets the DataFrame index using one or more existing columns.
# It is used when you want to change the index of the DataFrame to a specific column

df_indexed = df.set_index("Employee_ID")

print(df_indexed.head())

# reset_index() - resets the index of the DataFrame to the default integer index.
# It is used when you want to revert the index back to the default integer index.
# convert the index back to a regular column
df_indexed = df_indexed.reset_index()
print(df_indexed.head())

# multiIndex - allows you to have multiple levels of indexing in a DataFrame.
# It is used when you want to represent hierarchical data or perform advanced indexing operations.

multi_index_df = df.set_index(["Department", "Gender"])
print(multi_index_df.head())

# rank() - assigns ranks to the values in a column or Series.
df['Salary_Rank'] = df['Salary'].rank(ascending=False)
print(df[['Salary', 'Salary_Rank']])

# shift() - shifts the values in a column or Series by a specified number of periods.
data = pd.DataFrame({
    "Month": ["Jan", "Feb", "Mar", "Apr"],
    "Sales": [1000, 1200, 1500, 1300]
})

data["Previous_Month_Sales"] = data["Sales"].shift(1)

print(data)

# rolling() - provides a moving window calculation on a Series or DataFrame.
data["Rolling_Avg_Sales"] = data["Sales"].rolling(window=2).mean
print(data)

# resample() - allows you to change the frequency of time series data.
# value_counts() - returns a Series containing counts of unique values in a column.
# nsmallest() - returns the n smallest values from a Series or DataFrame.
# nlargest() - returns the n largest values from a Series or DataFrame. 

#-------------------------------------------------------------------------------
# Reading data
# ↓
# Inspecting data
# ↓
# Selecting data
# ↓
# Filtering
# ↓
# Cleaning
# ↓
# Transforming
# ↓
# Grouping
# ↓
# Working with dates
# ↓
# Combining tables
# ↓
# Advanced analysis