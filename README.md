# Walmart Sales Insights

## Overview
End-to-end **SQL + Python data analysis project** on Walmart sales data.  
Imports raw CSV into a database, performs preprocessing and visualization in Python,  
and creates a clean SQL table ready for further analysis.

## Workflow
- **Import CSV into SQL Database**: Load `WalmartCleanData.csv` into a SQLite database as the `SalesRaw` table.  
  Clean numeric columns, convert dates, and handle missing values to ensure accurate database storage.  

- **Connect SQL to Python**: Use Python’s `sqlite3` library to connect to the database and fetch data.  
  This allows all preprocessing, analysis, and visualization to be performed programmatically and reproducibly.  

- **Python Processing & Visualization**: Clean data, calculate `total_sales`, and engineer relevant features for analysis.  
  Generate professional visualizations such as top products, sales trends over time, and category-wise sales distributions.  

- **Create Clean SQL Table**: Write the processed and enriched data back into the database as the `SalesClean` table.  
  This creates a ready-to-use clean dataset for further queries or reporting in SQL or Python.  

- **View & Explore Clean Data**: Preview the `SalesClean` table and perform quick analysis using Python.  
  Visualize top products and key metrics to validate the cleaned data and provide actionable insights.

## Key Features
- Full **SQL + Python workflow**  
- Handles missing values and cleans numeric & date columns  
- Professional visualizations with **Matplotlib** & **Seaborn**  
- Fully reproducible on any system using SQLite

## How to Run
1. Install dependencies:
```bash
pip install -r requirements.txt
