import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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
def calculate_yearly_differences(salary_df, rent_df, fuel_df, basket_df):
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
    merged_df["difference"] = merged_df["yearly_salary"] - merged_df["yearly_expenses"]
    return merged_df

# Visualization: Heatmap for Differences
def plot_heatmap(merged_df):
    fig, ax = plt.subplots(figsize=(12, 6))
    heatmap_data = merged_df.pivot("year", "year", "difference")
    sns.heatmap(
        heatmap_data,
        annot=True,
        fmt=".0f",
        cmap="coolwarm",
        cbar_kws={'label': 'Difference (₪)'}
    )
    ax.set_title("Yearly Difference: Income vs Expenses", fontsize=16)
    ax.set_xlabel("Year", fontsize=12)
    ax.set_ylabel("Year", fontsize=12)
    return fig

# Streamlit UI
st.title("Income vs Expenses: Heatmap")

# Calculate yearly differences
merged_df = calculate_yearly_differences(salary_df, rent_df, fuel_df, basket_df)

# Display heatmap
st.header("Yearly Difference Heatmap")
st.pyplot(plot_heatmap(merged_df))
