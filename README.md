# Retail-Tax-Forecasting

# 📈 Retail Sales Tax Forecast App

An interactive forecasting web app to visualize and predict quarterly retail sales tax revenue by city and county using Facebook Prophet. Built using Streamlit and deployed locally (cloud optional).

![image](https://github.com/user-attachments/assets/fe0c6995-1b41-4fd2-8e68-1f80cea39ed6)

---

## 🚀 Features

- Forecasts sales tax revenue by **city & county**
- Allows users to select **forecast horizon** (1–8 quarters)
- Powered by **Facebook Prophet** for time series forecasting
- Clean visualizations using **Matplotlib**
- Includes **MAPE, MAE, RMSE, and R²** evaluation metrics (optional)

---

## 🧠 Problem Statement

Government analysts need to predict sales tax revenue to make informed budget and policy decisions. This tool provides a simple way to select any city-county pair and forecast quarterly revenue trends.

---

## 📊 Dataset

**Source:** Iowa Department of Revenue  
**File:** `Quarterly_Retail_Sales_Tax_Data_by_County_and_City.csv`  
**Fields Used:**
- `Quarter Ending` – Period of reporting
- `County` – County name
- `City` – City name
- `Computed Tax` – Retail sales tax collected

---

## 🔍 Forecasting Approach

**Model:** Facebook Prophet  
**Frequency:** Quarterly (`QE`)  
**Metrics Evaluated:**
- **MAPE** (Mean Absolute Percentage Error)
- **MAE** (Mean Absolute Error)
- **RMSE** (Root Mean Squared Error)
- **R² Score** (for goodness of fit)

---

## 💻 How to Run

```bash
# 1. Clone this repo
git clone https://github.com/your-username/retail-forecast-app.git
cd retail-forecast-app

# 2. Install dependencies
pip install -r requirements.txt

# 3. Run the app
streamlit run streamlit_app.py
