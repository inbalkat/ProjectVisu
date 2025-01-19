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

# Visualization function: Star Plot
def plot_star(data):
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw={"projection": "polar"})
    categories = ["Rent", "Fuel", "Basic Basket"]
    angles = np.linspace(0, 2 * np.pi, len(categories), endpoint=False).tolist()

    # Add the closing angle to complete the loop
    angles += angles[:1]

    # Plot for each year
    for _, row in data.iterrows():
        values = row[categories].values.tolist()
        values += values[:1]  # Repeat the first value to close the loop
        ax.plot(angles, values, label=f"Year {int(row['Year'])}")
        ax.fill(angles, values, alpha=0.1)

    # Customize plot
    ax.set_yticks([])
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(categories)
    ax.set_title("Star Plot: Categories as % of Salary", va="bottom")
    ax.legend(loc="upper right", bbox_to_anchor=(1.3, 1.1))

    return fig

# Streamlit UI
st.title("Star Plot: Categories as % of Salary")

# Display star plot
st.pyplot(plot_star(data))
