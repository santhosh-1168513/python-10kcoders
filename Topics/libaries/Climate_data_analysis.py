'''
Climate Data Analysis
Main tasks
Load & Inspect
--Shape
--Data types
--Missing values
--Weather categories
--Seasons

Basic Statistics
--Mean, minimum, maximum and standard deviation of temperature
--Precipitation statistics
--Count rainy and snow days
--Hottest and coldest days

Grouped Analysis
--Average temperature by month
--Total rainfall by month
--Average temperature by season
--Total rainfall by season
--Percentage of each weather type

Required Visualizations
--Temperature over time
--Histogram + KDE of precipitation
--Temperature distribution
--Correlation heatmap
--Box/violin plot by season
--Pairplot
--Weather-category bar/count plot
'''
# load libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# load and inspect the dataset
df = pd.read_csv(r"C:\Users\sivasankar\Downloads\Datasets\weather_seattle_student_dataset.csv")
print(df.head())
print(df.info())
print(df.describe())
print("shape of the dataset:", df.shape)
print("data types of the dataset:", df.dtypes)
print("coloumns of the dataset:", df.columns)
print("missing values", df.isnull().sum())
print("duplicated values", df.duplicated().sum())
print("unique values in weather column", df['weather'].unique())
print("unique values in season column", df['season'].unique())
print("unique values in percipitation column", df['precipitation'].unique())
print("check the season column values", df['season'].value_counts())
df['date'] = pd.to_datetime(df['date'])
print(df.dtypes)
print("start date:", df['date'].min())
print("end date:", df["date"].max())
print("total number of days in the dataset:", (df['date'].max() - df['date'].min()).days)

#---------------------------------------------------------------------------

# Basic statistics
# to get the summary
print(df[["temp_max", "temp_min", "temp_avg"]].describe())
print(df[["precipitation"]].describe())
print(df['wind'].describe())

# mean temperature
max_temp = df['temp_max'].mean()
min_temp = df['temp_min'].mean()
avg_temp = df['temp_avg'].mean()
print("mean of max_temp, min_temp, avg_temp", max_temp, min_temp, avg_temp)

# rainy days
rainy_days = df['is_rainy'].sum()
print("total rainy days:", rainy_days)

# snow days
snow_days = (df["weather"] == "snow").sum()
print("Total Snow Days:", snow_days)

# weather count
print("weather count:", df['weather'].value_counts())

# HOTTEST DAY
hottest_day = df.loc[df['temp_max'].idxmax()]
print(hottest_day[['date', 'temp_max']])

# COLDEST DAY
coldest_day = df.loc[df['temp_min'].idxmin()]
print(coldest_day[['date', 'temp_min']])

#-------------------------------------------------------------------------

# group analysis
# month average temperature
month_avg_temp = df.groupby(df['date'].dt.month_name())['temp_avg'].mean()
print("Average temperature by month:", month_avg_temp)

# total rainfall by month
month_total_rainfall = df.groupby(df['date'].dt.month_name())['precipitation'].sum()
print("Total rainfall by month:", month_total_rainfall)

# average temperature by season
season_avg_temp = df.groupby('season')['temp_avg'].mean()
print("Average temperature by season:", season_avg_temp)

# Total rainfall by season
season_rainfall = df.groupby('season')['precipitation'].sum()
print("Total rainfall by season:", season_rainfall)

# weather type percentage
weather_percentage = df['weather'].value_counts(normalize=True)*100
print("Percentage of each weather type:", weather_percentage)   

# sort months corrrectly
monthly_temp = (df.groupby(['month', 'month_name'])['temp_avg'].mean().reset_index())
print(monthly_temp)

monthly_rainfall = (df.groupby(["month", "month_name"])["precipitation"].sum().sort_index().reset_index())
print(monthly_rainfall)

#--------------------------------------------------------------------------
# charts
import matplotlib.pyplot as plt

# temperature over time
plt.figure(figsize=(12, 6))
plt.plot(df['date'], df['temp_avg'], color='orange')
plt.title('Average Temperature Over Time')
plt.xlabel('Date')
plt.ylabel('Average Temperature (°C)')
plt.xticks(rotation=45)
plt.grid()
plt.tight_layout()
plt.show()

# precipitation distribution
plt.figure(figsize=(12, 6))
plt.hist(df['precipitation'], bins=30, color='blue', alpha=0.7)
plt.title('Precipitation Distribution')
plt.xlabel('Precipitation (mm)')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()

# temperature distribution
plt.figure(figsize=(12, 6))
plt.hist(df['temp_avg'], bins=30, color='green', alpha=0.7)
plt.title('Temperature Distribution')
plt.xlabel('Average Temperature (°C)')
plt.ylabel('Frequency')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()

# correlation heatmap
correlation_columns = ['temp_max', 'temp_min', 'temp_avg', 'precipitation', 'wind']
correlation_matrix = df[correlation_columns].corr()
plt.figure(figsize=(10, 8))
plt.imshow(correlation_matrix, cmap='coolwarm', interpolation='none')
plt.colorbar(label='Correlation Coefficient')
plt.xticks(range(len(correlation_columns)), correlation_columns, rotation=45)
plt.yticks(range(len(correlation_columns)), correlation_columns)
plt.title('Correlation Heatmap')
plt.tight_layout()
for i in range(len(correlation_columns)):
    for j in range(len(correlation_columns)):
        plt.text(j, i, f"{correlation_matrix.iloc[i, j]:.2f}", ha='center', va='center', color='black')
plt.show()


# temperature boxplot by season
seasons = ["Winter", "Spring", "Summer", 'Autumn']
season_data = [df[df['season'] == season]['temp_avg'] for season in seasons]
plt.figure(figsize=(10, 6))
plt.boxplot(season_data, tick_labels=seasons)
plt.title('Temperature Distribution by Season')
plt.xlabel('Season')
plt.ylabel('Average Temperature (°C)')
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()

# weather category bar plot
weather_counts = df['weather'].value_counts()
plt.figure(figsize=(10, 6))
plt.bar(weather_counts.index, weather_counts.values, color='skyblue')
plt.title('Weather Category Counts')
plt.xlabel('Weather Category')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()
plt.show()

# dashboard
plt.figure(figsize=(18, 12))

# 1. Temperature Over Time
plt.subplot(2, 3, 1)

plt.plot(df["date"], df["temp_avg"])

plt.title("Average Temperature Over Time")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.xticks(rotation=45)


# 2. Precipitation Distribution
plt.subplot(2, 3, 2)

plt.hist(df["precipitation"], bins=30, edgecolor="black")

plt.title("Distribution of Precipitation")
plt.xlabel("Precipitation (mm)")
plt.ylabel("Number of Days")


# 3. Temperature Distribution
plt.subplot(2, 3, 3)

plt.hist(df["temp_avg"], bins=30, edgecolor="black")

plt.title("Distribution of Average Temperature")
plt.xlabel("Temperature (°C)")
plt.ylabel("Number of Days")


# 4. Correlation Heatmap
plt.subplot(2, 3, 4)

correlation_columns = [
    "precipitation",
    "temp_max",
    "temp_min",
    "temp_avg",
    "wind"
]

correlation_matrix = df[correlation_columns].corr()

plt.imshow(
    correlation_matrix,
    cmap="coolwarm",
    aspect="auto"
)

plt.colorbar()

plt.xticks(
    range(len(correlation_columns)),
    correlation_columns,
    rotation=45
)

plt.yticks(
    range(len(correlation_columns)),
    correlation_columns
)

for i in range(len(correlation_columns)):
    for j in range(len(correlation_columns)):
        plt.text(
            j,
            i,
            round(correlation_matrix.iloc[i, j], 2),
            ha="center",
            va="center"
        )

plt.title("Correlation Heatmap")


# 5. Temperature by Season
plt.subplot(2, 3, 5)

seasons = ["Winter", "Spring", "Summer", "Autumn"]

season_data = [
    df[df["season"] == season]["temp_avg"]
    for season in seasons
]

plt.boxplot(
    season_data,
    tick_labels=seasons
)

plt.title("Temperature by Season")
plt.xlabel("Season")
plt.ylabel("Temperature (°C)")


# 6. Weather Categories
plt.subplot(2, 3, 6)

weather_counts = df["weather"].value_counts()

plt.bar(
    weather_counts.index,
    weather_counts.values,
    edgecolor="black"
)

plt.title("Weather Categories")
plt.xlabel("Weather")
plt.ylabel("Number of Days")


plt.suptitle("Seattle Weather Analysis Dashboard", fontsize=16)

plt.tight_layout()

plt.show()