
# 🍬 Nassau Candy Distributor – Shipping Route Efficiency Analysis

## 📌 Project Overview

This project analyzes the factory-to-customer shipping operations of Nassau Candy Distributor.

The objective is to understand shipping lead times, route performance, regional patterns, factory contribution, ship modes, and product-level shipping activity.

The analysis combines Python-based data analysis with an interactive Streamlit dashboard.

---

## 🎯 Project Objectives

- Analyze overall shipping performance
- Calculate shipping lead time
- Compare shipping performance across factories
- Analyze regional shipping patterns
- Compare different ship modes
- Identify high-volume shipping routes
- Identify routes with higher average lead times
- Analyze product-level shipment activity
- Understand factory contribution to shipments, sales, and profit
- Provide an interactive dashboard for business users

---

## 📊 Key Analysis Areas

### 1. Shipping Lead Time
Shipping lead time is calculated as:

`Ship Date - Order Date`

### 2. Factory Analysis
The project compares shipping activity and lead time across the assigned factories.

### 3. Regional Analysis
Shipping performance is analyzed across different regions and states/provinces.

### 4. Ship Mode Analysis
The dashboard compares:
- Standard Class
- Second Class
- First Class
- Same Day

### 5. Route Analysis
Factory-to-customer routes are created using:

`Factory → State/Province`

Routes are analyzed based on:
- Shipment volume
- Average lead time
- Median lead time
- Lead-time variability

### 6. Product Analysis
Products are analyzed based on shipment volume and average shipping lead time.

---

## 🛠️ Tools & Technologies

- Python
- Pandas
- NumPy
- Streamlit
- Matplotlib
- Jupyter / Google Colab
- CSV Dataset

---

## 📁 Project Structure

```text
Nassau_Candy_Shipping_Analysis
│
├── data
│   └── Nassau_Candy_Cleaned.csv
│
├── analysis
│   ├── Ship_Mode_Analysis.csv
│   ├── Region_Analysis.csv
│   ├── Factory_Analysis.csv
│   ├── Route_Performance_Summary.csv
│   ├── Route_Risk_Analysis.csv
│   ├── High_Volume_Route_Analysis.csv
│   ├── Product_Factory_Analysis.csv
│   └── Factory_Contribution_Analysis.csv
│
├── dashboard
│   └── app.py
│
├── report
│
├── screenshots
│
├── requirements.txt
├── README.md
└── Nassau_Candy_Shipping_Analysis.ipynb
