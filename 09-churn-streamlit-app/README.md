# Deploy the Churn Model with Streamlit

Takes the churn model from `../07-customer-churn-prediction` out of the notebook and into a
live, interactive Streamlit app — the difference between a result and something someone can
actually use without opening Jupyter.

## Why this project
A trained model sitting in a notebook is a data science exercise. A trained model behind a form
someone can fill in is a product. This is the one project in the portfolio explicitly about
that gap.

## Files
| File | Purpose |
|---|---|
| `app.py` | Streamlit app — form for customer attributes, returns churn probability + feature importance |
| `model/model.pkl` | Trained Random Forest + scaler + encoders, copied from project 07 |
| `requirements.txt` | Minimal dependencies to run the app |

## How to run
```bash
pip install -r requirements.txt
streamlit run app.py
```
Then open the local URL Streamlit prints (usually `http://localhost:8501`).

## How it works
1. Loads `model/model.pkl` (built by running the notebook in `../07-customer-churn-prediction`).
2. Collects a customer profile through a form (tenure, contract type, monthly charges, internet
   service, tech support, payment method, paperless billing).
3. Applies the same label encoders used at training time, runs the model, and displays:
   - Churn probability as a percentage and progress bar
   - A clear "high risk / low risk" call, not just a raw number
   - An expandable feature-importance chart so the prediction isn't a black box

## Regenerating the model
If you retrain the model in `07-customer-churn-prediction/notebook.ipynb`, re-running that
notebook automatically copies the updated `model.pkl` into `model/` here — no manual step needed.

## Deploying publicly
To share a live link (not just run locally): push this folder to GitHub, then deploy for free
on [Streamlit Community Cloud](https://streamlit.io/cloud) by pointing it at `app.py`. Update
the portfolio's "Live app" link once deployed.
