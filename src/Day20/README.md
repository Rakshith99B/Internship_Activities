
# 📊 Mini Project 1 — Exploratory Data Analysis (EDA)

## 📌 Project Overview
This project focuses on Exploratory Data Analysis (EDA) using Python libraries such as Pandas, NumPy, Matplotlib, and Seaborn.

The objective is to inspect, clean, visualize, and analyze a customer analytics dataset to discover meaningful patterns and relationships between variables.

Each row in the dataset represents a single customer record containing demographic and spending-related information.

---

## 📂 Project Structure

MiniProject1_EDA/
│
├── MiniProject1_EDA.ipynb
├── customer_analytics.csv
└── README.md

---

## ⚙️ Technologies Used

- Python 3.x
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Jupyter Notebook

---

## 🚀 Project Workflow

### 🔎 Phase 1 — Setup & Inspection
- Load dataset using Pandas
- Use df.head(), df.info(), df.describe()
- Understand structure, data types, and statistics

### 🧹 Phase 2 — Data Cleaning
- Check missing values using df.isnull().sum()
- Fill numerical columns with median
- Fill categorical columns with mode
- Remove duplicate rows

### 📈 Phase 3 — Univariate & Bivariate Analysis
Univariate plots:
- Age Distribution
- Annual Income Distribution
- Gender Distribution

Bivariate plots:
- Annual Income vs Spending Score
- Annual Income by Gender

### 🔗 Phase 4 — Multivariate Analysis
- Generate correlation matrix
- Visualize using Seaborn heatmap

---

## 📊 Executive Summary

1. Customer age and income show useful distribution patterns.
2. Spending behavior varies with income levels.
3. Correlation heatmap highlights relationships between numerical features.

---

## ▶️ How to Run

1. Install libraries:

pip install pandas numpy matplotlib seaborn

2. Run Jupyter Notebook:

jupyter notebook

3. Open MiniProject1_EDA.ipynb and Run All Cells.

---

## 👨‍💻 Author
Rakshith B
