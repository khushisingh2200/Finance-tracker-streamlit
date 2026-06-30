import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import date
import os

st.set_page_config(page_title="Finance Tracker", layout="wide", page_icon="💶")

# --- Load from CSV or create empty DataFrame ---
if "Transactions" not in st.session_state:
    if os.path.exists("transactions.csv"):
        st.session_state["Transactions"] = pd.read_csv("transactions.csv")
    else:
        st.session_state["Transactions"] = pd.DataFrame(
            columns=["Date", "Category", "Description", "Amount"]
        )

st.title("Personal Finance Tracker")
st.caption("Track your spending, stay within budget, and visualize where your money goes.")

# --- Sidebar ---
st.sidebar.title("Filters")
categories = ["Food", "Transport", "Entertainment", "Rent", "Others"]
selected_category = st.sidebar.multiselect("Select Categories", categories, default=categories)
budget = st.sidebar.number_input("Monthly Budget (€)", value=1000)

st.sidebar.divider()
st.sidebar.caption("Tip: Uncheck categories above to filter the dashboard and history.")

tab1, tab2, tab3 = st.tabs(["Dashboard", "Entry Form", "History"])

# =====================
# TAB 1 — DASHBOARD
# =====================
with tab1:
    st.subheader("Monthly Overview")

    df = st.session_state.Transactions

    # Apply category filter
    if not df.empty:
        filtered_df = df[df["Category"].isin(selected_category)]
    else:
        filtered_df = df

    total = filtered_df["Amount"].sum() if not filtered_df.empty else 0
    budget_left = budget - total
    num_transactions = len(filtered_df)

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Spent", f"€{total:.2f}")
    col2.metric("Budget Left", f"€{budget_left:.2f}", delta=f"{-total:.2f}")
    col3.metric("Transactions", num_transactions)

    st.divider()

    if filtered_df.empty:
        st.warning("No transactions match your filters. Try selecting more categories or add one in the Entry Form tab.")
    else:
        col4, col5 = st.columns(2)

        with col4:
            st.subheader("Spending by Category")
            cat_df = filtered_df.groupby("Category")["Amount"].sum().reset_index()
            fig1 = px.bar(cat_df, x="Category", y="Amount", color="Category", text_auto=".2s")
            fig1.update_layout(yaxis_title="Amount (€)", showlegend=False)
            st.plotly_chart(fig1, use_container_width=True)

        with col5:
            st.subheader("Category Breakdown")
            fig2 = px.pie(cat_df, names="Category", values="Amount", hole=0.4)
            st.plotly_chart(fig2, use_container_width=True)

        st.divider()
        st.subheader("Spending Over Time")
        time_df = filtered_df.groupby("Date")["Amount"].sum().reset_index()
        fig3 = px.line(time_df, x="Date", y="Amount", markers=True)
        fig3.update_layout(yaxis_title="Amount (€)")
        st.plotly_chart(fig3, use_container_width=True)

# =====================
# TAB 2 — ENTRY FORM
# =====================
with tab2:
    st.subheader("Add a Transaction")

    with st.form("entry_form", clear_on_submit=True):
        col_a, col_b = st.columns(2)
        with col_a:
            d = st.date_input("Date", value=date.today())
            cat = st.selectbox("Category", categories)
        with col_b:
            amount = st.number_input("Amount (€)", min_value=0.0, step=0.5)
            description = st.text_input("Description")

        submit = st.form_submit_button("Add Transaction", use_container_width=True)

        if submit:
            if description == "":
                st.error("Please enter a description.")
            elif amount == 0:
                st.warning("Amount is 0. Are you sure?")
            else:
                new_row = {
                    "Date": d,
                    "Category": cat,
                    "Description": description,
                    "Amount": amount
                }
                st.session_state.Transactions = pd.concat(
                    [st.session_state.Transactions, pd.DataFrame([new_row])],
                    ignore_index=True
                )
                st.session_state.Transactions.to_csv("transactions.csv", index=False)
                st.success(f" Added €{amount:.2f} for {cat}!")
                st.balloons()

# =====================
# TAB 3 — HISTORY
# =====================
with tab3:
    st.subheader("Transaction History")

    df = st.session_state.Transactions

    if df.empty:
        st.warning("No transactions found. Add one in the Entry Form tab.")
    else:
        filtered_df = df[df["Category"].isin(selected_category)]

        if filtered_df.empty:
            st.info("No transactions match the selected categories.")
        else:
            st.dataframe(filtered_df, use_container_width=True)

            col_x, col_y = st.columns(2)
            with col_x:
                csv = filtered_df.to_csv(index=False)
                st.download_button(
                    "⬇️ Download Filtered CSV",
                    csv,
                    file_name="transactions.csv",
                    mime="text/csv",
                    use_container_width=True
                )
            with col_y:
                if st.button("🗑️ Clear All Transactions", use_container_width=True):
                    st.session_state.Transactions = pd.DataFrame(
                        columns=["Date", "Category", "Description", "Amount"]
                    )
                    st.session_state.Transactions.to_csv("transactions.csv", index=False)
                    st.rerun()

        with st.expander("Show Raw Unfiltered Data"):
            st.write(df)