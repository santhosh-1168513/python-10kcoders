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
df['Salary'] = df['Salary'].fillna(df['Salary'].mean())
df['Age'] = df['Age'].fillna(df['Age'].mean())
df["City"] = df["City"].fillna("Unknown")
df["Performance"] = df["Performance"].fillna("Not Rated")
df['Experience'] = df['Experience'].fillna(df['Experience'].median())
print(df.isnull().sum())