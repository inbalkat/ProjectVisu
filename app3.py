import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load data from uploaded Excel files
@st.cache_data
def load_data():
    salary_df = pd.read_excel("https://raw.githubusercontent.com/inbalkat/ProjectVisu/main/salary.xlsx")
    rent_df = pd.read_excel("https://raw.githubusercontent.com/inbalkat/ProjectVisu/main/rent.xlsx")
    fuel_df = pd.read_excel("https://raw.githubusercontent.com/inbalkat/ProjectVisu/main/fuel.xlsx")
    basket_df = pd.read_excel("https://raw.githubusercontent.com/inbalkat/ProjectVisu/main/basic_basket.xlsx")
    return salary_df, rent_df, fuel_df, basket_df

# Load the data
salary_df, rent_df, fuel_df, basket_df = load_data()

# Calculate monthly cost for basic basket
def calculate_monthly_basket_cost(basket_df):
    basket_df["monthly_cost"] = basket_df["price for basic basket"] * 6  # Fixed to 6 baskets per month
    return basket_df

basket_df = calculate_monthly_basket_cost(basket_df)

# Aggregate total monthly expenses
def calculate_monthly_expenses(rent_df, fuel_df, basket_df):
    total_expenses_df = pd.DataFrame()
    total_expenses_df["year"] = rent_df["year"]
    total_expenses_df["monthly_expenses"] = (
        rent_df["price for month"] +  # Monthly rent
        fuel_df["price per liter"] * 100 +  # 100 liters of fuel per month
        basket_df["monthly_cost"]  # Monthly cost of basic basket
    )
    return total_expenses_df

total_expenses_df = calculate_monthly_expenses(rent_df, fuel_df, basket_df)

# Merge with salary data
def merge_salary_and_expenses(salary_df, total_expenses_df):
    merged_df = pd.merge(salary_df, total_expenses_df, on="year")
    merged_df["expenses_to_salary_ratio"] = merged_df["monthly_expenses"] / merged_df["salary"]
    return merged_df

merged_df = merge_salary_and_expenses(salary_df, total_expenses_df)

# Visualization: Combined Monthly Salary and Expenses
def plot_combined_salary_and_expenses(merged_df):
    fig, ax = plt.subplots(figsize=(12, 8))
    x = np.arange(len(merged_df["year"]))  # the label locations
    width = 0.35  # the width of the bars

    ax.bar(x - width/2, merged_df["salary"], width, label="Monthly Salary", color="green")
    ax.bar(x + width/2, merged_df["monthly_expenses"], width, label="Monthly Expenses", color="blue")

    # Add labels, title, and grid
    ax.set_xlabel("Year")
    ax.set_ylabel("Amount (₪)")
    ax.set_title("Monthly Salary vs Monthly Expenses")
    ax.set_xticks(x)
    ax.set_xticklabels(merged_df["year"])
    ax.legend()
    ax.grid(axis="y")

    return fig

# Streamlit UI
st.title("Cost of Living in Israel")

# Display combined graph
st.header("Monthly Salary vs Monthly Expenses")
st.pyplot(plot_combined_salary_and_expenses(merged_df))
