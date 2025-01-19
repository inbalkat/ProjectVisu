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

# Prepare data for visualization
def prepare_data_monthly(salary_df, rent_df, fuel_df, basket_df):
    # Calculate monthly expenses for each category
    basket_df["monthly_expenses"] = basket_df["price for basic basket"] * 4
    fuel_df["monthly_expenses"] = fuel_df["price per liter"] * 100

    # Merge with salary data
    merged_rent = rent_df.merge(salary_df, on="year")
    merged_fuel = fuel_df.merge(salary_df, on="year")
    merged_basket = basket_df.merge(salary_df, on="year")

    # Calculate percentages of salary
    rent_percent = merged_rent["price for month"] / merged_rent["salary"]
    fuel_percent = merged_fuel["monthly_expenses"] / merged_fuel["salary"]
    basket_percent = merged_basket["monthly_expenses"] / merged_basket["salary"]

    years = salary_df["year"]

    data = pd.DataFrame({
        "Year": years,
        "Rent": rent_percent,
        "Fuel": fuel_percent,
        "Basic Basket": basket_percent
    })
    return data

data = prepare_data_monthly(salary_df, rent_df, fuel_df, basket_df)

# Visualization function: Pie-like Plot
def plot_category_pie(data, category):
    years = data["Year"].values
    values = data[category].values

    # Normalize values for better visualization in the pie plot
    total = np.sum(values)
    normalized_values = values / total

    fig, ax = plt.subplots(figsize=(8, 8))
    wedges, texts, autotexts = ax.pie(
        values,
        labels=years,
        autopct=lambda p: f'{p:.1f}% ({p * total / 100:.2f})',
        startangle=90,
        colors=plt.cm.viridis(np.linspace(0, 1, len(years))),
        wedgeprops=dict(width=0.3, edgecolor='w')
    )

    # Customize plot
    ax.set_title(f"{category} Percentage of Salary Over Time", fontsize=16)
    plt.setp(autotexts, size=10, weight="bold")

    return fig

# Streamlit UI
st.title("Pie-like Plot: Categories as % of Salary")

# User selects category
category = st.selectbox("Choose a category:", ["Rent", "Fuel", "Basic Basket"])

# Display pie-like plot for selected category
st.pyplot(plot_category_pie(data, category))
