# Step 1: Import pandas library
import pandas as pd

# Step 2: Load the CSV file into a pandas DataFrame
# Replace 'vegetable_prices_dataset.csv' with the correct path if needed
df = pd.read_csv('input/vegetable_prices_dataset.csv')

# Step 3: Display the first 5 rows of the dataset to get an overview
print("First 5 rows of the dataset:")
print(df.head())

# Step 4: Get basic information about the dataset (e.g., columns, data types, missing values)
print("\nBasic information about the dataset:")
print(df.info())

# Step 5: Get summary statistics for numerical columns (like Price_per_kg, Quantity_sold)
print("\nSummary statistics for numerical columns:")
print(df.describe())

# Step 6: Check for any missing values in the dataset
print("\nMissing values in the dataset:")
print(df.isnull().sum())

# Step 7: Count the number of unique vegetables in the dataset
print("\nNumber of unique vegetables:")
print(df['Vegetable'].nunique())

# Step 8: Display how many times each vegetable appears in the dataset
print("\nVegetable counts:")
print(df['Vegetable'].value_counts())

# Step 9: Sort the dataset by price in descending order
print("\nTop 5 most expensive vegetable records:")
print(df.sort_values(by='Price_per_kg', ascending=False).head())

# Step 10: Filter and display the rows where the price is greater than 80
print("\nVegetables with price per kg greater than 80:")
expensive_vegetables = df[df['Price_per_kg'] > 80]
print(expensive_vegetables)

# Step 11: Calculate the average price per kg for each vegetable
print("\nAverage price per kg for each vegetable:")
avg_price_per_vegetable = df.groupby('Vegetable')['Price_per_kg'].mean()
print(avg_price_per_vegetable)

# Step 12: Plot the average price per kg for each vegetable (requires matplotlib)
import matplotlib.pyplot as plt

avg_price_per_vegetable.plot(kind='bar', title='Average Price per kg of Vegetables')
plt.ylabel('Price (Rs)')
plt.xlabel('Vegetable')
plt.show()
