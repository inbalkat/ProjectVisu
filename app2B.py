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

# Visualization function: Polar Bar Chart
def plot_category_polar(data, category):
    years = data["Year"].values
    values = data[category].values

    # Normalize values for better visualization in the polar bar chart
    angles = np.linspace(0, 2 * np.pi, len(years), endpoint=False).tolist()
    angles += angles[:1]  # Close the circular plot for a seamless look
    values = np.append(values, values[0])  # Add the first value to the end to close the loop

    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw={"projection": "polar"})

    bars = ax.bar(
        angles[:-1],  # Use only the original angles for the bars
        values[:-1],  # Use only the original values for the bars
        width=2 * np.pi / len(years),
        color=plt.cm.viridis(np.linspace(0, 1, len(years))),
        edgecolor="white",
        align="center"
    )
    
    # Add labels to each bar (percentage in the middle of the slice)
    for angle, bar, value in zip(angles[:-1], bars, values[:-1]):
        ax.text(
            angle,
            bar.get_height() / 2,  # Position text at the middle of the bar
            f'{value:.1%}',
            ha="center", va="center", fontsize=12, color="white", fontweight="bold"
        )

    # Customize plot
    ax.set_title(f"{category} Percentage of Salary Over Time", fontsize=16, pad=20)
    ax.set_yticks([])  # Remove radial ticks
    ax.set_xticks(angles[:-1])  # Remove the repeated angle for the label
    ax.set_xticklabels(years, fontsize=10, color="black")

    return fig

# Streamlit UI
st.title("Polar Bar Plot: Categories as % of Salary")

# User selects category
category = st.selectbox("Choose a category:", ["Rent", "Fuel", "Basic Basket"])

# Display polar bar chart for selected category
st.pyplot(plot_category_polar(data, category))
