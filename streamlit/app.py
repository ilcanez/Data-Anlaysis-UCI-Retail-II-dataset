import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


#header
st.title("Sales Performance Dashboard")

#load data
df = pd.read_csv(r"C:\Users\LEGION\Documents\!DAMAR\PROJECT\!Pribadi Project\DASHBOARD PROJECT\UCI RETAIL\data\final_retail_clean.csv")




# KPI Perhitungan Dasar
total_revenue = df['total_price'].sum()
total_orders = df['invoice'].nunique()
aov = df['total_price'].mean()

# Best season berdasarkan total revenue
best_season = df.groupby('season')['total_price'].sum().idxmax()

# Best product berdasarkan revenue tertinggi
best_product = df.groupby('description')['total_price'].sum().idxmax()


col1, col2, col3 = st.columns(3)
col4, col5 = st.columns(2)

col1.metric("Total Revenue", f"{total_revenue:,.0f}")
col2.metric("Total Orders", f"{total_orders}")
col3.metric("Average Order Value (AOV)", f"{aov:,.2f}")

col4.metric("Best Season", best_season)
col5.metric("Top Product", best_product)


#-------------------------------------------------------------
#monthly trend
df = df.set_index('invoicedate')
df.index = pd.to_datetime(df.index)

monthly_revenue = df['total_price'].resample('M').sum()
monthly_revenue = monthly_revenue.reset_index()
monthly_revenue.columns = ['Month', 'Revenue']

st.subheader("Monthly Revenue Trend")

st.line_chart(
    data=monthly_revenue,
    x='Month',
    y='Revenue'
)


# ==========================================
# 📈 MARKET ANALYSIS SECTION
# ==========================================

st.header("🌍 Market Analysis")

# convert invoice date
df_reset = df.reset_index()
df_reset["year"] = df_reset["invoicedate"].dt.year

# ==========================================
# ❤️ Market Health Metrics
# ==========================================

st.subheader("Market Health Metrics")

df_reset["items_per_invoice"] = df_reset.groupby("invoice")["quantity"].transform("sum")

# 1. Average Basket Size (items per transaction)
avg_basket_size = df_reset["items_per_invoice"].mean()

# 2. Revenue per customer
revenue_per_customer = df_reset.groupby("customer_id")["total_price"].sum().mean()

# 3. Items per customer
items_per_customer = df_reset.groupby("customer_id")["quantity"].sum().mean()

colA, colB, colC = st.columns(3)

colA.metric("Average Basket Size", f"{avg_basket_size:.2f} items/order")
colB.metric("Revenue per Customer", f"{revenue_per_customer:,.2f}")
colC.metric("Items per Customer", f"{items_per_customer:.2f}")

# ----- 1) Revenue per Year -----
yearly_revenue = df_reset.groupby("year")["total_price"].sum().reset_index()

st.subheader("Revenue per Year")
st.line_chart(
    data=yearly_revenue,
    x="year",
    y="total_price"
)

# ----- 2) Year-over-Year Growth -----
yearly_revenue["YoY Growth (%)"] = yearly_revenue["total_price"].pct_change() * 100

st.subheader("YoY Revenue Growth (%)")
st.bar_chart(
    data=yearly_revenue,
    x="year",
    y="YoY Growth (%)"
)

# insight
last_year = yearly_revenue.iloc[-1]["year"]
growth = yearly_revenue.iloc[-1]["YoY Growth (%)"]

st.info(
    f"""
### 📊 Market Growth Insight
- Tahun **{last_year}** mengalami pertumbuhan YoY sebesar **{growth:.2f}%**
- Jika growth positif → market berkembang  
- Jika negatif → perlu investigasi penurunan market
"""
)


# ----- 3) Revenue Share per Product -----
st.subheader("Market Composition: Revenue Share (%)")

product_share = (
    df_reset.groupby("description")["total_price"]
    .sum()
    .reset_index()
    .sort_values("total_price", ascending=False)
)

product_total = product_share["total_price"].sum()
product_share["percentage"] = (product_share["total_price"] / product_total) * 100

st.dataframe(product_share.head(10), use_container_width=True)



#-------------------------------------------------------------


# Revenue per Season
season_revenue = df.groupby("season")["total_price"].sum().reset_index()
season_revenue = season_revenue.sort_values("total_price", ascending=False)
st.header("🍂 Season Analysis")

st.subheader("Revenue per Season")
st.bar_chart(
    data=season_revenue,
    x="season",
    y="total_price",
)

#tombol pilih season
selected_season = st.selectbox(
    "Select Season", 
    season_revenue["season"].unique()
)

#ambil data season dipilih dan hitung produk terlaris
df_season = df[df["season"] == selected_season]

top_products_season = (
    df_season.groupby("description")["total_price"]
    .sum()
    .reset_index()
    .sort_values("total_price", ascending=False)
)

#menampilkan top produk pakai bar chart
st.bar_chart(
    data=top_products_season.head(10),
    x="description",
    y="total_price"
)

#insight
best_prod = top_products_season.iloc[0]["description"]
best_rev  = top_products_season.iloc[0]["total_price"]

st.info(
    f"""
### Insight for **{selected_season}**
- Season ini menghasilkan revenue **{season_revenue.set_index('season').loc[selected_season]['total_price']:,}**
- Produk terbaik pada season ini adalah **{best_prod}**
- Produk tersebut menyumbang **{best_rev:,}** revenue
    """
)

#top revenue products
st.header("📦 Product Analysis")

# Hitung Top Revenue Products
top_revenue_products = (
    df.groupby("description")["total_price"]
    .sum()
    .reset_index()
    .sort_values("total_price", ascending=False)
)

st.subheader("Top Revenue Products")
st.bar_chart(
    data=top_revenue_products.head(10),
    x="description",
    y="total_price"
)

#top frequency
# Frequency per product
top_frequency_products = (
    df.groupby("description")["invoice"]
    .nunique()
    .reset_index()
    .sort_values("invoice", ascending=False)
)

st.subheader("Most Frequently Purchased Products")
st.bar_chart(
    data=top_frequency_products.head(10),
    x="description",
    y="invoice"
)

#AOV
product_stats = (df.groupby('description').agg(
    revenue=('total_price','sum'),
    transactions=('invoice','nunique'),
    quantity=('quantity','sum')
))
product_stats['aov'] = product_stats['revenue']/product_stats['transactions']
product_stats = product_stats.sort_values('aov',ascending=False)

st.subheader("Highest AOV Products")
st.dataframe(product_stats.head(10), use_container_width=True)


