import pandas as pd, sqlite3, os

os.makedirs("data", exist_ok=True)
conn = sqlite3.connect("data/sales.db")

df = pd.read_csv("data/sales.csv", parse_dates=["date"])
df.to_sql("sales", conn, if_exists="replace", index=False)

conn.close()
print("Loaded sales.csv into SQLite DB (data/sales.db)")
