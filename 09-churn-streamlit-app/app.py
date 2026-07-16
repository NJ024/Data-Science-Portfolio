"""
Customer Churn Predictor — Streamlit app
Loads the Random Forest model trained in ../07-customer-churn-prediction/notebook.ipynb
and serves live predictions through a simple form.

Run locally:
    pip install -r requirements.txt
    streamlit run app.py
"""
import pickle
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Churn Predictor", page_icon="📉", layout="centered")


@st.cache_resource
def load_model():
    with open("model/model.pkl", "rb") as f:
        return pickle.load(f)


bundle = load_model()
model = bundle["model"]
scaler = bundle["scaler"]
encoders = bundle["encoders"]
feature_order = bundle["feature_order"]

st.title("📉 Customer Churn Predictor")
st.caption(
    "Live demo of the churn model from `07-customer-churn-prediction`. "
    "Fill in a customer profile to get a churn-risk score."
)

with st.form("churn_form"):
    col1, col2 = st.columns(2)
    with col1:
        tenure_months = st.slider("Tenure (months)", 0, 72, 12)
        monthly_charges = st.slider("Monthly charges (₹)", 18, 120, 65)
        contract_type = st.selectbox("Contract type", ["Month-to-month", "One year", "Two year"])
        internet_service = st.selectbox("Internet service", ["DSL", "Fiber optic", "No"])
    with col2:
        tech_support = st.selectbox("Tech support", ["Yes", "No"])
        payment_method = st.selectbox(
            "Payment method",
            ["Electronic check", "Mailed check", "Bank transfer", "Credit card"],
        )
        paperless_billing = st.selectbox("Paperless billing", ["Yes", "No"])

    submitted = st.form_submit_button("Predict churn risk")

if submitted:
    total_charges = monthly_charges * (tenure_months + 1)
    row = {
        "tenure_months": tenure_months,
        "contract_type": contract_type,
        "monthly_charges": monthly_charges,
        "internet_service": internet_service,
        "tech_support": tech_support,
        "payment_method": payment_method,
        "paperless_billing": paperless_billing,
        "total_charges": total_charges,
    }
    df_row = pd.DataFrame([row])

    for col, le in encoders.items():
        df_row[col] = le.transform(df_row[col])

    df_row = df_row[feature_order]
    proba = model.predict_proba(df_row)[0, 1]
    pred = int(proba >= 0.5)

    st.divider()
    st.metric("Churn probability", f"{proba*100:.1f}%")
    if pred == 1:
        st.error("⚠️ High churn risk — flag this account for retention outreach.")
    else:
        st.success("✅ Low churn risk.")

    st.progress(min(int(proba * 100), 100))

    with st.expander("What's driving this prediction?"):
        importances = pd.Series(model.feature_importances_, index=feature_order).sort_values(ascending=False)
        st.bar_chart(importances)
