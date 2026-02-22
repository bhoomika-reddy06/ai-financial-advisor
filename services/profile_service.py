import streamlit as st

def collect_profile():
    st.sidebar.header("📊 Financial Profile")

    income = st.sidebar.number_input("Monthly Income", min_value=0)
    expenses = st.sidebar.number_input("Monthly Expenses", min_value=0)
    savings = st.sidebar.number_input("Current Savings", min_value=0)

    risk = st.sidebar.selectbox(
        "Risk Tolerance",
        ["Low", "Medium", "High"]
    )

    profile = {
        "income": income,
        "expenses": expenses,
        "savings": savings,
        "risk": risk
    }

    return profile