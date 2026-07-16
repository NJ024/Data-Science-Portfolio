# Loan Approval Prediction

Binary classifier on applicant financial and demographic data (income, loan amount, credit
score, employment history, dependents, education). Compares Logistic Regression against a
Random Forest, evaluated on accuracy, precision, recall, F1, and ROC-AUC.

## Why this project
Loan approval is a classic classification problem where the cost of a false positive
(approving a bad loan) and a false negative (rejecting a good applicant) are genuinely
different — a good excuse to evaluate beyond plain accuracy and think about what the business
actually cares about.

## Data
`data/loan_data.csv` — 2,000 synthetic applicants with an approval signal driven by credit
score, income-to-loan ratio, employment history, dependents, existing loans, and education —
plus noise, so the classes aren't perfectly separable.

## Files
| File | Purpose |
|---|---|
| `notebook.ipynb` | Encoding → Logistic Regression → Random Forest → full metric comparison → confusion matrix → ROC curve → feature importance |
| `data/loan_data.csv` | Synthetic loan application data |

## How to run
```bash
pip install -r requirements.txt
jupyter notebook notebook.ipynb
```

## Approach
1. Encoded the one categorical feature (`education`) and scaled features for Logistic
   Regression; Random Forest run on raw features.
2. Stratified train/test split to preserve the approval/rejection ratio.
3. Evaluated on accuracy **and** precision/recall/F1/ROC-AUC — accuracy alone would hide how the
   model handles the minority outcome.
4. Confusion matrix and ROC curve plotted for the stronger model; feature importance used to
   explain *why* the model approves or rejects.

## Findings
Credit score, loan-to-income ratio, and employment history are the strongest predictors of
approval. Random Forest edges out Logistic Regression on most metrics, but Logistic
Regression's coefficients are kept as a more interpretable fallback for explaining individual
rejections. Exact metric values are in the executed notebook.
