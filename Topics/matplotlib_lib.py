import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

monthly_report = pd.DataFrame({
    'products':['cpu', 'gpu', 'ram', 'ssd', 'hdd', 'motherboard'],
    "months": ["January", "February", "March", "April", "May", "June"],
    'sales_2024': [200, 180, 300, 150, 500, 600],
    'sales_2023': [150, 200, 250, 100, 400, 550],
    'sales_2022': [100, 150, 200, 80, 300, 400]
})

# print(monthly_report)

# plot is a function that is used to create a line plot of the sales data over the months. 
# It takes the months as the x-axis and the sales as the y-axis. 
# The plot is then displayed using plt.show().

# plt.plot(monthly_report['months'], monthly_report['sales_2022'],
#          color='blue', marker='o', linestyle='--', linewidth=2, markersize=8,label='Sales 2022')

# plt.plot(monthly_report['months'], monthly_report['sales_2023'],
#          color='orange', marker='o', linestyle='--', linewidth=2, markersize=8,label='Sales 2023')

# plt.plot(monthly_report['months'], monthly_report['sales_2024'],
#          color='green', marker='o', linestyle='--', linewidth=2, markersize=8,label='Sales 2024')

# plt.legend()
# plt.title('year Sales Report')
# plt.xlabel('Months')
# plt.ylabel('Sales')
# plt.grid()
# plt.show()

# plt.plot(monthly_report['months'], monthly_report['sales'],
#             color='green', marker='o', linestyle='--', linewidth=2, markersize=8) 

#################################################################################################

# # take the employee data set and create a bar chart that shows the number of employees are hired every year. 

# data = pd.read_excel(
#     r"C:\Users\sivasankar\Downloads\Datasets\Employee_Dataset_India.xlsx"
# )
# # print(data.info())
# data['year'] = data['HireDate'].dt.year
# data['month'] = data['HireDate'].dt.month
# data=data[data['year'].isin([2018, 2019, 2020, 2021, 2022, 2023])]

# monthly_hires = data.groupby(['year', 'month']).size().unstack(fill_value=0)
# # print(monthly_hires)
# # print(monthly_hires.index)
# # print(monthly_hires.values)

# for year in monthly_hires.index:
#     plt.plot(monthly_hires.columns, monthly_hires.loc[year],
#               marker='o', label=str(year))

# plt.title('Monthly wise employee hiring', fontsize=14,fontweight='bold', color='blue')
# plt.xlabel('Months', fontsize=12,fontweight='bold', color='blue')
# plt.ylabel('Number of Employees Hired', fontsize=12,fontweight='bold', color='blue')
# plt.grid(True, linestyle='--', alpha=0.5, linewidth=0.5)
# plt.legend(loc='upper left', title='Year', title_fontsize=10, fontsize=10)
# plt.tight_layout()
# # plt.show()

# patten:
# 1. load the data
# 2. to display the data like head, tail, shape, columns, dtypes, index, info, describe, unique values
# 3. data cleaning, grouping, filtering
# 4. plot the data


# bar chart is a type of chart that represents data with rectangular bars. 
# The length of each bar is proportional to the value it represents.
#  Bar charts are used to compare different categories of data.

# plt.Bar(x, height, width=0.8, color = 'blue', edgecolor = 'black', linewidth = 1.5, alpha = 0.7, label = 'label_name', linestyle = '-')
#plt.xticks()
# plt.yticks()




# monthly_report = pd.DataFrame({
#     'products':['cpu', 'gpu', 'ram', 'ssd', 'hdd', 'motherboard'],
#     "months": ["January", "February", "March", "April", "May", "June"],
#     'sales_2024': [200, 180, 300, 150, 500, 600],
#     # 'sales_2023': [150, 200, 250, 100, 400, 550],
#     # 'sales_2022': [100, 150, 200, 80, 300, 400]
# })

# fig,ax = plt.subplots(figsize=(10,6))
# bars = ax.bar(monthly_report['products'], monthly_report['sales_2024'], color='blue', edgecolor='black', linewidth=1.5, alpha=0.7, label='Sales 2024')
# ax.bar_label(bars,padding=3, fontsize=10, color='black', fontweight='bold')
# ax.set_title('Sales Report for 2024', fontsize=14, fontweight='bold', color='blue')
# ax.set_xlabel('Products', fontsize=12, fontweight='bold', color='blue')
# ax.set_ylabel('Sales', fontsize=12, fontweight='bold', color='blue')
# ax.grid(axis='y', linestyle='--', alpha=0.5, linewidth=0.5)
# plt.tight_layout()
# plt.show()

# product by sales bar chart
# data = pd.read_excel(r'C:\Users\sivasankar\Downloads\Datasets\sales.xlsx')
# product_sales = data.groupby('Product Name')['Sales'].sum().sort_values(ascending=False).head(10)
# plt.figure(figsize=(10,6))

# product_sales.plot(kind='bar', color='skyblue', edgecolor='black', linewidth=1.5, alpha=0.7)
# plt.title('Total Sales by Product', fontsize=14, fontweight='bold', color='blue')
# plt.xlabel('Product Name', fontsize=12, fontweight='bold', color='blue')
# plt.ylabel('Total Sales', fontsize=12, fontweight='bold', color='blue')
# plt.xticks(rotation=45, ha='right')
# plt.grid(axis='y', linestyle='--', alpha=0.5, linewidth=0.5)
# plt.tight_layout()  
# plt.show()

####################################################################
# groupby and plot the data
monthly_report = pd.DataFrame({
    'products':['cpu', 'gpu', 'ram', 'ssd', 'hdd', 'motherboard'],
    "months": ["January", "February", "March", "April", "May", "June"],
    'sales_2024': [200, 180, 300, 150, 500, 600],
    'sales_2023': [150, 200, 250, 100, 400, 550],
    'sales_2022': [100, 150, 200, 80, 300, 400]
})

# x = np.arange(len(monthly_report['products']))
# width = 0.35
# fig, ax = plt.subplots(figsize=(10, 6))
# bar1 = ax.bar(x - width/2, monthly_report['sales_2024'], width, label='Sales 2024', color='blue', edgecolor='black', linewidth=1.5, alpha=0.7)
# bar2 = ax.bar(x + width/2, monthly_report['sales_2023'], width, label='Sales 2023', color='orange', edgecolor='black', linewidth=1.5, alpha=0.7)
# ax.bar_label(bar1, padding=3, fontsize=10, color='black', fontweight='bold')
# ax.bar_label(bar2, padding=3, fontsize=10, color='black', fontweight='bold')
# ax.set_title('Sales Report Comparison', fontsize=14, fontweight='bold', color='blue')
# # ax.set_xlabel('Products', fontsize=12, fontweight='bold', color='blue') 
# ax.set_xticks(x)
# ax.set_xticklabels(monthly_report['products'], rotation=45, ha='right',
#                    fontsize=10, fontweight='bold')
# ax.set_ylabel('Sales', fontsize=12, fontweight='bold', color='blue')
# # ax.set_xticks(x, labels=monthly_report['products'], rotation=45, ha='right')
# # ax.set_yticks(y, fontsize=10, color='black', fontweight='bold')
# # ax.grid(axis='y', linestyle='--', alpha=0.5, linewidth=0.5)
# ax.legend()
# plt.tight_layout()
# plt.show()

# task
# employee hired by department and salary groupby chart

# data = pd.read_csv(r"C:\Users\sivasankar\Downloads\python pratices\Topics\employees.csv")
# # print(data.info())
# data['Joining_Date'] = pd.to_datetime(data['Joining_Date'])
# data['year'] = data['Joining_Date'].dt.year

# hired_data = data.groupby(['Department', 'year']).size().unstack(fill_value=0)
# #pivotdata.plot(kind='bar', figsize=(10, 6), color=['blue', 'orange', 'green'], edgecolor='black', linewidth=1.5, alpha=0.7)
# pivotdata.plot(kind='bar', figsize=(10, 6), color=['blue', 'orange', 'green'], edgecolor='black', linewidth=1.5, alpha=0.7)
# plt.title('Number of Employees Hired by Department and Year', fontsize=14, fontweight='bold', color='blue')
# plt.xlabel('Department', fontsize=12, fontweight='bold', color='blue')
# plt.ylabel('Number of Employees Hired', fontsize=12, fontweight='bold', color='blue')
# plt.xticks(rotation=45, ha='right', fontsize=10, fontweight='bold')
# plt.grid(axis='y', linestyle='--', alpha=0.5, linewidth=0.5)
# plt.tight_layout()
# plt.show()

# import pandas as pd
# import matplotlib.pyplot as plt

# data = pd.read_csv(r"C:\Users\sivasankar\Downloads\python pratices\Topics\employees.csv")
# data = data.drop_duplicates(subset=['Name', 'Email'])
# data['Joining_Date'] = pd.to_datetime(data['Joining_Date'], errors='coerce')
# data['year'] = data['Joining_Date'].dt.year
# hired_data = data.groupby(['Department', 'year']).size().unstack(fill_value=0)
# pivotdata = data.pivot_table(index='Department', columns='year', values='Employee_ID', aggfunc='count', fill_value=0)
# pivotdata.plot(kind='bar', figsize=(10, 6), color=['blue', 'orange', 'green'], edgecolor='black', linewidth=1.5, alpha=0.7)

# plt.title('Number of Employees Hired by Department and Year', fontsize=14, fontweight='bold', color='blue')
# plt.xlabel('Department', fontsize=12, fontweight='bold', color='blue')
# plt.ylabel('Number of Employees Hired', fontsize=12, fontweight='bold', color='blue')
# plt.xticks(rotation=45, ha='right', fontsize=10, fontweight='bold')
# plt.grid(axis='y', linestyle='--', alpha=0.5, linewidth=0.5)
# plt.tight_layout()
# plt.show()

###############################################################################################################


###########################################################################################################@@#

#boxplot is a type of chart that shows the distribution of a dataset. It displays the minimum, first quartile, median, third quartile, and maximum values of the data. 
# Boxplots are useful for identifying outliers and understanding the spread of the data.
# plt.boxplot(x, notch=False, widths=0.5, patch_artist= True, labels=none, meanline=true, meanprops=None, showmeans=True, 

# data = pd.read_csv(r"C:\Users\sivasankar\Downloads\python pratices\Topics\employees.csv")
# print(data.info())

