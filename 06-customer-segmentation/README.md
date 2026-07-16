# Customer Segmentation (RFM + K-Means)

Unsupervised segmentation of 800 customers into actionable marketing segments, using
Recency/Frequency/Monetary (RFM) features derived from ~3,200 raw transactions, clustered with
K-Means.

## Why this project
Fills the unsupervised-learning gap that most beginner portfolios (which are all classification/
regression) don't cover. RFM is also one of the most widely used frameworks in real marketing
analytics teams, so the technique transfers directly.

## Data
`data/customer_transactions.csv` — raw purchase-level transactions for 800 customers, generated
from four underlying behavioral archetypes (so the clusters found by K-Means are genuinely
recoverable from the data, not arbitrary).

## Files
| File | Purpose |
|---|---|
| `notebook.ipynb` | Build RFM features → scale → elbow method → K-Means (k=4) → segment labeling → PCA visualization → recommended actions |
| `data/customer_transactions.csv` | Raw transaction-level data |

## How to run
```bash
pip install -r requirements.txt
jupyter notebook notebook.ipynb
```

## Approach
1. Aggregated raw transactions into one row per customer: Recency (days since last purchase),
   Frequency (number of purchases), Monetary (total spend).
2. Standardized RFM features and used the elbow method to justify k=4.
3. Labeled each cluster from its RFM profile (e.g. low recency + high frequency = "Champions")
   rather than leaving them as unlabeled cluster numbers.
4. Visualized the 3D RFM space in 2D with PCA, and attached a concrete marketing action to each
   segment.

## Findings
Four segments emerge cleanly: **Champions** (recent, frequent buyers), **Loyal Customers**
(frequent but not always recent), **Big Spenders (Lapsed)** (high value, gone quiet — a
win-back target), and **Low-Value/At Risk**. Segment sizes and the recommended action per
segment are in the executed notebook.
