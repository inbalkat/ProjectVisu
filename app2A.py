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

# Prepare data for a single category
def prepare_category_data(salary_df, category_df, value_column, category_name):
    # Ensure the datasets have the same years
    merged = category_df.merge(salary_df, on="year")
    
    # Calculate the category as a percentage of salary
    category_percent = merged[value_column] / merged["salary"]
    
    # Create a DataFrame for the category
    data = pd.DataFrame({
        "Year": merged["year"],
        category_name: category_percent
    })
    
    return data

# Prepare data for each category
rent_data = prepare_category_data(salary_df, rent_df, "price for month", "Rent")
fuel_data = prepare_category_data(salary_df, fuel_df, "price per liter", "Fuel")
basket_data = prepare_category_data(salary_df, basket_df, "price for basic basket", "Basic Basket")

# Visualization function: Heatmap
def plot_heatmap(data, category_name):
    fig, ax = plt.subplots(figsize=(8, 6))
    
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
    plt.title(f"Heatmap: {category_name} as % of Salary")
    plt.xlabel("Year")
    plt.ylabel("Category")

    return fig

# Streamlit UI
st.title("Heatmap: Categories as % of Salary")

# Add selection to choose category
category = st.sidebar.radio(
    "Choose a category to display:",
    ("Rent", "Fuel", "Basic Basket")
)

# Show heatmap based on the selected category
if category == "Rent":
    st.pyplot(plot_heatmap(rent_data, "Rent"))
elif category == "Fuel":
    st.pyplot(plot_heatmap(fuel_data, "Fuel"))
elif category == "Basic Basket":
    st.pyplot(plot_heatmap(basket_data, "Basic Basket"))
