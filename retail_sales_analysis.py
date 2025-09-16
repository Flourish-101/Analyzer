import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

sns.set(style="whitegrid")

df = pd.read_csv("supermarket_sales.csv")

print("First 5 rows of dataset:")
print(df.head(), "\n")

print("Dataset info:")
print(df.info(), "\n")

print("Summary statistics:")
print(df.describe(), "\n")

df['Date'] = pd.to_datetime(df['Date'])

print("Missing values in each column:")
print(df.isnull().sum(), "\n")

sales_by_branch = df.groupby('Branch')['Total'].sum()
print("Total Sales by Branch:")
print(sales_by_branch, "\n")

avg_sales_product = df.groupby('Product line')['Total'].mean()
print("Average Sales by Product Line:")
print(avg_sales_product, "\n")

payment_sales = df.groupby('Payment')['Total'].sum()
print("Revenue by Payment Method:")
print(payment_sales, "\n")

plt.figure(figsize=(6,4))
sns.barplot(x=sales_by_branch.index, y=sales_by_branch.values)
plt.title("Total Sales by Branch")
plt.ylabel("Sales")
plt.show()

plt.figure(figsize=(8,5))
sns.barplot(x=avg_sales_product.index, y=avg_sales_product.values)
plt.title("Average Sales by Product Line")
plt.ylabel("Average Sales")
plt.xticks(rotation=45)
plt.show()

plt.figure(figsize=(6,4))
sns.barplot(x=payment_sales.index, y=payment_sales.values)
plt.title("Revenue by Payment Method")
plt.ylabel("Revenue")
plt.show()

print("Insights")
print("1. Branch with highest total sales: ", sales_by_branch.idxmax())
print("2. Product line with highest average sales: ", avg_sales_product.idxmax())
print("3. Most popular payment method: ", payment_sales.idxmax())
