import sqlite3
import pandas as pd
import os

d = os.path.dirname(os.path.abspath(__file__))
conn = sqlite3.connect(f"{d}/ecommerce.db")

for table in ["customers", "products", "orders", "order_items"]:
    df = pd.read_csv(f"{d}/data/{table}.csv")
    df.to_sql(table, conn, if_exists="replace", index=False)

conn.commit()
conn.close()
print("ecommerce.db built.")
