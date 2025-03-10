import streamlit as st
import pandas as pd
import plotly.graph_objects as go

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

# Visualization function: Interactive Stairs Plot using Plotly
def plot_category_stairs_plotly(data, category, color):
    years = data["Year"].values
    values = data[category].values

    # Create Plotly figure
    fig = go.Figure()

    # Add step plot
    fig.add_trace(go.Scatter(
        x=years,
        y=values,
        mode='lines+markers',
        line=dict(color=color, width=3, shape='hv'),  # 'hv' for step-like stairs
        marker=dict(size=8, color=color),
        text=[f"<b>{value:.2f}%</b>" for value in values],  # Values to show on hover
        hoverinfo="text",
        name=f"{category} as % of Salary"
    ))

    # Calculate dynamic range
    value_range = values.max() - values.min()
    buffer = value_range * 0.5

    # Customize layout
    fig.update_layout(
        title=f"<b>{category} as % of Salary</b>",
        title_font_size=20,
        xaxis=dict(title="Year", tickmode="linear"),
        yaxis=dict(
            title="Percentage of Salary (%)",
            range=[values.min() - buffer, values.max() + buffer]  # Dynamic range
        ),
        hoverlabel=dict(
            font_size=14
        ),
        template="plotly_white",
        legend=dict(yanchor="top", y=0.99, xanchor="left", x=0.01),
        width=1600,
        height=500
    )

    return fig

# Streamlit UI
st.title("Categories as % of Salary")

# User selects category
category = st.selectbox("Choose a category:", ["Rent", "Fuel", "Basic Basket"])

# Assign unique colors for each category
category_colors = { 
    "Rent": "#40C7A3", 
    "Fuel": "#FF9800",          
    "Basic Basket": "#C19AFF"   
}

# Display interactive stairs plot for selected category
selected_color = category_colors[category]
st.plotly_chart(plot_category_stairs_plotly(data, category, selected_color))
