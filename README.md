# 🛍️ Retail Sales Forecasting – Product Sales Prediction Project

This project focuses on building a robust machine learning model to forecast retail product sales using historical transactional data. The final output is a deployed Flask web app and an interactive Tableau dashboard.

---

## 📌 Problem Statement

The goal is to accurately predict **Sales** based on inputs like:
- Store Type
- Location Type
- Region Code
- Number of Orders
- Date-related features (Month, Day, Weekday)
- Holiday flag

---

## 📊 Exploratory Data Analysis (EDA)

- Clear monthly trends in sales
- Store Type S1 & S4 dominate overall sales
- Significant drop in sales observed on holidays
- Strong correlation between orders and sales

📈 [📊 Tableau Dashboard](https://public.tableau.com/views/RetailSalesForecastingGaganKrishna/Dashboard1)

---

## 🧪 Hypothesis Testing

- ✅ Holidays have a **statistically significant** impact on sales  
- T-test p-value < 0.05 confirms reduced sales during holidays

---

## 🤖 Model Building

Models tried:
- Linear Regression (R² = 0.91)
- ✅ XGBoost Regressor (R² = 0.96) → **Best performer**

### 🔍 Final Metrics (XGBoost):
- **MAE** = ₹2,483.62  
- **RMSE** = ₹3,550.70  
- **R²** = 0.9627

---

## 💻 Flask Web App

Built a lightweight Flask app to predict sales from form inputs.

🔗 [Demo Video (Loom)](YOUR_LOOM_LINK_HERE)

---

## 📦 Deployment Code

- `app.py` – Flask backend
- `index.html` – UI
- `best_sales_model.pkl` – saved model file
- `sales_forecasting_notebook.ipynb` – full EDA + training

---

## 📎 Links

- 🔗 [🧠 Medium Blog]([YOUR_MEDIUM_BLOG_LINK_HERE](https://medium.com/@tryhardggn/forecasting-retail-sales-7efc15d3a5aa))
- 🔗 [📊 Tableau Dashboard](https://public.tableau.com/views/RetailSalesForecastingGaganKrishna/Dashboard1)
- 🔗 [💻 Live Flask Code](GITHUB_LINK_HERE)
- 🔗 [🧠 DataSciencePortfolio.io (Optional)](YOUR_DSP_LINK)

---

## 🙌 Author

**Gagan Krishna**  
Built as part of a Data Science Portfolio Module  
