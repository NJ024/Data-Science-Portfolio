# Credit Card Fraud Detection

Highly imbalanced classification problem (~4% fraud). Uses `class_weight='balanced'`, a
stratified split, and precision/recall/F1/precision-recall-AUC — not accuracy — as the real
measures of success, since fraud is rare by design.

## Why this project
This is the project that demonstrates understanding of *why* accuracy is the wrong metric for
imbalanced problems, which is a common blind spot in beginner portfolios. It's also directly
relevant to any risk/fraud/anomaly-detection role.

## Data
`data/transactions.csv` — 10,000 synthetic transactions (9,600 legitimate, 400 fraudulent),
with fraud transactions generated to have higher amounts, larger distance-from-home, higher
ratio-to-median-purchase, and lower chip usage — mirroring real fraud signal patterns.

## Files
| File | Purpose |
|---|---|
| `notebook.ipynb` | Class imbalance audit → naive-baseline sanity check → Random Forest with balanced class weights → precision-recall curve → threshold tuning → feature importance |
| `data/transactions.csv` | Synthetic transaction data |

## How to run
```bash
pip install -r requirements.txt
jupyter notebook notebook.ipynb
```

## Approach
1. Quantified the class imbalance and showed explicitly why a naive "always legitimate" model's
   high accuracy is meaningless (it catches 0% of fraud).
2. Stratified train/test split to preserve the imbalance ratio in both sets.
3. Random Forest with `class_weight='balanced'` instead of naive oversampling.
4. Evaluated with a full classification report, ROC-AUC, and **average precision (PR-AUC)** —
   the more informative metric under heavy class imbalance — plus manual threshold tuning to
   maximize F1.

## Findings
`ratio_to_median_purchase` and `distance_from_home_km` are the strongest fraud signals — an
unusually large purchase far from the account's normal location is the clearest tell, matching
how real card-network fraud systems reason. Exact precision/recall/F1 numbers are in the
executed notebook.
