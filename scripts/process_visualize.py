import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Styling
sns.set_style("whitegrid")
plt.rcParams['figure.figsize'] = (12,6)

# Connect to SQL
conn = sqlite3.connect('/Users/shreyajoshi/Downloads/Walmart_Sales_Insights/data/walmart_sales.db')
df = pd.read_sql_query("SELECT * FROM SalesRaw", conn)

# Clean numeric columns
df['unit_price'] = pd.to_numeric(df['unit_price'], errors='coerce').fillna(0)
df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce').fillna(0)
df['total_sales'] = df['quantity'] * df['unit_price']
df['date'] = pd.to_datetime(df['date'], errors='coerce')

# Top 10 Products by Total Sales
top_products = df.groupby('product_name')['total_sales'].sum().sort_values(ascending=False).head(10)
sns.barplot(x=top_products.values, y=top_products.index, palette='viridis')
plt.title("Top 10 Products by Total Sales")
plt.xlabel("Total Sales")
plt.ylabel("Product Name")
plt.tight_layout()
plt.show()

# Total Sales Over Time
sales_over_time = df.groupby('date')['total_sales'].sum()
plt.figure(figsize=(14,5))
sales_over_time.plot(color='green', marker='o')
plt.title("Total Sales Over Time")
plt.xlabel("Date")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Sales by Category
category_sales = df.groupby('category')['total_sales'].sum().sort_values(ascending=False)
sns.barplot(x=category_sales.index, y=category_sales.values, palette='coolwarm')
plt.title("Total Sales by Category")
plt.xlabel("Category")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Quantity Sold Distribution
sns.histplot(df['quantity'], bins=20, kde=True, color='purple')
plt.title("Distribution of Quantity Sold")
plt.xlabel("Quantity")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

# Unit Price vs Total Sales Scatter
sns.scatterplot(data=df, x='unit_price', y='total_sales', hue='category', palette='tab10', alpha=0.7)
plt.title("Unit Price vs Total Sales by Category")
plt.xlabel("Unit Price")
plt.ylabel("Total Sales")
plt.tight_layout()
plt.show()

conn.close()
