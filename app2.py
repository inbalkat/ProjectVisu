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

# Prepare data for visualization
def prepare_data(real_df, salary_df, value_column):
    # Align years across both datasets
    real_df = real_df.set_index("year")
    salary_df = salary_df.set_index("year")
    
    # Ensure the years align before calculation
    real_prices = real_df[value_column] / salary_df["salary"]
    
    # Reset the index for plotting
    real_prices = real_prices.reset_index()
    return real_prices

# Visualization function
def plot_data(title, real_prices):
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(real_prices["year"], real_prices.iloc[:, 1], marker='o', label="Price as % of Salary", color='blue')
    ax.set_title(title)
    ax.set_xlabel("Year")
    ax.set_ylabel("Ratio to Salary")
    ax.set_xticks(range(2015, 2025))
    ax.legend()
    ax.grid(True)
    return fig

# Streamlit UI
st.title("Price Trends vs. Salaries")

# Multi-select for categories
categories = st.sidebar.multiselect(
    "Choose categories to display:",
    ["Fuel", "Basic Basket", "Rent"],
    default=["Fuel"]  # Default to showing only "Fuel"
)

# Display graphs for selected categories in a "board" layout
if not categories:
    st.write("Please select at least one category to display the graphs.")
else:
    for category in categories:
        if category == "Fuel":
            st.header("Fuel Prices vs. Salaries")
            real_prices = prepare_data(fuel_df, salary_df, "price per liter")
            st.pyplot(plot_data("Fuel Prices as % of Salary", real_prices))

        elif category == "Basic Basket":
            st.header("Basic Basket Prices vs. Salaries")
            real_prices = prepare_data(basket_df, salary_df, "price for basic basket")
            st.pyplot(plot_data("Basic Basket Prices as % of Salary", real_prices))

        elif category == "Rent":
            st.header("Rent Prices vs. Salaries")
            real_prices = prepare_data(rent_df, salary_df, "price for month")
            st.pyplot(plot_data("Rent Prices as % of Salary", real_prices))
