import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Hardcoded data from the Excel file
data = [
    {"product": "avocado", "year": 2015, "yearly average price": 6.729932},
    {"product": "rice", "year": 2015, "yearly average price": 9.595833},
    {"product": "eggs", "year": 2015, "yearly average price": 23.233333},
    {"product": "banana", "year": 2015, "yearly average price": 3.647727},
    {"product": "onion", "year": 2015, "yearly average price": 3.413717},
    # ... (Add all rows similarly)
    {"product": "canola oil", "year": 2024, "yearly average price": 12.346667},
    {"product": "strawberry", "year": 2024, "yearly average price": 33.180476},
    {"product": "corn", "year": 2024, "yearly average price": 8.526996},
    {"product": "apple", "year": 2024, "yearly average price": 8.494729},
    {"product": "potato", "year": 2024, "yearly average price": 5.034356},
]

# Convert to DataFrame
products_df = pd.DataFrame(data)

# Streamlit app title
st.title("Supermarket Product Prices Over Time")

# Sidebar for product selection
selected_products = st.multiselect(
    "Select products to include in the basket:",
    options=products_df['product'].unique(),
    default=[]
)

# Slider for year range selection
year_range = st.slider(
    "Select the year range:",
    min_value=int(products_df['year'].min()),
    max_value=int(products_df['year'].max()),
    value=(2015, 2024),
)

# Filter the dataset based on user selection
filtered_df = products_df[
    (products_df['product'].isin(selected_products)) &
    (products_df['year'] >= year_range[0]) &
    (products_df['year'] <= year_range[1])
]

# Calculate the yearly total for the selected products
if not filtered_df.empty:
    total_prices = (
        filtered_df.groupby('year')['yearly average price']
        .sum()
        .reset_index()
    )
else:
    total_prices = pd.DataFrame(columns=['year', 'yearly average price'])

# Create the plot
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(
    total_prices['year'],
    total_prices['yearly average price'],
    marker='o',
    label="Total Basket Cost"
)

# Customize the plot
ax.set_xlabel("Year")
ax.set_ylabel("Total Cost (₪)")
ax.set_title("Yearly Total Cost of Selected Products")
ax.legend()
ax.grid(True)

# Display the plot in Streamlit
st.pyplot(fig)

# Display the filtered data
st.subheader("Filtered Data")
st.dataframe(filtered_df)
