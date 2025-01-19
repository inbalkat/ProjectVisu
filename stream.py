import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Define separate app functions
def app1():
    st.title("Supermarket Product Prices Over Time")
    # Insert the full code for App 1 here
    st.write("This is App 1: Supermarket Product Prices Over Time.")

def app2():
    st.title("Categories as % of Salary")
    # Insert the full code for App 2 here
    st.write("This is App 2: Categories as % of Salary.")

def app3():
    st.title("Income vs Expenses")
    # Insert the full code for App 3 here
    st.write("This is App 3: Income vs Expenses.")

# Main navigation
def main():
    st.sidebar.title("Navigation")
    app_choice = st.sidebar.radio(
        "Choose an app:", 
        ["Supermarket Product Prices Over Time", "Categories as % of Salary", "Income vs Expenses"]
    )

    if app_choice == "Supermarket Product Prices Over Time":
        app1()
    elif app_choice == "Categories as % of Salary":
        app2()
    elif app_choice == "Income vs Expenses":
        app3()

if __name__ == "__main__":
    main()
