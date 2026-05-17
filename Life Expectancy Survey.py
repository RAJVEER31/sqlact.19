#You are a part of a survey team trying to analyze the life expectancy of different categories. A dataset of Life Expectancy for different countries for the year 2007 is provided to you. Various features may be a responsible factor for different life expectancies.
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
#Load the dataset
data = pd.read_csv('gapminder(2007).csv')
#Display the first few rows of the dataset
print(data.head())
#Summary statistics of the dataset
print(data.describe())
#Check for missing values
print(data.isnull().sum())
#Correlation matrix
correlation_matrix = data.select_dtypes(include="number").corr()
plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm')
plt.title('Correlation Matrix of Life Expectancy Dataset')
plt.show()
#Scatter plot of Life Expectancy vs GDP per Capita
plt.figure(figsize=(10, 6))
sns.scatterplot(x='population', y='life_exp', data=data)
plt.title('Life Expectancy vs GDP per Capita')
plt.xlabel('GDP per Capita')
plt.ylabel('Life Expectancy')
plt.xscale('log')
plt.show()
#Box plot of Life Expectancy by Continent
plt.figure(figsize=(10, 6))
sns.boxplot(x='continent', y='life_exp', data=data)
plt.title('Life Expectancy by Continent')
plt.xlabel('Continent')
plt.ylabel('Life Expectancy')
plt.show()
