import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
file_path = '/mnt/data/products.xlsx'
products_df = pd.read_excel(file_path)

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
