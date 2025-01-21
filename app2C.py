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
    rent_percent = merged_rent["price for month"] / merged_rent["salary"] * 100
    fuel_percent = merged_fuel["monthly_expenses"] / merged_fuel["salary"] * 100
    basket_percent = merged_basket["monthly_expenses"] / merged_basket["salary"] * 100

    years = salary_df["year"]

    data = pd.DataFrame({
        "Year": years,
        "Rent": rent_percent,
        "Fuel": fuel_percent,
        "Basic Basket": basket_percent
    })
    return data

data = prepare_data_monthly(salary_df, rent_df, fuel_df, basket_df)

# Visualization function: Stairs Plot for Each Category
def plot_category_stairs(data, category, color):
    fig, ax = plt.subplots(figsize=(10, 6))
    years = data["Year"].values
    values = data[category].values

    # Create step plot
    ax.step(years, values, label=f"{category} as % of Salary", color=color, where='mid', linewidth=2)

    # Highlight each step with a scatter plot for clarity
    ax.scatter(years, values, color=color, edgecolor="black", zorder=5)

    max_val = values.max()
    min_val = values.min()
    buffer = (max_val-min_val) * 0.5
    # ax.set_ylim(min_val-buffer, max_val+buffer)
    ax.set_ylim(min_val, max_val)

    # Customize plot
    ax.set_title(f"Stair Plot: {category} as % of Salary", fontsize=16)
    ax.set_xlabel("Year")
    ax.set_ylabel("Percentage of Salary (%)")
    ax.set_xticks(years)
    # ax.set_yticks(np.linspace(values.min(), values.max(), 5))
    ax.legend()
    ax.grid(True)

    return fig

# Streamlit UI
st.title("Stairs Plot: Categories as % of Salary")

# User selects category
category = st.selectbox("Choose a category:", ["Rent", "Fuel", "Basic Basket"])

# Assign unique colors for each category
category_colors = {
    "Rent": "green",
    "Fuel": "orange",
    "Basic Basket": "purple"
}

# Display stairs plot for selected category
selected_color = category_colors[category]
st.pyplot(plot_category_stairs(data, category, selected_color))
