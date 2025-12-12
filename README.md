
---

## 🧹 Data Preparation & Cleaning

Key preprocessing steps performed in the notebook:

- Removed duplicates
- Converted date columns to datetime
- Separated returned/cancelled transactions
- Created new features:
  - `total_price`
  - `season`
  - `period` (Month)
  - `year`
  - `items_per_invoice`
- Filtered invalid quantities (≤ 0)
- Ensured consistent data types & indexing

---

## 📈 Dashboard Features

### 1️⃣ **KPI Overview**
- Total Revenue  
- Total Orders  
- Average Order Value (AOV)  
- Best Season  
- Best Product  

### 2️⃣ **Market Analysis**
- Revenue per Year  
- Year-over-Year Growth  
- Market Composition (Product Contribution %)  
- Revenue by Category  
- Market Health Metrics:
  - Average Basket Size  
  - Revenue per Customer  
  - Items per Customer  

### 3️⃣ **Season Analysis**
- Revenue per Season
- Interactive Season Filter
- Top Products by Season
- Auto-generated insights

### 4️⃣ **Product Performance**
- Top Revenue Products  
- Most Frequently Purchased Products  
- Highest AOV Products  
- Detailed Product Statistics Table  

---

## 📊 Insight Summary

- **Autumn** is the season contributing the highest revenue (+32%).
- Top performing product: **12 Egg House Painted Wood**, contributing ~**38%** of its season's revenue.
- Revenue shows clear monthly seasonality patterns.
- Certain product categories dominate revenue and require better inventory planning.
- Basket size and revenue per customer give strong indicators of market health.


---

## 🌐 Live Dashboard
> 🔗 [*Add your deployed Streamlit link here once uploaded*](https://data-anlaysis-uci-retail-ii-dataset-lzlsdxu7rhsl4tntkvpx3w.streamlit.app/)

## 📘 Notebook (EDA & Feature Engineering)
Link to the complete Jupyter notebook:  https://colab.research.google.com/drive/1ENwxlFXMoT4NphEWLO_QMsjhnv2uVCZf?usp=sharing
