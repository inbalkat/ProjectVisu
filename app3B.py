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

# Update calculations to yearly
def calculate_yearly_expenses(salary_df, rent_df, fuel_df, basket_df):
    # Update basket to 4 per month * 12 months = 48 baskets per year
    basket_df["yearly_expenses"] = basket_df["price for basic basket"] * 48
    # Fuel: Assume 100 liters per month * 12 months = 1200 liters per year
    fuel_df["yearly_expenses"] = fuel_df["price per liter"] * 1200
    # Rent: Already yearly
    rent_df["yearly_expenses"] = rent_df["price for month"] * 12
    # Combine all yearly expenses
    salary_df["yearly_salary"] = salary_df["salary"] * 12
    merged_df = salary_df[["year", "yearly_salary"]].copy()
    merged_df["rent"] = rent_df["yearly_expenses"].values
    merged_df["fuel"] = fuel_df["yearly_expenses"].values
    merged_df["basket"] = basket_df["yearly_expenses"].values
    merged_df["total_expenses"] = (
        merged_df["rent"] + merged_df["fuel"] + merged_df["basket"]
    )
    return merged_df

# Visualization: Pie Chart for Selected Years
def plot_pie_chart_for_year(year_data):
    labels = ["Rent", "Fuel", "Basic Shopping Basket"]
    sizes = [year_data["rent"], year_data["fuel"], year_data["basket"]]
    colors = ["#FF9999", "#66B2FF", "#99FF99"]
    explode = (0.1, 0, 0)  # Slightly "explode" the first slice (Rent)

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.pie(
        sizes, labels=labels, autopct="%1.1f%%", startangle=140, colors=colors, explode=explode
    )
    ax.set_title(f"Expenses Breakdown for {year_data['year']}")
    return fig

# Streamlit UI
st.title("Income vs. Expenses - Yearly Breakdown")
st.sidebar.title("Year Selection")

# Calculate yearly expenses and salaries
merged_df = calculate_yearly_expenses(salary_df, rent_df, fuel_df, basket_df)

# Sidebar for year selection
available_years = merged_df["year"].tolist()
selected_years = st.sidebar.multiselect("Select Years to Display:", available_years, default=available_years)

# Filter data based on selected years
filtered_df = merged_df[merged_df["year"].isin(selected_years)]

# Display pie charts for selected years
if filtered_df.empty:
    st.write("No years selected. Please choose at least one year from the sidebar.")
else:
    for _, row in filtered_df.iterrows():
        st.pyplot(plot_pie_chart_for_year(row))
