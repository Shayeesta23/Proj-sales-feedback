import streamlit as st, pandas as pd, sqlite3, seaborn as sns
import matplotlib.pyplot as plt

st.title("Sales & Feedback Dashboard")

# Load data
conn = sqlite3.connect("data/sales.db")
df = pd.read_sql("SELECT * FROM sales", conn, parse_dates=["date"])
conn.close()

# Monthly revenue
df["month"] = df["date"].dt.to_period("M")
monthly_revenue = df.groupby("month")["amount"].sum().reset_index()

st.subheader("Monthly Revenue")
st.line_chart(monthly_revenue.set_index("month"))

# Top products
st.subheader("Top Products")
top_products = df.groupby("product")["amount"].sum().reset_index().sort_values("amount", ascending=False)
st.bar_chart(top_products.set_index("product"))

# Feedback sentiment
st.subheader("Customer Feedback Sentiment")
sentiment_counts = df["sentiment"].value_counts().reset_index()
sentiment_counts.columns = ["sentiment", "count"]
st.bar_chart(sentiment_counts.set_index("sentiment"))

# Raw preview
st.subheader("Sample Data")
st.write(df.head())
