import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Connect to the database
conn = sqlite3.connect('/Users/shreyajoshi/Downloads/Walmart_Sales_Insights/data/walmart_sales.db')

# Load the SalesClean table
df_clean = pd.read_sql_query("SELECT * FROM SalesClean", conn)

# Close the connection (we've loaded data into memory)
conn.close()

# Quick Overview
print("===== SalesClean Table Preview =====")
print(df_clean.head(10))
print("\n===== Table Info =====")
print(df_clean.info())
print("\n===== Summary Statistics =====")
print(df_clean.describe())

# Quick Visualization
sns.set_style("whitegrid")

# Top 10 products by total sales
top_products = df_clean.groupby('product_name')['total_sales'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,6))
sns.barplot(x=top_products.values, y=top_products.index, palette='viridis')
plt.title("Top 10 Products by Total Sales (SalesClean Table)")
plt.xlabel("Total Sales")
plt.ylabel("Product Name")
plt.tight_layout()
plt.show()
