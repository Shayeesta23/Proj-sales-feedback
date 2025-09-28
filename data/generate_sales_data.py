import pandas as pd, numpy as np, os
from datetime import datetime, timedelta
import random

os.makedirs("data", exist_ok=True)

# Generate sales data
dates = pd.date_range("2023-01-01", "2023-12-31")
products = ["Laptop", "Phone", "Tablet", "Headphones"]
customers = [f"CUST{i:03d}" for i in range(1, 51)]

sales = []
feedback_options = [
    "Great product!", "Not worth the price.", "Excellent service.",
    "Quality could be better.", "Super happy with this purchase.",
    "Delivery was late.", "Fantastic experience.", "Will not buy again."
]

for date in dates:
    for _ in range(np.random.randint(5, 20)): # daily transactions
        product = random.choice(products)
        customer = random.choice(customers)
        amount = round(np.random.uniform(100, 2000), 2)
        feedback = random.choice(feedback_options) if random.random() < 0.3 else "" # 30% leave feedback
        sales.append([date, product, customer, amount, feedback])

df = pd.DataFrame(sales, columns=["date", "product", "customer", "amount", "feedback"])
df.to_csv("data/sales.csv", index=False)

print("Created data/sales.csv")
