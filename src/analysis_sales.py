import sqlite3, pandas as pd, os
from textblob import TextBlob

os.makedirs("outputs", exist_ok=True)

conn = sqlite3.connect("data/sales.db")
df = pd.read_sql("SELECT * FROM sales", conn, parse_dates=["date"])
conn.close()

# Monthly revenue
df["month"] = df["date"].dt.to_period("M")
monthly_revenue = df.groupby("month")["amount"].sum().reset_index()

# Top products
top_products = df.groupby("product")["amount"].sum().reset_index().sort_values("amount", ascending=False)

# Sentiment analysis
def get_sentiment(text):
    if not text or pd.isna(text):
        return "Neutral"
    polarity = TextBlob(text).sentiment.polarity
    if polarity > 0.1:
        return "Positive"
    elif polarity < -0.1:
        return "Negative"
    return "Neutral"

df["sentiment"] = df["feedback"].apply(get_sentiment)
sentiment_counts = df["sentiment"].value_counts().reset_index()
sentiment_counts.columns = ["sentiment", "count"]

# Export to Excel
with pd.ExcelWriter("outputs/sales_report.xlsx") as writer:
    df.to_excel(writer, sheet_name="Raw Data", index=False)
    monthly_revenue.to_excel(writer, sheet_name="Monthly Revenue", index=False)
    top_products.to_excel(writer, sheet_name="Top Products", index=False)
    sentiment_counts.to_excel(writer, sheet_name="Feedback Sentiment", index=False)

print("Analysis complete. See outputs/sales_report.xlsx")
