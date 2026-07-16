"""
Generates realistic synthetic datasets for every project in the portfolio.
Seeded for reproducibility. Run once: python3 generate_datasets.py
"""
import numpy as np
import pandas as pd
from faker import Faker
import random
import os

np.random.seed(42)
random.seed(42)
fake = Faker()
Faker.seed(42)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---------------------------------------------------------------
# 01. SQL E-COMMERCE ANALYTICS — customers, products, orders, order_items
# ---------------------------------------------------------------
d = f"{ROOT}/01-sql-ecommerce-analytics/data"

n_customers = 500
regions = ["North", "South", "East", "West", "Central"]
signup_dates = pd.date_range("2022-01-01", "2023-12-31", periods=n_customers)
customers = pd.DataFrame({
    "customer_id": range(1, n_customers + 1),
    "customer_name": [fake.name() for _ in range(n_customers)],
    "email": [fake.email() for _ in range(n_customers)],
    "region": np.random.choice(regions, n_customers, p=[0.25, 0.2, 0.2, 0.2, 0.15]),
    "signup_date": np.random.choice(signup_dates, n_customers),
})
customers.to_csv(f"{d}/customers.csv", index=False)

categories = ["Electronics", "Home & Kitchen", "Fashion", "Sports", "Books", "Beauty"]
n_products = 120
base_price = {"Electronics": 3500, "Home & Kitchen": 1200, "Fashion": 800,
              "Sports": 1500, "Books": 350, "Beauty": 600}
products = pd.DataFrame({
    "product_id": range(1, n_products + 1),
    "product_name": [f"{fake.word().capitalize()} {c[:4]}" for c in
                      np.random.choice(categories, n_products)],
    "category": np.random.choice(categories, n_products),
})
products["unit_price"] = products["category"].map(base_price) * np.random.uniform(0.6, 1.8, n_products)
products["unit_price"] = products["unit_price"].round(2)
products.to_csv(f"{d}/products.csv", index=False)

n_orders = 3000
order_dates = pd.date_range("2022-01-01", "2023-12-31", periods=n_orders)
orders = pd.DataFrame({
    "order_id": range(1, n_orders + 1),
    "customer_id": np.random.choice(customers["customer_id"], n_orders),
    "order_date": np.random.choice(order_dates, n_orders),
    "status": np.random.choice(["Completed", "Cancelled", "Returned"], n_orders, p=[0.85, 0.08, 0.07]),
})
orders.to_csv(f"{d}/orders.csv", index=False)

n_items = 7000
order_items = pd.DataFrame({
    "order_item_id": range(1, n_items + 1),
    "order_id": np.random.choice(orders["order_id"], n_items),
    "product_id": np.random.choice(products["product_id"], n_items),
    "quantity": np.random.randint(1, 5, n_items),
})
order_items = order_items.merge(products[["product_id", "unit_price"]], on="product_id")
order_items["line_total"] = (order_items["quantity"] * order_items["unit_price"]).round(2)
order_items.drop(columns=["unit_price"], inplace=True)
order_items.to_csv(f"{d}/order_items.csv", index=False)

# ---------------------------------------------------------------
# 02. GLOBAL LAYOFFS ANALYSIS — intentionally messy
# ---------------------------------------------------------------
d = f"{ROOT}/02-global-layoffs-analysis/data"
companies = ["Meta", "Amazon", "Google", "Microsoft", "Twitter", "Netflix", "Shopify",
             "Uber", "Salesforce", "IBM", "Intel", "Spotify", "Snap", "Peloton", "Stripe"]
industries = ["Consumer", "Retail", "Transportation", "Finance", "Crypto", "Healthcare",
              "Media", "Hardware", "Other", "Food"]
countries = ["United States", "United States ", "USA", "India", "United Kingdom", "UK",
             "Germany", "Canada", "Brazil", "Sweden"]
n = 500
rows = []
for i in range(n):
    company = np.random.choice(companies)
    total_laid_off = np.random.choice([np.nan, np.random.randint(20, 8000)], p=[0.08, 0.92])
    pct = np.random.choice([np.nan, round(np.random.uniform(0.02, 0.6), 2)], p=[0.15, 0.85])
    import datetime as _dt
    date = fake.date_between(start_date=_dt.date(2022, 1, 1), end_date=_dt.date(2024, 6, 30))
    rows.append({
        "company": np.random.choice([company, company.upper(), f" {company}"]),
        "industry": np.random.choice(industries),
        "total_laid_off": total_laid_off,
        "percentage_laid_off": pct,
        "date": date.strftime(np.random.choice(["%Y-%m-%d", "%m/%d/%Y", "%d-%m-%Y"])),
        "country": np.random.choice(countries),
        "stage": np.random.choice(["Post-IPO", "Series C", "Series D", "Private Equity", "Series B", np.nan], p=[0.4,0.15,0.1,0.1,0.15,0.1]),
        "funds_raised_millions": np.random.choice([np.nan, round(np.random.uniform(5, 3000), 1)], p=[0.2, 0.8]),
    })
layoffs = pd.DataFrame(rows)
# inject some exact duplicates on purpose (messy real-world data)
layoffs = pd.concat([layoffs, layoffs.sample(15, random_state=1)], ignore_index=True)
layoffs.to_csv(f"{d}/layoffs_raw.csv", index=False)

# ---------------------------------------------------------------
# 03. A/B TEST — landing page conversion
# ---------------------------------------------------------------
d = f"{ROOT}/03-ab-test-hypothesis-testing/data"
n_a, n_b = 4200, 4150
group_a = pd.DataFrame({
    "user_id": range(1, n_a + 1),
    "group": "control",
    "converted": np.random.binomial(1, 0.112, n_a),
    "session_duration_sec": np.random.gamma(2.0, 60, n_a).round(1),
    "device": np.random.choice(["mobile", "desktop", "tablet"], n_a, p=[0.6, 0.32, 0.08]),
})
group_b = pd.DataFrame({
    "user_id": range(n_a + 1, n_a + n_b + 1),
    "group": "treatment",
    "converted": np.random.binomial(1, 0.131, n_b),
    "session_duration_sec": np.random.gamma(2.15, 62, n_b).round(1),
    "device": np.random.choice(["mobile", "desktop", "tablet"], n_b, p=[0.6, 0.32, 0.08]),
})
ab = pd.concat([group_a, group_b], ignore_index=True).sample(frac=1, random_state=1).reset_index(drop=True)
ab.to_csv(f"{d}/ab_test_data.csv", index=False)

# ---------------------------------------------------------------
# 04. HOUSE PRICE PREDICTION
# ---------------------------------------------------------------
d = f"{ROOT}/04-house-price-prediction/data"
n = 1500
area = np.random.normal(1800, 650, n).clip(400, 6000)
bedrooms = np.clip(np.round(area / 500 + np.random.normal(0, 0.7, n)), 1, 6)
bathrooms = np.clip(np.round(bedrooms * 0.75 + np.random.normal(0, 0.5, n)), 1, 5)
age = np.random.randint(0, 45, n)
city_tier = np.random.choice([1, 2, 3], n, p=[0.3, 0.45, 0.25])
distance_to_city_km = np.random.exponential(8, n).clip(0.2, 45)
has_garage = np.random.binomial(1, 0.6, n)
tier_multiplier = {1: 1.6, 2: 1.15, 3: 0.85}
price = (
    area * 1450 * pd.Series(city_tier).map(tier_multiplier).values
    + bedrooms * 95000
    + bathrooms * 60000
    - age * 3200
    - distance_to_city_km * 4800
    + has_garage * 180000
    + np.random.normal(0, 220000, n)
).clip(min=350000)
houses = pd.DataFrame({
    "area_sqft": area.round(0).astype(int),
    "bedrooms": bedrooms.astype(int),
    "bathrooms": bathrooms.astype(int),
    "age_years": age,
    "city_tier": city_tier,
    "distance_to_city_km": distance_to_city_km.round(1),
    "has_garage": has_garage,
    "sale_price": price.round(0).astype(int),
})
houses.to_csv(f"{d}/house_prices.csv", index=False)

# ---------------------------------------------------------------
# 05. LOAN APPROVAL PREDICTION
# ---------------------------------------------------------------
d = f"{ROOT}/05-loan-approval-prediction/data"
n = 2000
income = np.random.lognormal(10.8, 0.5, n).clip(15000, 400000)
loan_amount = (income * np.random.uniform(0.5, 4, n)).clip(20000, 1200000)
credit_score = np.random.normal(680, 90, n).clip(300, 900)
employment_years = np.random.exponential(5, n).clip(0, 35)
dependents = np.random.choice([0, 1, 2, 3, 4], n, p=[0.35, 0.3, 0.2, 0.1, 0.05])
existing_loans = np.random.choice([0, 1, 2, 3], n, p=[0.5, 0.3, 0.15, 0.05])
self_employed = np.random.binomial(1, 0.25, n)
education = np.random.choice(["Graduate", "Not Graduate"], n, p=[0.72, 0.28])

score = (
    0.012 * (credit_score - 550)
    - 0.000006 * (loan_amount - income * 1.5)
    + 0.08 * employment_years
    - 0.15 * existing_loans
    - 0.05 * dependents
    - 0.3 * self_employed
    + 0.25 * (education == "Graduate")
    + np.random.normal(0, 1.1, n)
)
approved = (score > np.percentile(score, 38)).astype(int)
loans = pd.DataFrame({
    "annual_income": income.round(0).astype(int),
    "loan_amount": loan_amount.round(0).astype(int),
    "credit_score": credit_score.round(0).astype(int),
    "employment_years": employment_years.round(1),
    "dependents": dependents,
    "existing_loans": existing_loans,
    "self_employed": self_employed,
    "education": education,
    "loan_approved": approved,
})
loans.to_csv(f"{d}/loan_data.csv", index=False)

# ---------------------------------------------------------------
# 06. CUSTOMER SEGMENTATION (RFM)
# ---------------------------------------------------------------
d = f"{ROOT}/06-customer-segmentation/data"
n_cust = 800
n_txn = 9000
cust_ids = np.arange(1, n_cust + 1)
# give customers different underlying behavior clusters to make segmentation meaningful
cluster_assign = np.random.choice([0, 1, 2, 3], n_cust, p=[0.3, 0.25, 0.25, 0.2])
cluster_params = {
    0: dict(freq_lambda=1.5, monetary_mean=400, recency_max=250),   # low value
    1: dict(freq_lambda=8, monetary_mean=1800, recency_max=40),     # champions
    2: dict(freq_lambda=4, monetary_mean=900, recency_max=90),      # loyal
    3: dict(freq_lambda=2, monetary_mean=1500, recency_max=200),    # big spenders, lapsed
}
txn_rows = []
txn_id = 1
for cid in cust_ids:
    params = cluster_params[cluster_assign[cid - 1]]
    n_purchases = max(1, np.random.poisson(params["freq_lambda"]))
    last_day_ago = np.random.randint(1, params["recency_max"])
    for k in range(n_purchases):
        days_ago = last_day_ago + np.random.randint(0, 300)
        amount = max(50, np.random.normal(params["monetary_mean"], params["monetary_mean"] * 0.35))
        txn_rows.append({
            "transaction_id": txn_id,
            "customer_id": cid,
            "purchase_date": (pd.Timestamp("2024-01-01") - pd.Timedelta(days=days_ago)).strftime("%Y-%m-%d"),
            "amount": round(amount, 2),
        })
        txn_id += 1
transactions = pd.DataFrame(txn_rows)
transactions.to_csv(f"{d}/customer_transactions.csv", index=False)

# ---------------------------------------------------------------
# 07. CUSTOMER CHURN PREDICTION (telecom style)
# ---------------------------------------------------------------
d = f"{ROOT}/07-customer-churn-prediction/data"
n = 3000
tenure = np.random.randint(0, 72, n)
contract = np.random.choice(["Month-to-month", "One year", "Two year"], n, p=[0.55, 0.25, 0.2])
monthly_charges = np.random.normal(70, 30, n).clip(18, 120)
internet_service = np.random.choice(["DSL", "Fiber optic", "No"], n, p=[0.35, 0.45, 0.2])
tech_support = np.random.choice(["Yes", "No"], n, p=[0.4, 0.6])
payment_method = np.random.choice(
    ["Electronic check", "Mailed check", "Bank transfer", "Credit card"], n, p=[0.35, 0.2, 0.22, 0.23]
)
paperless_billing = np.random.choice(["Yes", "No"], n, p=[0.6, 0.4])

contract_risk = {"Month-to-month": 0.55, "One year": 0.15, "Two year": 0.03}
churn_prob = (
    pd.Series(contract).map(contract_risk).values
    + (internet_service == "Fiber optic") * 0.12
    + (tech_support == "No") * 0.10
    + (payment_method == "Electronic check") * 0.08
    - (tenure / 72) * 0.35
    + np.random.normal(0, 0.08, n)
).clip(0.02, 0.95)
churn = np.random.binomial(1, churn_prob)
churn_df = pd.DataFrame({
    "tenure_months": tenure,
    "contract_type": contract,
    "monthly_charges": monthly_charges.round(2),
    "internet_service": internet_service,
    "tech_support": tech_support,
    "payment_method": payment_method,
    "paperless_billing": paperless_billing,
    "total_charges": (monthly_charges * (tenure + 1)).round(2),
    "churn": churn,
})
churn_df.to_csv(f"{d}/telecom_churn.csv", index=False)

# ---------------------------------------------------------------
# 08. CREDIT CARD FRAUD DETECTION (imbalanced)
# ---------------------------------------------------------------
d = f"{ROOT}/08-credit-card-fraud-detection/data"
n_legit = 9600
n_fraud = 400
legit = pd.DataFrame({
    "amount": np.random.gamma(2.0, 40, n_legit).round(2),
    "hour_of_day": np.random.normal(14, 4, n_legit).clip(0, 23).astype(int),
    "distance_from_home_km": np.random.exponential(5, n_legit).clip(0, 80).round(1),
    "distance_from_last_txn_km": np.random.exponential(3, n_legit).clip(0, 60).round(1),
    "ratio_to_median_purchase": np.random.normal(1.0, 0.4, n_legit).clip(0.1, 4),
    "is_online_order": np.random.binomial(1, 0.35, n_legit),
    "used_chip": np.random.binomial(1, 0.8, n_legit),
    "is_fraud": 0,
})
fraud = pd.DataFrame({
    "amount": np.random.gamma(3.5, 90, n_fraud).round(2),
    "hour_of_day": np.random.choice(range(24), n_fraud, p=None),
    "distance_from_home_km": np.random.exponential(35, n_fraud).clip(0, 400).round(1),
    "distance_from_last_txn_km": np.random.exponential(28, n_fraud).clip(0, 350).round(1),
    "ratio_to_median_purchase": np.random.normal(4.2, 1.8, n_fraud).clip(1.5, 12),
    "is_online_order": np.random.binomial(1, 0.78, n_fraud),
    "used_chip": np.random.binomial(1, 0.15, n_fraud),
    "is_fraud": 1,
})
fraud_data = pd.concat([legit, fraud], ignore_index=True).sample(frac=1, random_state=7).reset_index(drop=True)
fraud_data.insert(0, "transaction_id", range(1, len(fraud_data) + 1))
fraud_data.to_csv(f"{d}/transactions.csv", index=False)

print("All datasets generated successfully.")
for path, _, files in os.walk(ROOT):
    for f in files:
        if f.endswith(".csv"):
            fp = os.path.join(path, f)
            print(fp, "->", len(pd.read_csv(fp)), "rows")
