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

# Prepare data for visualization
def prepare_data(salary_df, rent_df, fuel_df, basket_df):
    merged_rent = rent_df.merge(salary_df, on="year")
    merged_fuel = fuel_df.merge(salary_df, on="year")
    merged_basket = basket_df.merge(salary_df, on="year")

    rent_percent = merged_rent["price for month"] / merged_rent["salary"]
    fuel_percent = merged_fuel["price per liter"] / merged_fuel["salary"]
    basket_percent = merged_basket["price for basic basket"] / merged_basket["salary"]

    years = salary_df["year"]

    data = pd.DataFrame({
        "Year": years,
        "Rent": rent_percent,
        "Fuel": fuel_percent,
        "Basic Basket": basket_percent
    })
    return data

data = prepare_data(salary_df, rent_df, fuel_df, basket_df)

# Visualization function: Heatmap
def plot_heatmap(data):
    fig, ax = plt.subplots(figsize=(12, 8))

    # Pivot data for heatmap
    heatmap_data = data.set_index("Year").transpose()

    sns.heatmap(
        heatmap_data,
        annot=True,
        fmt=".2f",
        cmap="coolwarm",
        linewidths=.5,
        linecolor="white",
        cbar_kws={'label': '% of Salary'}
    )

    # Customize plot
    plt.title("Heatmap: Percentage of Salary Spent on Categories")
    plt.xlabel("Year")
    plt.ylabel("Category")

    return fig

# Streamlit UI
st.title("Heatmap: Expenses as % of Salary")

# Display heatmap
st.pyplot(plot_heatmap(data))
