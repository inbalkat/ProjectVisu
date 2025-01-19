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

# Visualization function: Radar Plot for Each Category
def plot_category_star(data, category, color):
    fig, ax = plt.subplots(figsize=(8, 8), subplot_kw={"projection": "polar"})
    years = data["Year"].values
    values = data[category].values

    # Define angles for each year
    angles = np.linspace(0, 2 * np.pi, len(years), endpoint=False).tolist()
    angles += angles[:1]  # Close the loop

    # Add the closing value to close the radar plot
    values = np.append(values, values[0])

    # Plot the radar chart
    ax.plot(angles, values, label=f"{category} as % of Salary", color=color)
    ax.fill(angles, values, alpha=0.25, color=color)

    # Customize plot ranges
    max_value = np.max(values)
    min_value = np.min(values)
    range_buffer = (max_value - min_value) * 0.1  # Add a 10% buffer to the range

    ax.set_ylim(min_value - range_buffer, max_value + range_buffer)  # Adjust radial limits

    # Customize plot
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(years)
    ax.set_yticks(np.linspace(min_value, max_value, 5))  # Dynamically set radial ticks
    ax.set_yticklabels([f"{tick:.2f}" for tick in np.linspace(min_value, max_value, 5)])
    ax.set_title(f"Radar Plot: {category} as % of Salary", va="bottom")

    return fig

# Streamlit UI
st.title("Radar Plot: Categories as % of Salary")

# User selects category
category = st.selectbox("Choose a category:", ["Rent", "Fuel", "Basic Basket"])

# Assign unique colors for each category
category_colors = {
    "Rent": "green",
    "Fuel": "orange",
    "Basic Basket": "purple"
}

# Display radar plot for selected category
selected_color = category_colors[category]
st.pyplot(plot_category_star(data, category, selected_color))
