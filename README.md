# 📊 Sales Data Analysis Project

## 📌 Overview

This project focuses on analyzing a real-world retail dataset (**Sample Superstore**) using **Python, Pandas, NumPy, and SQL (SQLite)** to extract meaningful business insights.

The goal is to perform **data cleaning, transformation, analysis, and visualization** to understand sales performance, customer trends, and product profitability.

---

## 🎯 Objectives

* Analyze overall sales and profit
* Identify top-performing products
* Understand region-wise performance
* Perform SQL-based data analysis

---

## 🧰 Technologies Used

* **Python **
* **Pandas**
* **NumPy**
* **SQLite (SQL)**
* **Matplotlib** (for visualization)

---

## 📂 Project Structure

```
sales-analysis-project/
│── data/
│   └── Sample-Superstore.csv
│── sql/
│   └── queries.sql
│── src/
│   └── main.py
│── screenshots/
│── sales.db
│── README.md
│── requirements.txt
```

---

## 🔍 Data Processing Steps

### 1️⃣ Data Cleaning

* Removed duplicate records
* Handled missing values
* Converted date columns to datetime format

### 2️⃣ Feature Engineering

* Created new columns:

  * Month, Year
  * Profit Status (Profit/Loss)
  * Delivery Days

### 3️⃣ Data Analysis

Performed analysis using Pandas:

* Total Sales & Profit
* Top 10 Products
* Sales by Region
* Monthly Sales Trends

---

## 🗄️ SQL Integration (SQLite)

The dataset is stored in a SQLite database (`sales.db`) and analyzed using SQL queries.

### Example Query:

```sql
SELECT Region, SUM(Sales) AS total_sales
FROM sales
GROUP BY Region;
```

---

## 📈 Key Insights

* 📌 West region generated the highest sales
* 📌 Technology category performed best
* 📌 Certain products consistently drive revenue
* 📌 Sales show variation across months

---

## 📸 Screenshots

(Add your screenshots in this section)

```
screenshots/
```

---

## ▶️ How to Run the Project

1. Clone the repository or download files
2. Install dependencies:

```
pip install pandas numpy matplotlib
```

3. Run the script:

```
python src/main.py
```

---

## 💡 Concepts Used

* Data Cleaning
* Data Transformation
* Exploratory Data Analysis (EDA)
* SQL Queries (GROUP BY, ORDER BY)
* Data Visualization

---

## 🚀 Future Improvements

* Add interactive dashboard (Streamlit / Power BI)
* Use larger real-world datasets
* Implement predictive analysis

---

## 🤝 Contribution

Contributions are welcome! Feel free to fork and improve the project.

---

## 📄 License

This project is for educational purposes.

---

## 👨‍💻 Author

**Yashraj Jani**

---

