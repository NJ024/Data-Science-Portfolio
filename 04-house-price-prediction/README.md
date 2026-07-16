# House Price Prediction

Regression pipeline predicting sale price from property features (area, bedrooms, bathrooms,
age, city tier, distance to city, garage). Compares a Linear Regression baseline against a
Random Forest Regressor, evaluated on RMSE, MAE, and R².

## Why this project
Regression is a gap most beginner portfolios skip in favor of classification. House pricing is
also an intuitive domain to sanity-check a model against — you can reason about whether "more
area = higher price" and "further from city = lower price" actually show up in the results.

## Data
`data/house_prices.csv` — 1,500 synthetic properties with a price formula that includes
realistic nonlinear effects (city-tier multiplier, diminishing returns) plus noise, so no model
should get a "perfect" R².

## Files
| File | Purpose |
|---|---|
| `notebook.ipynb` | EDA → train/test split → Linear Regression baseline → Random Forest → comparison → feature importance |
| `data/house_prices.csv` | Synthetic housing data |

## How to run
```bash
pip install -r requirements.txt
jupyter notebook notebook.ipynb
```

## Approach
1. EDA: correlation of each feature with `sale_price`, scatter of area vs. price.
2. Standardized features for Linear Regression; Random Forest run on raw features (tree models
   don't need scaling).
3. Compared both models on RMSE, MAE, and R² — not just one metric.
4. Feature importance from the Random Forest, plus a predicted-vs-actual scatter to visually
   check where the model is weaker (typically the high-price tail, where fewer examples exist).

## Findings
Random Forest outperforms the Linear Regression baseline across all three metrics, since price
isn't a purely linear function of the inputs. `area_sqft` and `city_tier` are consistently the
strongest price drivers. Exact metric values are in the executed notebook.
