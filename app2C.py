# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np

# # Load data from uploaded Excel files
# @st.cache_data
# def load_data():
#     salary_df = pd.read_excel("https://raw.githubusercontent.com/inbalkat/ProjectVisu/main/salary.xlsx")
#     rent_df = pd.read_excel("https://raw.githubusercontent.com/inbalkat/ProjectVisu/main/rent.xlsx")
#     fuel_df = pd.read_excel("https://raw.githubusercontent.com/inbalkat/ProjectVisu/main/fuel.xlsx")
#     basket_df = pd.read_excel("https://raw.githubusercontent.com/inbalkat/ProjectVisu/main/basic_basket.xlsx")
#     return salary_df, rent_df, fuel_df, basket_df

# # Load the data
# salary_df, rent_df, fuel_df, basket_df = load_data()

# # Prepare data for visualization
# def prepare_data_monthly(salary_df, rent_df, fuel_df, basket_df):
#     # Calculate monthly expenses for each category
#     basket_df["monthly_expenses"] = basket_df["price for basic basket"] * 4
#     fuel_df["monthly_expenses"] = fuel_df["price per liter"] * 100

#     # Merge with salary data
#     merged_rent = rent_df.merge(salary_df, on="year")
#     merged_fuel = fuel_df.merge(salary_df, on="year")
#     merged_basket = basket_df.merge(salary_df, on="year")

#     # Calculate percentages of salary
#     rent_percent = merged_rent["price for month"] / merged_rent["salary"] * 100
#     fuel_percent = merged_fuel["monthly_expenses"] / merged_fuel["salary"] * 100
#     basket_percent = merged_basket["monthly_expenses"] / merged_basket["salary"] * 100

#     years = salary_df["year"]

#     data = pd.DataFrame({
#         "Year": years,
#         "Rent": rent_percent,
#         "Fuel": fuel_percent,
#         "Basic Basket": basket_percent
#     })
#     return data

# data = prepare_data_monthly(salary_df, rent_df, fuel_df, basket_df)

# # Visualization function: Stairs Plot for Each Category
# def plot_category_stairs(data, category, color):
#     fig, ax = plt.subplots(figsize=(10, 6))
#     years = data["Year"].values
#     values = data[category].values

#     # Create step plot
#     ax.step(years, values, label=f"{category} as % of Salary", color=color, where='mid', linewidth=3)

#     # Highlight each step with a scatter plot for clarity
#     ax.scatter(years, values, color=color, edgecolor="black", zorder=5, s=50)

#     max_val = values.max()
#     min_val = values.min()
#     buffer = (max_val-min_val) * 0.3
#     ax.set_ylim(min_val-buffer, max_val+buffer)

#     # Customize plot
#     ax.set_title(f"Stair Plot: {category} as % of Salary", fontsize=16)
#     ax.set_xlabel("Year")
#     ax.set_ylabel("Percentage of Salary (%)")
#     ax.set_xticks(years)
#     # ax.set_yticks(np.linspace(values.min(), values.max(), 5))
#     ax.legend()
#     ax.grid(True)

#     return fig

# # Streamlit UI
# st.title("Stairs Plot: Categories as % of Salary")

# # User selects category
# category = st.selectbox("Choose a category:", ["Rent", "Fuel", "Basic Basket"])

# # Assign unique colors for each category
# category_colors = {
#     "Rent": "green",
#     "Fuel": "orange",
#     "Basic Basket": "purple"
# }

# # Display stairs plot for selected category
# selected_color = category_colors[category]
# st.pyplot(plot_category_stairs(data, category, selected_color))
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
        title=f"<b>Interactive Stair Plot: {category} as % of Salary</b>",
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
st.title("Interactive Stairs Plot: Categories as % of Salary")

# User selects category
category = st.selectbox("Choose a category:", ["Rent", "Fuel", "Basic Basket"])

# Assign unique colors for each category
category_colors = {
    # "Rent": "#4CAF50",   
    "Rent": "#45D6AF", 
    "Fuel": "#FF9800",          
    "Basic Basket": "#FF73D0"   
}

# Display interactive stairs plot for selected category
selected_color = category_colors[category]
st.plotly_chart(plot_category_stairs_plotly(data, category, selected_color))
