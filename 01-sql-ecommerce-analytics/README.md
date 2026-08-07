# 🛒 SQL E-Commerce Analytics

> **An end-to-end SQL analytics project that models an e-commerce database and answers real-world business questions using PostgreSQL. The project demonstrates advanced SQL techniques—including CTEs, Window Functions, Cohort Analysis, and Customer Segmentation—to generate actionable business insights.**

<p align="center">

![PostgreSQL](https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-025E8C?style=for-the-badge)
![Analytics](https://img.shields.io/badge/Business-Analytics-blue?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)

</p>

---

# 📌 Project Overview

Modern e-commerce businesses rely on data-driven decision-making to improve revenue, customer retention, and operational efficiency. This project simulates a real-world analytics environment by designing a normalized e-commerce database and solving business problems using advanced SQL.

The analysis covers customer behavior, sales performance, retention, lifetime value, churn risk, and product performance, providing insights that would typically support marketing, sales, and executive teams.

---

# 🎯 Business Objectives

The project aims to answer key business questions such as:

- Which products generate the highest revenue?
- Which customer segments contribute the most value?
- How well are customers being retained over time?
- Which regions drive the majority of sales?
- Which customers are at risk of churning?
- What are the month-over-month revenue trends?

---

# 🛠 Tech Stack

- PostgreSQL
- SQL
- SQLite (Notebook Support)
- Python
- Pandas
- Faker
- NumPy
- Jupyter Notebook

---

# 🗄 Database Schema

The project uses a normalized relational database consisting of four core tables:

```text
Customers
    │
Orders
    │
Order_Items
    │
Products
```

### Tables

- **customers** — Customer demographics and regional information
- **products** — Product catalog and categories
- **orders** — Order transactions and statuses
- **order_items** — Individual products purchased in each order

---

# 📂 Dataset

Synthetic but realistic business data generated using **Faker** and **NumPy**.

| Dataset | Records |
|----------|---------:|
| Customers | 500 |
| Products | 120 |
| Orders | 3,000 |
| Order Items | ~7,000 |

The data simulates purchasing patterns across multiple customer segments, product categories, and geographic regions.

---

# 📊 SQL Analysis

The project includes **15 business-focused SQL queries** covering:

- Revenue Analysis
- Customer Lifetime Value (CLV)
- Repeat Purchase Rate
- Customer Cohort Retention
- Product Performance
- Regional Sales Analysis
- Revenue Growth
- Churn Risk Identification
- Customer Segmentation

---

# 💻 SQL Concepts Demonstrated

- INNER JOIN & LEFT JOIN
- Common Table Expressions (CTEs)
- Window Functions
- Aggregate Functions
- CASE Statements
- GROUP BY & HAVING
- Date Functions
- Ranking Functions
- Subqueries

### Window Functions Used

- `RANK()`
- `ROW_NUMBER()`
- `LAG()`
- `NTILE()`

---

# 📈 Business Questions Solved

✔ Monthly Revenue & Order Trends

✔ Revenue by Region

✔ Top Selling Products

✔ Category Revenue Contribution

✔ Customer Lifetime Value Ranking

✔ Repeat Purchase Rate

✔ Monthly Cohort Retention Analysis

✔ Month-over-Month Revenue Growth

✔ Top Products by Category

✔ Customer Spend Quartiles

✔ Customers at Churn Risk (90+ Days Inactive)

---

# 📁 Repository Structure

```text
01-sql-ecommerce-analytics/
│
├── data/
│   ├── customers.csv
│   ├── products.csv
│   ├── orders.csv
│   └── order_items.csv
│
├── schema.sql
├── queries.sql
├── notebook.ipynb
├── _build_db.py
├── requirements.txt
└── README.md
```

---

# ▶️ Getting Started

## Option 1 — PostgreSQL (Recommended)

Create the database:

```bash
createdb ecommerce
```

Run the schema:

```bash
psql ecommerce -f schema.sql
```

Import the datasets:

```bash
psql ecommerce -c "\copy customers FROM 'data/customers.csv' DELIMITER ',' CSV HEADER;"
psql ecommerce -c "\copy products FROM 'data/products.csv' DELIMITER ',' CSV HEADER;"
psql ecommerce -c "\copy orders FROM 'data/orders.csv' DELIMITER ',' CSV HEADER;"
psql ecommerce -c "\copy order_items FROM 'data/order_items.csv' DELIMITER ',' CSV HEADER;"
```

Execute all analytical queries:

```bash
psql ecommerce -f queries.sql
```

---

## Option 2 — SQLite (Notebook Version)

Install dependencies:

```bash
pip install -r requirements.txt
```

Build the local database:

```bash
python _build_db.py
```

Launch Jupyter Notebook:

```bash
jupyter notebook notebook.ipynb
```

---

# 💡 Key Insights

The analysis revealed several important business insights:

- A small number of products and categories contribute a disproportionate share of total revenue.
- Customer retention declines significantly after the first purchase, highlighting opportunities for targeted engagement campaigns.
- High-value customers generate substantially higher lifetime value than the average customer, making loyalty initiatives especially impactful.
- Revenue distribution varies across regions, helping identify high-performing and underperforming markets.
- Approximately one-quarter of customers have been inactive for more than 90 days, representing a valuable audience for win-back campaigns.

---

# 🚀 Business Impact

This project demonstrates how SQL can be used to transform raw transactional data into actionable business intelligence by:

- Tracking revenue performance
- Identifying customer retention opportunities
- Measuring customer lifetime value
- Detecting churn risk
- Supporting executive decision-making through analytics

---

# 📦 Deliverables

- Normalized PostgreSQL Database
- SQL Schema (DDL)
- 15 Advanced SQL Queries
- Cohort Retention Analysis
- Customer Lifetime Value Analysis
- Revenue Analytics
- Churn Risk Identification
- SQLite-Compatible Notebook

---

# 🔮 Future Improvements

- Interactive Power BI Dashboard
- Customer Segmentation with RFM Analysis
- Sales Forecasting
- Inventory Analytics
- Stored Procedures & Views
- Query Performance Optimization
- PostgreSQL Materialized Views

---

# 👩‍💻 Author

**Nupur Jaiswal**

📧 **nupurjaiswal931@gmail.com**

💼 **https://linkedin.com/in/nupur-jaiswal**

🐙 **https://github.com/NJ024**

---

## ⭐ Support

If you found this project useful or learned something from it, consider giving the repository a **⭐ Star**.
