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

# Update calculations to yearly
def calculate_yearly_expenses(salary_df, rent_df, fuel_df, basket_df):
    # Update basket to 4 per month * 12 months = 48 baskets per year
    basket_df["yearly_expenses"] = basket_df["price for basic basket"] * 48
    # Fuel: Assume 100 liters per month * 12 months = 1200 liters per year
    fuel_df["yearly_expenses"] = fuel_df["price per liter"] * 1200
    # Rent: Already yearly
    rent_df["yearly_expenses"] = rent_df["price for month"] * 12
    # Combine all yearly expenses
    salary_df["yearly_salary"] = salary_df["salary"] * 12
    merged_df = salary_df[["year", "yearly_salary"]].copy()
    merged_df["yearly_expenses"] = (
        basket_df["yearly_expenses"].values
        + fuel_df["yearly_expenses"].values
        + rent_df["yearly_expenses"].values
    )
    return merged_df

# Visualization: Combined Yearly Salary and Expenses
def plot_combined_salary_and_expenses(merged_df):
    fig, ax = plt.subplots(figsize=(12, 8))
    x = np.arange(len(merged_df["year"]))  # the label locations
    width = 0.35  # the width of the bars

    # Define custom colors
    salary_color = "cornflowerblue"
    expenses_color = "indianred"

    ax.bar(x - width/2, merged_df["yearly_salary"], width, label="Yearly Salary", color=salary_color)
    ax.bar(x + width/2, merged_df["yearly_expenses"], width, label="Yearly Expenses", color=expenses_color)

    # Add labels, title, grid, and customize y-axis range
    ax.set_xlabel("Year")
    ax.set_ylabel("Amount (₪)")
    ax.set_title("Yearly Salary vs Yearly Expenses")
    ax.set_xticks(x)
    ax.set_xticklabels(merged_df["year"])
    ax.set_ylim(50000, 80000)  # Adjusted to reflect yearly values
    ax.legend()
    ax.grid(axis="y")

    return fig

# Streamlit UI
st.title("Income vs Expenses")

# Calculate yearly expenses and salaries
merged_df = calculate_yearly_expenses(salary_df, rent_df, fuel_df, basket_df)

# Display combined graph
st.header("Yearly Salary vs Yearly Expenses")
st.markdown("<p style='font-size:18px; color:white;'>Expenses = Rent + Basic Shopping Basket + Fuel</p>", unsafe_allow_html=True) 
# st.subheader("Expenses = Rent + Basic Shopping Basket + Fuel")
st.pyplot(plot_combined_salary_and_expenses(merged_df))
