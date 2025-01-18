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

# Define item icons
item_icons = {
    "avocado": "🥑",
    "rice": "🍚",
    "eggs": "🥚",
    "banana": "🍌",
    "onion": "🧅",
    "apple": "🍎",
    "potato": "🥔",
    "canola oil": "🛢️",
    "strawberry": "🍓",
    "corn": "🌽",
}

# Initialize session state for basket
if "basket" not in st.session_state:
    st.session_state.basket = []

if "selected_products" not in st.session_state:
    st.session_state.selected_products = []

# Display the supermarket layout
st.subheader("Supermarket")
supermarket_html = """
<style>
    .item {
        display: inline-block;
        margin: 10px;
        cursor: pointer;
        font-size: 40px;
        text-align: center;
    }
    .item:hover {
        transform: scale(1.2);
        transition: transform 0.2s;
    }
    .basket {
        font-size: 80px;
        margin-top: 20px;
        text-align: center;
    }
</style>
"""

st.markdown(supermarket_html, unsafe_allow_html=True)

for product, icon in item_icons.items():
    if st.button(icon):
        if product not in st.session_state.selected_products:
            st.session_state.selected_products.append(product)
            st.session_state.basket.append(icon)

# Display the basket
st.markdown("<div class='basket'>🧺 " + " ".join(st.session_state.basket) + "</div>", unsafe_allow_html=True)

# Filter the dataset based on selected products
filtered_df = products_df[products_df['product'].isin(st.session_state.selected_products)]

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
ax.set_xticks(range(2015, 2025))  # Ensure all years are shown on the x-axis
ax.legend()
ax.grid(True)

# Display the plot in Streamlit
st.pyplot(fig)
