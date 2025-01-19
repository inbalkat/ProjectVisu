
# Sort the items alphabetically
item_icons = dict(sorted(item_icons.items()))

# Initialize session state for basket
if "basket" not in st.session_state:
    st.session_state.basket = []

if "selected_products" not in st.session_state:
    st.session_state.selected_products = []

# Display the supermarket layout
supermarket_html = """
<style>
    .item {
        display: flex;
        margin: 10px;
        cursor: pointer;
        font-size: 20px;
        text-align: center;
        justify-content: center;
        align-items: center;
        padding: 10px;
        border: 1px solid #ccc;
        border-radius: 10px;
        white-space: nowrap; /* Prevent line breaks */
        max-width: 180px; /* Set a maximum width */
        overflow: hidden; /* Hide overflow */
        text-overflow: ellipsis; /* Show '...' if text is too long */
        height: 50px;
    }
    .item:hover {
        transform: scale(1.2);
        transition: transform 0.2s;
        background-color: #f0f0f0;
    }
    .cart {
        font-size: 100px;
        margin-top: 20px;
        text-align: right;
        position: relative;
        display: flex;
        align-items: center;
        justify-content: flex-end;
    }
    .cart-items {
        font-size: 40px;
        margin-right: 20px;
    }
</style>
"""

st.markdown(supermarket_html, unsafe_allow_html=True)

columns = st.columns(5)
for index, (product, icon) in enumerate(item_icons.items()):
    with columns[index % 5]:
        if st.button(f"{icon} {product.capitalize()}"):
            if product in st.session_state.selected_products:
                st.session_state.selected_products.remove(product)
                st.session_state.basket.remove(icon)
            else:
                st.session_state.selected_products.append(product)
                st.session_state.basket.append(icon)

# Display the cart
cart_html = f"""
<div class='cart'>
    <div class='cart-items'>{' '.join(st.session_state.basket)}</div>
    🛒
</div>
"""
st.markdown(cart_html, unsafe_allow_html=True)

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
    color='black',
    linewidth=2,
    label="Total Basket Cost"
)

# Customize the plot
ax.set_xlabel("Year")
ax.set_ylabel("Total Cost (₪)")
ax.set_title("Total Cost of Selected Products Over Time")
ax.set_xticks(range(2015, 2025))  # Ensure all years are shown on the x-axis
ax.legend()
ax.grid(True)

# Display the plot in Streamlit
st.pyplot(fig)
