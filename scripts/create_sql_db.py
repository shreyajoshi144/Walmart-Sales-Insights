import sqlite3
import pandas as pd
import os

# Load CSV
csv_file = '/Users/shreyajoshi/Downloads/Walmart_Sales_Insights/data/walmart_clean_data.csv'
df = pd.read_csv(csv_file)

# Standardize columns
df.columns = [col.strip().lower().replace(" ", "_") for col in df.columns]

# Rename columns if needed
rename_dict = {
    'product': 'product_name',
    'item': 'product_name',
    'category_name': 'category',
    'price': 'unit_price',
    'unitprice': 'unit_price'
}
df.rename(columns=rename_dict, inplace=True)

# Clean numeric columns
df['unit_price'] = df['unit_price'].astype(str).replace(r'[\$,]', '', regex=True).str.replace(',', '')
df['unit_price'] = pd.to_numeric(df['unit_price'], errors='coerce')
df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')
df.fillna({'unit_price': 0, 'quantity': 0}, inplace=True)

# Ensure database folder exists
db_path = '../data/walmart_sales.db'
os.makedirs(os.path.dirname(db_path), exist_ok=True)

# Connect to SQLite database
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Create table
cursor.execute('''
CREATE TABLE IF NOT EXISTS SalesRaw (
    date TEXT,
    product_name TEXT,
    category TEXT,
    quantity INTEGER,
    unit_price REAL
)
''')

# Insert CSV into SQL
for _, row in df.iterrows():
    cursor.execute('''
    INSERT INTO SalesRaw (date, product_name, category, quantity, unit_price)
    VALUES (?, ?, ?, ?, ?)
    ''', (row.get('date', ''), row.get('product_name', ''), row.get('category', ''),
          int(row.get('quantity', 0)), float(row.get('unit_price', 0))))

conn.commit()
print("SQL database 'walmart_sales.db' and table 'SalesRaw' created successfully!")
conn.close()
