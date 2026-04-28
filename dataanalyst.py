import pandas as pd
import matplotlib.pyplot as plt
import sqlite3
df = pd.read_csv("Sample-Superstore.csv")
#EDA
print(df.shape)
print(df.columns)
print(df.head())
print(df.info())
print(df.isnull().sum(0))
print(df.describe())

# data cleaning
print(df[df.duplicated()])
df.drop_duplicates(inplace=True)
df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

#data analysis
print("Total Sales:", df["Sales"].sum())
print("Total Profit:", df["Profit"].sum())
top10_product= df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10)
region_sales  =df.groupby("Region")["Sales"].sum()

print(top10_product)
print(region_sales)

#visulization using matplotlib 
df.groupby("Region")["Sales"].sum().plot(kind="bar")
plt.title("Sales by Region")
plt.show()
df.groupby("Order Date")["Sales"].sum().plot(kind="bar")
plt.title("Sales by order date")
plt.show()
df.groupby("Region")["Profit"].sum().plot(kind="bar")
plt.title("profit by Region")
plt.show()

#sql part
#creating database i am using currently sqllite but i have also knowledge of workbench

conn = sqlite3.connect("sales.db")
print("Database created successfully")
df.to_sql("sales", conn, if_exists="replace", index=False)
query = """
SELECT Region, SUM(Sales) as total_sales
FROM sales
GROUP BY Region
"""

result = pd.read_sql(query, conn)
print(result)

query2="""SELECT "Product Name", SUM(Sales) as total
FROM sales
GROUP BY "Product Name"
ORDER BY total DESC
LIMIT 5;
"""
result2 = pd.read_sql(query2,conn)
print(result2)

conn.close()

#final scripting
print("Total Sales:", df["Sales"].sum())
print("total profit:",df["Profit"].sum())
print("top state:")
print(df.groupby("State")["Sales"].sum().idxmax())
print("Top Region:")
print(df.groupby("Region")["Sales"].sum().idxmax())




