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
    
    {"product": "avocado", "year": 2016, "yearly average price": 7.123456},
    {"product": "rice", "year": 2016, "yearly average price": 9.789012},
    {"product": "eggs", "year": 2016, "yearly average price": 23.654321},
    {"product": "banana", "year": 2016, "yearly average price": 3.876543},
    {"product": "onion", "year": 2016, "yearly average price": 3.543210},
    
    {"product": "avocado", "year": 2017, "yearly average price": 7.234567},
    {"product": "rice", "year": 2017, "yearly average price": 9.890123},
    {"product": "eggs", "year": 2017, "yearly average price": 23.765432},
    {"product": "banana", "year": 2017, "yearly average price": 4.098765},
    {"product": "onion", "year": 2017, "yearly average price": 3.654321},

    {"product": "avocado", "year": 2018, "yearly average price": 12.231},
    {"product": "rice", "year": 2018, "yearly average price": 9.928},

    {"product": "avocado", "year": 2019, "yearly average price": 11.797},
    {"product": "rice", "year": 2019, "yearly average price": 10.119},

    {"product": "avocado", "year": 2020, "yearly average price": 13.824},
    {"product": "rice", "year": 2020, "yearly average price": 10.224},

    {"product": "avocado", "year": 2021, "yearly average price": 10.747},
    {"product": "rice", "year": 2021, "yearly average price": 10.515},

    {"product": "avocado", "year": 2022, "yearly average price": 8.332},
    {"product": "rice", "year": 2022, "yearly average price": 11.038},

    {"product": "avocado", "year": 2023, "yearly average price": 11.419},
    {"product": "rice", "year": 2023, "yearly average price": 11.178},
    
    {"product": "avocado", "year": 2024, "yearly average price": 10.420},
    {"product": "rice", "year": 2024, "yearly average price": 11.272},

    {"product": "canola oil", "year": 2024, "yearly average price": 12.346667},
    {"product": "strawberry", "year": 2024, "yearly average price": 33.180476},
    {"product": "corn", "year": 2024, "yearly average price": 8.526996},
    {"product": "apple", "year": 2024, "yearly average price": 8.494729},
    {"product": "potato", "year": 2024, "yearly average price": 5.034356}
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
ax.set_xticks(range(2015,2025))
ax.legend()
ax.grid(True)

# Display the plot in Streamlit
st.pyplot(fig)
