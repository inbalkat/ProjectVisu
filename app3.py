import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

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
def calculate_monthly_basket_cost(basket_df, baskets_per_month):
    basket_df["monthly_cost"] = basket_df["price for basic basket"] * baskets_per_month
    return basket_df

# User input for number of baskets per month
baskets_per_month = st.sidebar.slider("Number of basic baskets purchased per month:", 1, 10, 6)
basket_df = calculate_monthly_basket_cost(basket_df, baskets_per_month)

# Aggregate total monthly expenses
def calculate_monthly_expenses(rent_df, fuel_df, basket_df):
    total_expenses_df = pd.DataFrame()
    total_expenses_df["year"] = rent_df["year"]
    total_expenses_df["monthly_expenses"] = (
        rent_df["price for month"] +  # Monthly rent
        fuel_df["price per liter"] * 100 +  # Example: 100 liters of fuel per month
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

# Visualization: Monthly Expenses vs Salary
def plot_monthly_expenses_vs_salary(merged_df):
    fig, ax1 = plt.subplots(figsize=(10, 6))

    # Plot monthly expenses
    ax1.plot(merged_df["year"], merged_df["monthly_expenses"], label="Monthly Expenses", color="blue", marker="o")
    ax1.set_ylabel("Monthly Expenses (₪)", color="blue")
    ax1.tick_params(axis="y", labelcolor="blue")
    ax1.set_xlabel("Year")

    # Plot monthly salary
    ax2 = ax1.twinx()
    ax2.plot(merged_df["year"], merged_df["salary"], label="Monthly Salary", color="green", marker="o", linestyle="--")
    ax2.set_ylabel("Monthly Salary (₪)", color="green")
    ax2.tick_params(axis="y", labelcolor="green")

    fig.suptitle("Monthly Expenses vs. Salary Over Years")
    fig.tight_layout()
    ax1.legend(loc="upper left")
    ax2.legend(loc="upper right")
    return fig

st.pyplot(plot_monthly_expenses_vs_salary(merged_df))

# Visualization: Expenses to Salary Ratio
def plot_monthly_expenses_to_salary_ratio(merged_df):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(merged_df["year"], merged_df["expenses_to_salary_ratio"], label="Expenses to Salary Ratio", color="red", marker="o")
    ax.set_title("Monthly Expenses to Salary Ratio Over Years")
    ax.set_xlabel("Year")
    ax.set_ylabel("Ratio")
    ax.grid(True)
    ax.legend()
    return fig

st.pyplot(plot_monthly_expenses_to_salary_ratio(merged_df))
