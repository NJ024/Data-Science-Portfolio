# Global Layoffs Analysis

Cleaned a deliberately messy tech-layoffs dataset — duplicate rows, three different date
formats, inconsistent company-name casing/whitespace, missing values — then analyzed layoff
trends by year, industry, and country.

## Why this project
Most real-world data isn't clean. This project is a demonstration of the unglamorous but
essential first 70% of any data science task: auditing data quality, writing a repeatable
cleaning pipeline, and validating the result before doing any analysis on top of it.

## Data
`data/layoffs_raw.csv` — synthetic data intentionally generated with common messy-data issues:
- Exact duplicate rows
- Company names with inconsistent casing/leading whitespace (`"Meta"`, `"META"`, `" Meta"`)
- Three date formats mixed in the same column (`YYYY-MM-DD`, `MM/DD/YYYY`, `DD-MM-YYYY`)
- Missing values in `total_laid_off`, `percentage_laid_off`, `stage`, and `funds_raised_millions`

## Files
| File | Purpose |
|---|---|
| `notebook.ipynb` | Data quality audit → cleaning pipeline → year/industry/country analysis |
| `data/layoffs_raw.csv` | Raw (messy) input data |

## How to run
```bash
pip install -r requirements.txt
jupyter notebook notebook.ipynb
```

## Approach
1. **Audit** — count duplicates, missing values, and inspect text-field inconsistencies before touching anything.
2. **Clean** — drop exact duplicates, standardize text casing/whitespace, parse all three date formats into a single `datetime` column, coerce numeric columns instead of dropping rows with missing headcounts (a missing headcount doesn't mean the layoff didn't happen).
3. **Analyze** — aggregate by year, industry, and country; separately track *percentage of workforce cut* vs. *raw headcount*, since a 60%-of-staff cut at a small company and a 2% cut at a large company aren't comparable on headcount alone.

## Findings
See the notebook for the full breakdown — cleaning removed all duplicate rows and unified the
date column, after which layoffs are aggregated by year (trend), industry (top 10), and country,
plus a ranked list of companies with the highest percentage of workforce cut.
