# Data Science Portfolio — Nupur Jaiswal

Final-year B.Tech CSE (AI Specialization) student. This repo holds end-to-end data science
projects — from raw/messy data to a decision, model, or deployed app — built with Python, SQL/
PostgreSQL, Pandas/NumPy, Statistics, and Scikit-learn.

🔗 [LinkedIn](https://www.linkedin.com/in/nupur-jaiswal/) · [LeetCode](https://leetcode.com/u/NJ_9972/) · nupurjiaswal931@gmail.com

Each project folder is self-contained: a `README.md` explaining the problem and approach, the
dataset in `data/`, a `notebook.ipynb` with the full worked analysis (already executed, with
outputs and charts saved in place), and a `requirements.txt` to reproduce it.

> **Note on data:** all datasets are synthetically generated (`_scripts/generate_datasets.py`,
> seeded for reproducibility) to closely mirror the structure and signal of well-known
> real-world datasets for each problem type. This was a deliberate choice to keep every project
> runnable without external downloads or licensing questions — the modeling/analysis code and
> methodology are the point, not the specific numbers.

## Stage 1 — SQL & Statistical Foundations

| Project | Skills | Folder |
|---|---|---|
| SQL E-commerce Analytics | PostgreSQL, CTEs, window functions | [`01-sql-ecommerce-analytics`](./01-sql-ecommerce-analytics) |
| Global Layoffs Analysis | Pandas, NumPy, data cleaning | [`02-global-layoffs-analysis`](./02-global-layoffs-analysis) |
| Hypothesis Testing on A/B Test Results | Statistics, z-test, confidence intervals | [`03-ab-test-hypothesis-testing`](./03-ab-test-hypothesis-testing) |

## Stage 2 — Machine Learning Core

| Project | Skills | Folder |
|---|---|---|
| House Price Prediction | Regression, Scikit-learn | [`04-house-price-prediction`](./04-house-price-prediction) |
| Loan Approval Prediction | Classification, feature engineering | [`05-loan-approval-prediction`](./05-loan-approval-prediction) |
| Customer Segmentation | K-Means, unsupervised learning, RFM | [`06-customer-segmentation`](./06-customer-segmentation) |
| Customer Churn Prediction | Classification, Random Forest | [`07-customer-churn-prediction`](./07-customer-churn-prediction) |
| Credit Card Fraud Detection | Imbalanced classification, precision/recall | [`08-credit-card-fraud-detection`](./08-credit-card-fraud-detection) |
| Deploy the Churn Model with Streamlit | Deployment, Streamlit | [`09-churn-streamlit-app`](./09-churn-streamlit-app) |

## Stage 3 — NLP, Deep Learning & GenAI *(roadmap — not yet in this repo)*

Sentiment Analysis · Resume Classification · CNN Image Classifier · AI SQL Assistant ·
PDF QA Chatbot — to be added as these skills are learned. See the portfolio site for the full
roadmap.

## Repo structure
```
Data-Science-Portfolio/
├── 01-sql-ecommerce-analytics/
│   ├── README.md
│   ├── schema.sql
│   ├── queries.sql
│   ├── notebook.ipynb
│   ├── data/*.csv
│   └── requirements.txt
├── 02-global-layoffs-analysis/
│   ├── README.md
│   ├── notebook.ipynb
│   ├── data/layoffs_raw.csv
│   └── requirements.txt
├── 03-ab-test-hypothesis-testing/  ...
├── 04-house-price-prediction/      ...
├── 05-loan-approval-prediction/    ...
├── 06-customer-segmentation/       ...
├── 07-customer-churn-prediction/   ...
├── 08-credit-card-fraud-detection/ ...
├── 09-churn-streamlit-app/
│   ├── README.md
│   ├── app.py
│   ├── model/model.pkl
│   └── requirements.txt
└── _scripts/
    └── generate_datasets.py   (regenerates every dataset in /data from scratch)
```

## How to use this repo
Each project works independently — `cd` into a folder, `pip install -r requirements.txt`, and
open the notebook (or run `streamlit run app.py` for project 09). To regenerate all datasets
from scratch: `python3 _scripts/generate_datasets.py` from the repo root.

## Setting this up on GitHub
1. Copy this folder's contents into your local clone of
   [`NJ024/Data-Science-Portfolio`](https://github.com/NJ024/Data-Science-Portfolio).
2. `git add . && git commit -m "Add stage 1 & 2 projects" && git push`.
3. Swap each project's placeholder portfolio-site links (`#`) for the real GitHub folder URLs,
   e.g. `https://github.com/NJ024/Data-Science-Portfolio/tree/main/07-customer-churn-prediction`.
