import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
def load_data():
    data = {
        "product": ["avocado", "rice", "eggs", "banana", "onion"],
        "year": [2015, 2015, 2015, 2015, 2015],
        "yearly average price": [6.73, 9.6, 23.23, 3.65, 3.41]
    }
    return pd.DataFrame(data)

data = load_data()

# Streamlit app
def main():
    st.title("Supermarket Product Prices (2015-2024)")
    st.write("Select products to visualize their yearly price trends.")

    # Sidebar for product selection
    products = st.multiselect(
        "Select products:", 
        options=data["product"].unique(), 
        default=data["product"].unique()
    )

    # Filter data based on selection
    filtered_data = data[data["product"].isin(products)]

    if filtered_data.empty:
        st.warning("Please select at least one product.")
    else:
        # Pivot table to calculate yearly sums
        pivot = filtered_data.pivot_table(
            index="year", 
            values="yearly average price", 
            aggfunc="sum"
        )

        # Plot the data
        st.write("### Yearly Total Prices of Selected Products")
        plt.figure(figsize=(10, 6))
        plt.plot(pivot.index, pivot["yearly average price"], marker="o", linestyle="-", label="Total Price")
        plt.title("Yearly Total Prices of Selected Products")
        plt.xlabel("Year")
        plt.ylabel("Total Price (in currency)")
        plt.grid(True)
        plt.legend()
        st.pyplot(plt)

if __name__ == "__main__":
    main()
