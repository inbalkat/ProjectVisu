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
def plot_combined_data(title, fuel_prices, basket_prices, rent_prices):
    fig, ax = plt.subplots(figsize=(10, 6))
    
    ax.plot(fuel_prices["year"], fuel_prices.iloc[:, 1], label="Fuel as % of Salary", color='orange')
    ax.plot(basket_prices["year"], basket_prices.iloc[:, 1], label="Basic Basket as % of Salary", color='green')
    ax.plot(rent_prices["year"], rent_prices.iloc[:, 1], label="Rent as % of Salary", color='blue')
    
    ax.set_title(title)
    ax.set_xlabel("Year")
    ax.set_ylabel("Ratio to Salary")
    ax.set_xticks(range(2015, 2025))
    ax.legend()
    ax.grid(True)
    
    return fig

# Prepare the data for each category
fuel_prices = prepare_data(fuel_df, salary_df, "price per liter", multiplier=100)
basket_prices = prepare_data(basket_df, salary_df, "price for basic basket", multiplier=4)
rent_prices = prepare_data(rent_df, salary_df, "price for month")

# Streamlit UI
st.title("Price Trends vs. Salaries")
st.header("All Categories on a Single Plot")

# Display combined plot
st.pyplot(plot_combined_data("Prices of Categories as % of Salary", fuel_prices, basket_prices, rent_prices))
