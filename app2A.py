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
def prepare_data(salary_df, rent_df, fuel_df, basket_df):
    # Align years across all datasets and calculate the monthly percentages
    rent_df = rent_df.set_index("year")
    fuel_df = fuel_df.set_index("year")
    basket_df = basket_df.set_index("year")
    salary_df = salary_df.set_index("year")

    rent_percent = rent_df["price for month"] / salary_df["salary"]
    fuel_percent = (fuel_df["price per liter"] * 100) / salary_df["salary"]  # Fuel: 100 liters/month
    basket_percent = (basket_df["price for basic basket"] * 4) / salary_df["salary"]  # Basket: 4 baskets/month

    # Combine into a single dataframe
    data = pd.DataFrame({
        "Year": salary_df.index,
        "Rent": rent_percent,
        "Fuel": fuel_percent,
        "Basic Basket": basket_percent
    })

    return data.reset_index(drop=True)

data = prepare_data(salary_df, rent_df, fuel_df, basket_df)

# Visualization function: Overlapping Area Plot
def plot_combined_area(data):
    fig, ax = plt.subplots(figsize=(10, 6))
    
    # Plot each category separately
    ax.fill_between(
        data["Year"],
        data["Rent"] * 100,  # Convert to percentage
        color="lightskyblue",
        alpha=0.7,
        label="Rent"
    )
    ax.fill_between(
        data["Year"],
        data["Basic Basket"] * 100,  # Convert to percentage
        color="mediumpurple",
        alpha=0.7,
        label="Basic Basket"
    )
    ax.fill_between(
        data["Year"],
        data["Fuel"] * 100,  # Convert to percentage
        color="royalblue",
        alpha=0.7,
        label="Fuel"
    )
    
    
    # Customize the plot
    ax.set_title("Categories as % of Salary", fontsize=16)
    ax.set_xlabel("Year")
    ax.set_ylabel("Percentage of Salary (%)")
    ax.set_xticks(range(2015, 2025))
    ax.set_ylim(0, 100)
    ax.legend(loc="upper left")
    ax.grid(axis="y", linestyle="--", alpha=0.7)

    return fig

# Streamlit UI
st.title("Categories as % of Salary")
# st.header("")

# Display the overlapping area plot
st.pyplot(plot_combined_area(data))
