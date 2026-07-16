# SQL E-commerce Analytics

Normalized `customers` / `products` / `orders` / `order_items` schema, analyzed with 15 SQL
queries covering revenue, cohort retention, repeat-purchase rate, and top-product/region
breakdowns — built for a mock stakeholder brief.

## Why this project
E-commerce analytics is one of the most common real-world SQL use cases: multiple related
tables, questions that need CTEs and window functions (not just `GROUP BY`), and results a
non-technical stakeholder actually cares about (revenue, retention, churn risk).

## Data
Synthetic but realistic data generated with Faker/NumPy (`/data/*.csv`):
- `customers.csv` — 500 customers across 5 regions
- `products.csv` — 120 products across 6 categories
- `orders.csv` — 3,000 orders (Completed / Cancelled / Returned)
- `order_items.csv` — ~7,000 line items

## Files
| File | Purpose |
|---|---|
| `schema.sql` | PostgreSQL DDL — run this first |
| `queries.sql` | 15 analytical queries (CTEs, window functions: `RANK`, `LAG`, `ROW_NUMBER`, `NTILE`) |
| `_build_db.py` | Builds a local `ecommerce.db` SQLite file from the CSVs, for quick local testing |
| `notebook.ipynb` | Runs SQLite-adapted versions of the queries and visualizes the results |

## How to run
**Option A — PostgreSQL (what the queries are written for):**
```bash
createdb ecommerce
psql ecommerce -f schema.sql
psql ecommerce -c "\copy customers FROM 'data/customers.csv' DELIMITER ',' CSV HEADER;"
psql ecommerce -c "\copy products FROM 'data/products.csv' DELIMITER ',' CSV HEADER;"
psql ecommerce -c "\copy orders FROM 'data/orders.csv' DELIMITER ',' CSV HEADER;"
psql ecommerce -c "\copy order_items FROM 'data/order_items.csv' DELIMITER ',' CSV HEADER;"
psql ecommerce -f queries.sql
```

**Option B — SQLite (zero setup, used by the notebook):**
```bash
pip install -r requirements.txt
python3 _build_db.py        # builds ecommerce.db from the CSVs
jupyter notebook notebook.ipynb
```

## Key queries covered
- Monthly revenue & order count
- Revenue by region, top 10 products, category revenue share
- Customer lifetime value ranked with `RANK()`
- Repeat purchase rate
- Monthly cohort retention (signup-month cohort × active month)
- Month-over-month revenue growth with `LAG()`
- Top 3 products per category with `ROW_NUMBER()`
- Customers at churn risk (90+ days since last order)
- Customer spend quartiles with `NTILE(4)`

## Findings
See the notebook for the full run — headline results: a small number of regions/product
categories drive most of revenue, retention drops off sharply after the first purchase month,
and roughly a quarter of the customer base has gone quiet (90+ days since last order) —
a clear win-back target list.
