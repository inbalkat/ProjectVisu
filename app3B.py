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
    basket_df["yearly_expenses"] = basket_df["price for basic basket"] * 48
    fuel_df["yearly_expenses"] = fuel_df["price per liter"] * 1200
    rent_df["yearly_expenses"] = rent_df["price for month"] * 12
    salary_df["yearly_salary"] = salary_df["salary"] * 12
    merged_df = salary_df[["year", "yearly_salary"]].copy()
    merged_df["rent"] = rent_df["yearly_expenses"].values
    merged_df["fuel"] = fuel_df["yearly_expenses"].values
    merged_df["basket"] = basket_df["yearly_expenses"].values
    merged_df["total_expenses"] = (
        merged_df["rent"] + merged_df["fuel"] + merged_df["basket"]
    )
    return merged_df

# Visualization: Faceted Stacked Bar Plot
def plot_stacked_bars(merged_df, selected_years):
    num_years = len(selected_years)
    fig, axes = plt.subplots(1, num_years, figsize=(6 * num_years, 6), squeeze=False)

    for idx, year in enumerate(selected_years):
        year_data = merged_df[merged_df["year"] == year].iloc[0]
        expenses = [year_data["basket"], year_data["fuel"], year_data["rent"]]
        labels = ["Basic Basket", "Fuel", "Rent"]
        colors = ["#99FF99", "#66B2FF", "#FF9999"]

        ax = axes[0, idx]
        ax.bar(labels, expenses, color=colors, alpha=0.8)
        ax.axhline(year_data["yearly_salary"], color="black", linestyle="--", label="Yearly Salary")
        ax.set_title(f"Year {year}")
        ax.set_ylabel("Amount (₪)")
        ax.legend()

    plt.tight_layout()
    return fig

# Streamlit UI
st.title("Income vs. Expenses Visualization")

# Calculate yearly expenses and salaries
merged_df = calculate_yearly_expenses(salary_df, rent_df, fuel_df, basket_df)

# Sidebar for year selection
st.sidebar.title("Select Years")
selected_years = st.sidebar.multiselect(
    "Choose years to display:", options=merged_df["year"].tolist(), default=merged_df["year"].tolist()
)

if selected_years:
    st.header("Income and Expenses per Year")
    st.pyplot(plot_stacked_bars(merged_df, selected_years))
else:
    st.warning("Please select at least one year.")
