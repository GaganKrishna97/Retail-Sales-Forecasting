# 🛍️ Retail Sales Forecasting – Product Sales Prediction

This end-to-end project predicts retail store sales using historical transactional data. It includes EDA, hypothesis testing, XGBoost model training, Flask deployment, and a Tableau dashboard.

---

## 📌 Problem Statement

Retailers need accurate sales forecasts to optimize stock and plan operations. This project predicts daily sales based on features like store type, location, number of orders, and holidays.

---

## 🗃️ Dataset

The dataset includes:
- Store_Type, Location_Type, Region_Code
- Holiday (Yes/No), #Order, Sales
- Date (transformed into Month, Day, Weekday)

---

## 📊 EDA Insights

- Sales peaked in March and June
- Store Type S1 had the highest revenue
- Holidays significantly reduce sales
- Strong correlation between orders and sales

📊 [Tableau Dashboard](https://public.tableau.com/views/RetailSalesForecastingGaganKrishna/Dashboard1)

---

## 🧪 Hypothesis Testing

Used a t-test to test:
**Do holidays affect sales?**

- T-statistic: -66.18  
- p-value: 0.0000 ✅  
➡️ Sales drop significantly on holidays

---

## 🛠 Feature Engineering

- Extracted Month, Day, Weekday from Date
- One-hot encoded all categorical variables
- Dropped null/unused fields like Discount

---

## 🤖 Model Building

| Model             | MAE      | RMSE     | R²     |
|------------------|----------|----------|--------|
| Linear Regression| ₹3,915.78 | ₹5,376.24 | 0.91   |
| ✅ XGBoost        | ₹2,483.62 | ₹3,550.70 | **0.96** ✅

---

## 🌐 Flask Web App

A simple interface to predict daily sales from user inputs.

📂 Run with:  
```bash
python app.py
